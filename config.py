"""
Configuration file for the Stock Exchange Discord Bot
Contains all constant values, settings, and configurations
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot token from environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Channel IDs
ACTIVE_CHANNEL_IDS = [1276652104253051005, 1347853900799152211, 1288198542741213224, 1288198542741213224]
STOCK_CHANNEL_ID = 1347853926044799008
LEADERBOARD_CHANNEL_ID = 1347853992008351764

# Economy settings
DAILY_CAP = 60
DAILY_REWARD_MIN = 15
DAILY_REWARD_MAX = 100
SELLING_FEE = 7  # Fee to sell stocks

# Message rewards
MESSAGE_REWARD_MIN = 1
MESSAGE_REWARD_MAX = 3
REACTION_REWARD_AUTHOR_MIN = 2
REACTION_REWARD_AUTHOR_MAX = 5
REACTION_REWARD_REACTOR_MIN = 1
REACTION_REWARD_REACTOR_MAX = 2

# File paths
USER_DATA_FILE = "user_data.json"
STOCKS_FILE = "stocks.json"
STOCK_MESSAGES_FILE = "stocks_messages.json"
LOGO_FILE = "logo.png"

# Stock configuration
STOCK_SYMBOLS = [
    "$BBST", "$PETE", "$SWAG", "$GAGE", "$HNME", "$WREX", "$LAND", 
    "$BRAN", "$KYLE", "$HAKM", "$SAM", "$NUTB", "$MJRK"
]

# Mapping of user IDs to their ticker symbols
USER_TO_TICKER = {
    "140696029489004544": "$BBST", "102216667047690240": "$PETE",
    "195325076848115722": "$SWAG", "411412236725256204": "$HNME",
    "203284441122996224": "$WREX", "690423460027039755": "$LAND",
    "490011081251487766": "$BRAN", "205044983382802432": "$KYLE",
    "126535729156194304": "$GAGE", "127566924992217089": "$SAM",
    "380842798359904267": "$NUTB", "185924063464521730": "$MJRK"
}

# Update settings
STOCK_UPDATE_INTERVAL = 45  # minutes
LEADERBOARD_UPDATE_INTERVAL = 15  # minutes
STOCK_PRICE_MIN_CHANGE = -3
STOCK_PRICE_MAX_CHANGE = 3
NEW_STOCK_MIN_PRICE = 80
NEW_STOCK_MAX_PRICE = 90
STOCK_BUY_MIN_CHANGE = 3
STOCK_BUY_MAX_CHANGE = 9
STOCK_SELL_MIN_CHANGE = 3
STOCK_SELL_MAX_CHANGE = 9

# Colors
COLOR_SUCCESS = 0x00FF00  # Green
COLOR_ERROR = 0xFF0000  # Red
COLOR_INFO = 0x3498DB  # Blue
COLOR_WARNING = 0xFFD700  # Gold
COLOR_SPECIAL = 0xE91E63  # Pink
COLOR_DISCORD = 0x7289DA  # Discord Blurple

# Command list for help 
COMMANDS = {
    "Economy": [
        ("!balance or !bal", "Check your $USD balance"),
        ("!daily", "Claim daily reward"),
        ("!gift <@user> <amount>", "Gift $USD to another user")
    ],
    "Stocks": [
        ("!mystocks or !portfolio", "View your stock portfolio"),
        ("!stock <symbol>", "Check a stock price and chart")
    ],
    "Info": [
        ("!about", "About this bot"),
        ("!help", "Show this command menu")
    ]
}

# Default user data
DEFAULT_USER_DATA = {
    "balance": 50,
    "inventory": {},
    "last_daily": None,
    "bank": 0,
    "date": None,
    "earned": 0
}