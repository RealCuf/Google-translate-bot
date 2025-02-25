# Import necessary modules from Pyrogram
from pyrogram import Client, idle  # Client for creating the bot, idle to keep the bot running
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid  # Error handling for common issues
import plugins.start  # Importing custom plugins (e.g., start command)
import os  # For accessing environment variables

# Getting the Bot Token from environment variables
# Default value is provided for local testing
BOT_TOKEN = os.environ.get('BOT_TOKEN', '#')

# Getting the API ID from environment variables and converting it to an integer
APP_ID = int(os.environ.get('API_ID', '#'))

# Getting the API Hash from environment variables
API_HASH = os.environ.get('API_HASH', '#')

# Configuring the plugin folder
# This tells Pyrogram to look for bot commands and handlers inside the 'plugins' folder
plugins = dict(
    root='plugins',
)

# Creating a Client instance for the bot
app = Client(
    name='bot',  # Name of the session
    plugins=plugins,  # Setting the plugin folder
    api_id=APP_ID,  # API ID for Telegram
    api_hash=API_HASH,  # API Hash for Telegram
    bot_token=BOT_TOKEN,  # Bot Token from BotFather
)

# Main entry point of the script
if __name__ == "__main__":
    try:
        # Starting the bot
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        # Error if API_ID or API_HASH is invalid
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        # Error if BOT_TOKEN is invalid
        raise Exception("Your BOT_TOKEN is not valid.")
    
    # Getting the bot's username to confirm successful startup
    uname = app.get_me().username
    print(f"@{uname} Started Successfully!")

    # Keeps the bot running and listens for new updates
    idle()

    # Stops the bot when interrupted (e.g., Ctrl+C)
    app.stop()
    print("Bot stopped. Alvida!")  # Alvida means goodbye in Hindi/Urdu
