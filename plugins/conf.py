from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # Import necessary classes for creating inline buttons

# Start message text with f-string placeholder for the user's name
start_text = """Welcome dear {user_name} 🦉
This bot will translate messages and send translated text as voice.
It supports 81 languages.

To get started, send your text to receive the translation 🙂"""

# Help message text
help_text = """Currently, the bot will automatically recognize the source language by default, first send your text to change the destination language.

If you get into trouble, message to support 🙂"""

# URL of the image to be sent with the language selection message
photo = "https://postimg.cc/sMKJSCYD"

# Caption for the photo
photo_caption = """Determine Language:

Please select one of the following 🙂"""

# account link for the support
support_url = "https://github.com/RealCuf"

# link for the ADs
ads_url = "https://github.com/RealCuf"

# Inline keyboard for the start message
start_reply_markup = InlineKeyboardMarkup(
            [
                [
                    # Button linking to a support page (e.g., GitHub)
                    InlineKeyboardButton(text='Support', url=support_url),
                    # Button that triggers a callback for help
                    InlineKeyboardButton(text='Help', callback_data='help')
                ],
            ]
        )

# Inline keyboard for the help message
help_reply_markup = InlineKeyboardMarkup(
            [
                [
                    # Button linking to a support page (e.g., GitHub)
                    InlineKeyboardButton(text='Support', url=support_url),
                ],
            ]
        )