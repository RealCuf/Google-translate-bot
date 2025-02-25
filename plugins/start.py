# Importing required modules from Pyrogram
from pyrogram import Client, filters  # Client is used to create the bot, filters for filtering messages
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery  # Telegram-specific types
import plugins.conf as conf  # Importing configuration data (like texts and buttons) from a separate config file

# Dictionary to store user text data temporarily
user_text_data = {}

# Handler for the /start command in private chats
@Client.on_message(filters.command('start') & filters.private)
def start_handler(client: Client, message: Message):
    user = message.from_user  # Get information about the user who sent the message
    # Send a photo with a welcome caption and inline buttons
    message.reply_photo(
        photo=conf.photo,  # Photo URL imported from conf.py
        caption=conf.start_text.format(user_name=user.first_name),  # Personalized welcome message
        reply_markup=conf.start_reply_markup  # Inline keyboard for Support and Help buttons
    )

# Handler for the /help command in private chats
@Client.on_message(filters.command('help') & filters.private)
def help_handler(client: Client, message: Message):
    # Send a text with help text and inline buttons
    message.reply_text(
        text=conf.help_text,  # Help text imported from conf.py
        reply_markup=conf.help_reply_markup  # Inline keyboard for help navigation
    )

# Handler for text messages in private chats (to initiate translation)
@Client.on_message(filters.text & filters.private)
def translate_handler(client: Client, message: Message):
    utext = message.text  # Get the text sent by the user
    user_text_data[message.from_user.id] = utext  # Store the text associated with the user ID

    # Send a photo with a language selection menu using InlineKeyboardMarkup
    message.reply_photo(
        photo=conf.photo,  # Photo URL for language selection
        caption=conf.photo_caption,  # Caption prompting the user to select a language
        reply_markup=InlineKeyboardMarkup(
            [
                # Creating multiple rows of inline buttons for language selection
                [
                    InlineKeyboardButton(text='🇮🇷 Iran', callback_data='fa'),
                    InlineKeyboardButton(text='🇺🇸 USA', callback_data='en'),
                    InlineKeyboardButton(text='🇫🇷 France', callback_data='fr')
                ],
                [
                    InlineKeyboardButton(text='🇩🇪 Germany', callback_data='de'),
                    InlineKeyboardButton(text='🇸🇦 Arabic', callback_data='ar'),
                    InlineKeyboardButton(text='🇯🇵 Japanese', callback_data='ja')
                ],
                [
                    InlineKeyboardButton(text='🇦🇫 Afghanistan', callback_data='af'),
                    InlineKeyboardButton(text='🇦🇱 Albania', callback_data='sq'),
                    InlineKeyboardButton(text='🇪🇹 Ethiopia', callback_data='am')
                ],
                [
                    InlineKeyboardButton(text='🇦🇲 Armenia', callback_data='hy'),
                    InlineKeyboardButton(text='🇦🇿 Azerbaijan', callback_data='az'),
                    InlineKeyboardButton(text='🇪🇸 Basque Country', callback_data='eu')
                ],
                [
                    InlineKeyboardButton(text='🇧🇾 Belarus', callback_data='be'),
                    InlineKeyboardButton(text='🇧🇩 Bangladesh', callback_data='bn'),
                    InlineKeyboardButton(text='🇧🇦 Bosnia', callback_data='bs')
                ],
                [
                    InlineKeyboardButton(text='🇧🇬 Bulgaria', callback_data='bg'),
                    InlineKeyboardButton(text='🇪🇸 Catalonia', callback_data='ca'),
                    InlineKeyboardButton(text='🇵🇭 Philippines', callback_data='ceb')
                ],
                [
                    InlineKeyboardButton(text='🇲🇼 Malawi', callback_data='ny'),
                    InlineKeyboardButton(text='🇨🇳 China', callback_data='zh-cn'),
                    InlineKeyboardButton(text='🇹🇼 Taiwan', callback_data='zh-tw')
                ],
                [
                    InlineKeyboardButton(text='🇫🇷 Corsica', callback_data='co'),
                    InlineKeyboardButton(text='🇭🇷 Croatia', callback_data='hr'),
                    InlineKeyboardButton(text='🇨🇿 Czech Republic', callback_data='cs')
                ],
                [
                    InlineKeyboardButton(text='🇩🇰 Denmark', callback_data='da'),
                    InlineKeyboardButton(text='🇳🇱 Netherlands', callback_data='nl'),
                    InlineKeyboardButton(text='🇪🇪 Estonia', callback_data='et')
                ],
                [
                    InlineKeyboardButton(text='🇵🇭 Philippines', callback_data='tl'),
                    InlineKeyboardButton(text='🇫🇮 Finland', callback_data='fi'),
                    InlineKeyboardButton(text='🇳🇱 Friesland', callback_data='fy')
                ],
                [
                    InlineKeyboardButton(text='🇪🇸 Galicia', callback_data='gl'),
                    InlineKeyboardButton(text='🇬🇪 Georgia', callback_data='ka'),
                    InlineKeyboardButton(text='🇬🇷 Greece', callback_data='el')
                ],
                [
                    InlineKeyboardButton(text='🇮🇳 India', callback_data='gu'),
                    InlineKeyboardButton(text='🇭🇹 Haiti', callback_data='ht'),
                    InlineKeyboardButton(text='🇳🇬 Nigeria', callback_data='ha')
                ],
                [
                    InlineKeyboardButton(text='🇺🇸 Hawaii', callback_data='haw'),
                    InlineKeyboardButton(text='🇮🇱 Israel', callback_data='iw'),
                    InlineKeyboardButton(text='🇭🇺 Hungary', callback_data='hu')
                ],
                [
                    InlineKeyboardButton(text='🇮🇸 Iceland', callback_data='es'),
                    InlineKeyboardButton(text='🇮🇩 Indonesia', callback_data='id'),
                    InlineKeyboardButton(text='🇮🇪 Ireland', callback_data='ga')
                ],              
                [
                    InlineKeyboardButton(text='🇮🇹 Italy', callback_data='it'),
                    InlineKeyboardButton(text='🇰🇿 Kazakhstan', callback_data='kk'),
                    InlineKeyboardButton(text='🇰🇭 Cambodia', callback_data='km')
                ],
                [
                    InlineKeyboardButton(text='🇰🇷 South Korea', callback_data='ko'),
                    InlineKeyboardButton(text='🇹🇷 Turkey', callback_data='tr'),
                    InlineKeyboardButton(text='🇰🇬 Kyrgyzstan', callback_data='ky')
                ],
                [
                    InlineKeyboardButton(text='🇱🇦 Laos', callback_data='lo'),
                    InlineKeyboardButton(text='🇻🇦 Vatican', callback_data='la'),
                    InlineKeyboardButton(text='🇱🇻 Latvia', callback_data='lv')
                ],
                [
                    InlineKeyboardButton(text='🇱🇹 Lithuania', callback_data='lt'),
                    InlineKeyboardButton(text='🇱🇺 Luxembourg', callback_data='lb'),
                    InlineKeyboardButton(text='🇲🇰 North Macedonia', callback_data='mk')
                ],
                [
                    InlineKeyboardButton(text='🇲🇬 Madagascar', callback_data='mg'),
                    InlineKeyboardButton(text='🇲🇾 Malaysia', callback_data='ms'),
                    InlineKeyboardButton(text='🇲🇹 Malta', callback_data='mt')
                ],
                [
                    InlineKeyboardButton(text='🇳🇿 New Zealand', callback_data='mi'),
                    InlineKeyboardButton(text='🇲🇳 Mongolia', callback_data='mn'),
                    InlineKeyboardButton(text='🇲🇲 Myanmar', callback_data='my')
                ],
                [
                    InlineKeyboardButton(text='🇵🇰 Pakistan', callback_data='ur'),
                    InlineKeyboardButton(text='🇺🇦 Ukraine', callback_data='uk'),
                    InlineKeyboardButton(text='🇹🇭 Thailand', callback_data='th')
                ],
                [
                    InlineKeyboardButton(text='🇹🇯 Tajikistan', callback_data='tg'),
                    InlineKeyboardButton(text='🇸🇪 Sweden', callback_data='sv'),
                    InlineKeyboardButton(text='🇪🇸 Spain', callback_data='es')
                ],
                [
                    InlineKeyboardButton(text='🇸🇴 Somalia', callback_data='so'),
                    InlineKeyboardButton(text='🇸🇰 Slovakia', callback_data='sk'),
                    InlineKeyboardButton(text='🇱🇰 Sri Lanka', callback_data='si')
                ],
                [
                    InlineKeyboardButton(text='🇿🇼 Zimbabwe', callback_data='sn'),
                    InlineKeyboardButton(text='🇱🇸 Lesotho', callback_data='st'),
                    InlineKeyboardButton(text='🇷🇸 Serbia', callback_data='sr')
                ]
            ]
        )
    )
