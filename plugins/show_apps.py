from io import BytesIO
from pyrogram.filters import *
from sample_config import Config
from pyrogram import Client, filters
from helpers.herokuu import app, h_conn
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Client.on_message(filters.command(["apps", f"apps@{Config.BOT_USERNAME}"]))
async def list_apps(bot, update):
    if update.from_user.id not in Config.ADMINS:
        await update.reply_text("You are not allowed to use this command.")
        return

    inline_keyboard = []
    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    # looping for all the apps added
    i = 0
    while i < len(app):
        if app[i] and app[i+1] is not None:
            inline_keyboard.append([
                InlineKeyboardButton(
                    text=app[i], 
                    callback_data=f"sett_{i}"
                ),
                InlineKeyboardButton(
                    text=app[i+1],
                    callback_data=f"sett_{i+1}"
                )
                ])
        elif app[i] is None and not i+1 >= len(app) and not i >= len(app):
            if app[i+1] is not None:
                inline_keyboard.append([
                    InlineKeyboardButton(
                        text=app[i+1],
                        callback_data=f"sett_{i+1}"
                    )
                    ])
        elif app[i] is not None and app[i+1] is None:
            inline_keyboard.append([
                InlineKeyboardButton(
                    text=app[i],
                    callback_data=f"sett_{i}"
                )
                ])
        # 2 apps managed at once so.....
        i = i + 2

    inline_keyboard.append([
        InlineKeyboardButton(
            text="❌ CLOSE MENU ❌",
            callback_data="close"
        )
    ])
    await bot.send_message(
        chat_id=update.chat.id,
        text="Choose the APP below",
        reply_markup=reply_markup
    )

@Client.on_callback_query()
async def setting_handler(c: Client, cb: CallbackQuery):
    if cb.from_user.id not in Config.ADMINS:
        await cb.answer(f"You are not Authorised 🤭", show_alert=True)
        return

    data = cb.data

    if data == "close":
        await cb.answer("Closed 🙂")
        await cb.message.edit_text("Closed Menu")
        return

    if data.startswith("sett_"):
        data = data.replace("sett_", "")
        data = int(data)
        await cb.message.edit_reply_markup(
            InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⏹️ SHUTDOWN ⏹️",
                        callback_data=f"shutdown_{data}")],
                    [InlineKeyboardButton("🔃 RESTART 🔃",
                        callback_data=f"restart_{data}")],
                    [InlineKeyboardButton("▶️ BOOT ▶️",
                        callback_data=f"boot_{data}")],
                    [InlineKeyboardButton("📜 LOGS 📜",
                        callback_data=f"logs_{data}")],
                    [InlineKeyboardButton("❌ CLOSE MENU ❌",
                        callback_data="close")]
                ]
            )
        )
        return

    elif data.startswith("shutdown_"):
        data = data.replace("shutdown_", "")
        data = int(data)
        try:
            happ = h_conn[data].apps()[app[data]]
            happ.change_connection(h_conn[data])
            happ.process_formation()["worker"].scale(0)
            await cb.answer(f"Shutting Down - {app[data]}", show_alert=True)
        except Exception as e:
            await cb.answer(f"Error: {e}", show_alert=True)
        return

    elif data.startswith("restart_"):
        data = data.replace("restart_", "")
        data = int(data)
        try:
            happ = h_conn[data].apps()[app[data]]
            happ.change_connection(h_conn[data])
            happ.restart()
            await cb.answer(f"Restarting - {app[data]}", show_alert=True)
        except Exception as e:
            await cb.answer(f"Error: {e}", show_alert=True)
        return

    elif data.startswith("boot_"):
        data = data.replace("boot_", "")
        data = int(data)
        try:
            happ = h_conn[data].apps()[app[data]]
            happ.change_connection(h_conn[data])
            happ.process_formation()["worker"].scale(1)
            await cb.answer(f"Booting - {app[data]}", show_alert=True)
        except Exception as e:
            await cb.answer(f"Error: {e}", show_alert=True)
        return

    elif data.startswith("logs_"):
        data = data.replace("logs_", "")
        data = int(data)
        try:
            happ = h_conn[data].apps()[app[data]]
            happ.change_connection(h_conn[data])
            log = happ.get_log()
            file = BytesIO(bytes(log, "utf-8"))
            file.name = f"{app[data]}_log.txt"
            await cb.message.reply_document(file)
        except Exception as e:
            await cb.answer(f"Error: {e}", show_alert=True)
        return

