from sample_config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

msg = f"""<b>•••         HELLO SIR         •••</b>

I'm a bot that can help you manage your Heroku apps.
Use /apps to see the list of apps you have."""

@Client.on_message(filters.command(["start", f"start@{Config.BOT_USERNAME}"]))
async def start(bot, update):
        await bot.send_message(
           chat_id=update.chat.id,
            text=MsgText.StartText,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Source", url="https://github.com/vinayak-7-0-3/heroku-tg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "Owner", url="https://t.me/v_m_7_0_3"
                        )
                    ],
                ]
            ),
            reply_to_message_id=update.message_id
        )

        
        

    

    
        
        
