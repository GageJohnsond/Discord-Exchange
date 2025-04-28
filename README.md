# Discord Exchange Bot

A Discord bot that simulates a local Stock Exchange, allowing users to earn virtual currency, trade eachothers stocks, and promotes interaction with the discord.

## Features

- Virtual currency system 
- Stock market simulation with real-time price updates
- Interactive commands with button-based UI
- Daily rewards and message/reaction based earnings
- Persistent leaderboards that update automatically

## Structure

The bot is organized into modular components:

- `main.py` - Entry point for the bot
- `config.py` - Configuration settings and constants
- `data_manager.py` - Handles loading and saving data
- `user_manager.py` - User account and balance management
- `stock_manager.py` - Stock market simulation
- `external_api.py` - Integration with external APIs
- `ui_components.py` - Discord UI components (buttons, views)
- `commands.py` - Bot command definitions
- `event_handlers.py` - Discord event handlers
- `leaderboard_manager.py` - Persistent leaderboard management

## Setup

1. Clone the repository
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Discord bot token:
   ```
   DISCORD_BOT_TOKEN=your_token_here
   ```
4. Run the bot:
   ```
   python main.py
   ```

## Commands

### Economy Commands
- `!balance` - Check your balance
- `!daily` - Claim daily reward
- `!gift <@user> <amount>` - Gift to another user
- `!leaderboard` - Show top holders

### Stock Market Commands
- `!stocks` - Show most valuable stocks
- `!mystocks` - View your stock portfolio
- `!stock <symbol>` - Check a specific stock price and chart



### Information Commands
- `!about` - About this bot
- `!what` - Show command menu

## Currency Earning

Users can earn $USD by being active in the server.