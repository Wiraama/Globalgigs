import asyncio, threading, os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler, Application, CommandHandler, ContextTypes, MessageHandler, filters
from v1.models.database import User
from v1.extension import SessionLocal

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

def get_user(update: Update):
    tg_user = update.message.from_user
    
    session = SessionLocal()
    
    user = session.query(User).filter_by(tel_id=tg_user.id).first()
    if not user:
        new_user = User(
            tel_id=tg_user.id,
            f_name=tg_user.first_name,
            l_name=tg_user.last_name
        )
        session.add(new_user)
        session.commit()
    session.close()

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