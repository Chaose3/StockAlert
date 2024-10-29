import os
import discord
import yahoofinance as yf

TOKEN = os.getenv('DISCORD_TOKEN')  # Make sure to set your Discord token as an environment variable
CHANNEL_ID = os.getenv('CHANNEL_ID')  # Set your channel ID
if CHANNEL_ID is None:
	raise ValueError("CHANNEL_ID environment variable is not set.")
CHANNEL_ID = int(CHANNEL_ID)  # Convert to integer after checking

client = discord.Client(intents=discord.Intents.default())


def calculate_indicators(data):
	# Moving Averages
	data['SMA_50'] = data['Close'].rolling(window=50).mean()
	data['SMA_200'] = data['Close'].rolling(window=200).mean()

	# RSI
	delta = data['Close'].diff(1)
	gain = delta.where(delta > 0, 0)
	loss = -delta.where(delta < 0, 0)
	avg_gain = gain.rolling(window=14).mean()
	avg_loss = loss.rolling(window=14).mean()
	rs = avg_gain / avg_loss
	data['RSI'] = 100 - (100 / (1 + rs))

	# MACD
	data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
	data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
	data['MACD'] = data['EMA_12'] - data['EMA_26']
	data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

	return data


def generate_signals(data):
	signals = []

	# Moving Average Buy/Sell Signals
	if data['SMA_50'].iloc[-1] > data['SMA_200'].iloc[-1]:
		signals.append("Buy signal from Moving Average Crossover (SMA 50 > SMA 200).")
	elif data['SMA_50'].iloc[-1] < data['SMA_200'].iloc[-1]:
		signals.append("Sell signal from Moving Average Crossover (SMA 50 < SMA 200).")

	# RSI Buy/Sell Signals
	if data['RSI'].iloc[-1] < 30:
		signals.append("Buy signal from RSI (RSI < 30).")
	elif data['RSI'].iloc[-1] > 70:
		signals.append("Sell signal from RSI (RSI > 70).")

	# MACD Buy/Sell Signals
	if data['MACD'].iloc[-1] > data['Signal_Line'].iloc[-1]:
		signals.append("Buy signal from MACD crossover (MACD > Signal Line).")
	elif data['MACD'].iloc[-1] < data['Signal_Line'].iloc[-1]:
		signals.append("Sell signal from MACD crossover (MACD < Signal Line).")

	return signals


async def alert_signals(ticker):
	data = yf.download(ticker, period='6mo', interval='1d')
	data = calculate_indicators(data)
	signals = generate_signals(data)

	if signals:
		message = f"Signals for {ticker}:\n" + "\n".join(signals)
	else:
		message = f"No significant signals for {ticker}."

	return message


@client.event
async def on_ready():
	print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!stock'):
		ticker = message.content.split(' ')[1]
		signals_message = await alert_signals(ticker)
		await message.channel.send(signals_message)


client.run(TOKEN)