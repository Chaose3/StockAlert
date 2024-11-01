# 📈 Discord Stock Alert Bot

This bot sends daily stock signals and alerts based on technical indicators (RSI, SMA, and MACD) to a Discord channel. Built with `discord.py`, `yfinance`, and `APScheduler`.

## ⚙️ Features

- Daily stock signals posted automatically to a Discord channel.
- Supports basic technical analysis indicators:
  - **Simple Moving Average (SMA)** crossover signals.
  - **Relative Strength Index (RSI)** overbought/oversold signals.
  - **Moving Average Convergence Divergence (MACD)** crossover signals.
- Slash commands to check stock signals for specific tickers and to clear messages.

---

## 🛠️ Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Chaose3/discord-stock-alert-bot.git
    cd discord-stock-alert-bot
    ```

2. **Install Dependencies**

    ```bash
    pip install discord.py yfinance APScheduler
    ```

3. **Set Up Environment Variables**

   This bot requires two environment variables: `DISCORD_TOKEN` (your bot's token) and `CHANNEL_ID` (the ID of the channel to post alerts). You can set them up by creating a `.env` file or exporting them directly.

    ```bash
    export DISCORD_TOKEN=your_discord_token_here
    export CHANNEL_ID=your_discord_channel_id_here
    ```

   Alternatively, create a `.env` file in the project root:

    ```plaintext
    DISCORD_TOKEN=your_discord_token_here
    CHANNEL_ID=your_discord_channel_id_here
    ```

4. **Run the Bot**

    ```bash
    python bot.py
    ```

---

## 🗂️ File Structure

- `bot.py`: Main script for the bot with stock alerts, indicators calculation, and slash commands.
- `.env`: File for environment variables (add `DISCORD_TOKEN` and `CHANNEL_ID` here).

---

## 🧩 Commands

- **`/stock <ticker>`**: Get real-time signals for a specified stock ticker (e.g., `/stock AAPL`).
- **`/company <company_name>`**: Get the stock ticker for a specified company.
- **`/clear <amount>`**: Clear the specified number of messages from the chat.

---

## 📊 Technical Indicators Used

### 1. Simple Moving Average (SMA)
   - Uses a 50-day and 200-day moving average to generate buy/sell signals.

### 2. Relative Strength Index (RSI)
   - Provides signals when the RSI falls below 30 (buy) or rises above 70 (sell).

### 3. Moving Average Convergence Divergence (MACD)
   - Utilizes a 12-day and 26-day EMA to generate crossover signals.

---

## 📝 Usage Example

1. Start the bot:
    ```bash
    python3 bot.py
    ```

2. Use commands in your Discord server:
   - `/stock AAPL` to check signals for Apple.
   - `/company Microsoft` to get the ticker symbol for Microsoft.
   - `/clear 10` to clear the last 10 messages in the channel.

---

## 🐞 Troubleshooting

- **Invalid Discord Token**: Check that your token in `.env` is correct.
- **Channel ID Issues**: Ensure the bot has permission to access the channel specified by `CHANNEL_ID`.
- **Command Not Found**: Make sure your bot has message content and slash command intents enabled in the Discord Developer Portal.

---

## 📃 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💬 Support

For questions or support, open an issue or contact Chaose3 on discord
