### Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/Chaose3/StockAlert.git
   cd StockAlert
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install yfinance pandas numpy discord.py
   ```

4. **Set up environment variables**:
   Make sure to set your Discord token and channel ID as environment variables in your terminal:
   ```
   export DISCORD_TOKEN='your_discord_token'  # On Windows use `set DISCORD_TOKEN=your_discord_token`
   export CHANNEL_ID='your_channel_id'  # On Windows use `set CHANNEL_ID=your_channel_id`
   ```
