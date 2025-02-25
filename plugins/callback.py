# Import necessary libraries
from googletrans import Translator  # For translating text
from pyrogram import Client  # For interacting with the Telegram API
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery  # For creating inline buttons
from gtts import gTTS  # For converting text to voice
import plugins.conf as conf # To use text and inline keyboard data
import plugins.start as s  # To use user input data
import os  # For file management

# Function to translate text
def translate_text(utext, dest_lang):
    translator = Translator()  # Create a Translator object
    detected_lang = translator.detect(utext).lang  # Detect the language of the input text
    result = translator.translate(utext, dest=dest_lang, src=detected_lang)  # Translate the text to the target language
    return result.text  # Return the translated text

# Function to convert translated text to voice
def voice_text(result, dest_lang, uid):
    speech = gTTS(text=result, lang=dest_lang, slow=False)  # Create a speech object using gTTS
    speech.save(f"{uid}.ogg")  # Save the audio file with the user ID as the filename

# Handler for language selection callback
@Client.on_callback_query()
async def language_selection_handler(client: Client, callback: CallbackQuery):
    
    if callback.data == 'help':
        await callback.message.reply_text(
            text=conf.help_text,
            reply_markup=conf.help_reply_markup
            )
    try:
        # Retrieve user text and target language
        utext = s.user_text_data.get(callback.from_user.id)
        dest_lang = callback.data
        uid = callback.from_user.id

        # Translate the user text
        result = translate_text(utext, dest_lang)

        # Convert the translated text to voice
        voice_text(result, dest_lang, uid)

        # Send the voice message along with the translated text
        await client.send_voice(
            callback.from_user.id,
            voice=f"{callback.from_user.id}.ogg",
            caption=f"""Translation:
            
{result}""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text='Ads', url=conf.ads_url)
                    ]
                ]
            ),
        )

        # Remove the audio file after sending it
        os.remove(f"{callback.from_user.id}.ogg")

    except:
        # If an error occurs, send the translated text as a message
        await callback.message.reply_text(
            text=f"""Translation:
            
{result}""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text='Ads', url='https://github.com/RealCuf')
                    ]
                ]
            ),
        )