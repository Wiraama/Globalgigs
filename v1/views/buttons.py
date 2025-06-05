import asyncio, threading, os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler, Application, CommandHandler, ContextTypes, MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    get_user(update)
    keyboard = [
        [
            InlineKeyboardButton("See All Jobs Links", callback_data="get_gigs"),
            InlineKeyboardButton("Main Menu", callback_data="specific")
        ],
        [
            InlineKeyboardButton("Search", callback_data="search")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await update.message.reply_text(
            "*Global Gigs*!\nChoose an option:",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    except TimedOut:
        print("❌ Failed to send message: Timed out")

async def nextprev(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Main Menu", callback_data="specific"),
            InlineKeyboardButton("Next >>", callback_data="next")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Proceed to next",
        reply_markup=reply_markup
    )