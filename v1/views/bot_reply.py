from telegram.ext import CallbackQueryHandler, Application, CommandHandler, ContextTypes, MessageHandler, filters
import asyncio, threading, os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ChatAction
from .gig_dist import ask_database
from telegram.error import TimedOut, TelegramError
from telegram.request import HTTPXRequest
from v1.models.database import User
from v1.extension import SessionLocal
from v1.views.buttons import start, nextprev, get_user
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = 'https://06b0-102-209-56-114.ngrok-free.app/telegram'
PAGE_SIZE = 10

if not TOKEN:
    raise ValueError("Bot token not found in environment variables")

# create application
bot_app = Application.builder().token(TOKEN).request(HTTPXRequest(connect_timeout=10.0, read_timeout=10.0)).build()

loop = asyncio.new_event_loop()


async def setup_bot():
    await bot_app.initialize()
    await bot_app.bot.set_webhook(WEBHOOK_URL)

def start_webhook():
    asyncio.run(setup_bot())


def run_loop():
    asyncio.set_event_loop(loop)
    loop.run_until_complete(setup_bot())
    loop.run_forever()


async def send_gigs_page(update: Update, context):
    query = update.callback_query
    gigs = context.user_data["gigs"]
    page = context.user_data["page"]

    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    
    send_func = query.message.reply_text if query else update.message.reply_text
    
    if start >= len(gigs):
        await send_func("No more gigs.")
        await start(update, context)
        return

    for row in gigs[start:end]:
        await send_func(f"{row[1]}\n{row[3]}")
 
    if end < len(gigs):
        await nextprev(update, context)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    gigs = ask_database()

    if query.data == "get_gigs":
        context.user_data["gigs"] = gigs
        context.user_data["page"] = 0
        await send_gigs_page(update, context)

    elif query.data == "next":
        context.user_data["page"] += 1
        await send_gigs_page(update, context)
        
    elif query.data == "specific":
        await department(update, context)
    elif query.data == "search":
        query = update.callback_query
        await query.answer()
        await query.message.reply_text("Enter Your Keyword")
        context.user_data["awaiting_keyword"] = True

    elif query.data == "teaching":
        teaching_jobs = []

        for row in gigs:
            title = row[1].lower()
            if "principal" in title or "teacher" in title or "teaching" in title:
                teaching_jobs.append(row)

        if teaching_jobs:
            await query.message.reply_text("Teaching Jobs Found:")
            context.user_data["gigs"] = teaching_jobs
            context.user_data["page"] = 0
            await send_gigs_page(update, context)
        else:
            await query.message.reply_text("OOOPS!!!\nNo Jobs Related To Teaching Currently")
            await start(update, context)
    elif query.data == "security":
        security_jobs = []
        for row in gigs:
            title = row[1].lower()
            if "security" in title or "guard" in title or "guards" in title:
                security_jobs.append(row)
        if security_jobs:
            await query.message.reply_text("Security Jobs Found:")
            context.user_data["gigs"] = security_jobs
            context.user_data["page"] = 0
            await send_gigs_page(update, context)
        else:
            await query.message.reply_text("OOOPS!!!\nNo Jobs Related To Security Currently")
            await restart(update, context)
            
    elif query.data == "developer":
        developer_jobs = []
        for row in gigs:
            title = row[1].lower()
            if "developer" in title or " it " in title or "network" in title:
                developer_jobs.append(row)
        if developer_jobs:
            await query.message.reply_text("Developer Jobs Found:")
            context.user_data["gigs"] = developer_jobs
            context.user_data["page"] = 0
            await send_gigs_page(update, context)
            
        else:
            await query.message.reply_text("OOOPS!!!\nNo Jobs Related To Security Currently")
            await restart(update, context)
            
    elif query.data == "biz":
        biz_jobs = []
        for row in gigs:
                title = row[1].lower()
                if "accounting"in title or "marketing" in title or "sales" in title or "sale" in title or "business" in title or "hr" in title or "manager" in title:
                    biz_jobs.append(row)
        if biz_jobs:
            await query.message.reply_text("Business Related Jobs Found:")
            context.user_data["gigs"] = biz_jobs
            context.user_data["page"] = 0
            await send_gigs_page(update, context)
            
        else:
            await query.message.reply_text("OOOPS!!!\nNo Jobs Related To Business Currently")
            await restart(update, context)
            
    elif query.data == "engineer":
        engineer_jobs = []
        for row in gigs:
            title = row[1].lower()
            if "engineer" in title or "engineering" in title:
                engineer_jobs.append(row)
        if engineer_jobs:
            await query.message.reply_text("Engineering Related Jobs Found:")
            context.user_data["gigs"] = engineer_jobs
            context.user_data["page"] = 0
            await send_gigs_page(update, context)

        else:
            await query.message.reply_text("OOOPS!!!\nNo Jobs Related To Engineering Currently")
            await restart(update, context)
    
    elif query.data == "hospitality":
        hospitality_jobs = []
        for row in gigs:
            title = row[1].lower()
            if "cashier" in title or "tourism" in title or "chef" in title or "hospitality" in title or "cook" in title:
                hospitality_jobs.append(row)
        if hospitality_jobs:
            await query.message.reply_text("Hospitality $ Tourism Jobs Found:")
            context.user_data["gigs"] = hospitality_jobs
            context.user_data["page"] = 0
            await send_gigs_page(update, context)

        else:
            await query.message.reply_text("OOOPS!!!\nNo Jobs Related To Hospitality Currently")
            await restart(update, context)
    
    elif query.data == "medical":
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        medical_jobs = []
        for row in gigs:
            title = row[1].lower()
            if "medicine" in title or "medical" in title or "clinical" in title or "nurse" in title or "nursing" in title or "hospital" in title or "health" in title:
                medical_jobs.append(row)
        if medical_jobs:
            await query.message.reply_text("Medical Related Jobs Found:")
            context.user_data["gigs"] = medical_jobs
            context.user_data["page"] = 0
            await send_gigs_page(update, context)

        else:
            await query.message.reply_text("OOOPS!!!\nNo Jobs Related To Hospitality Currently")
            await restart(update, context)
    elif query.data == "bug":
        url = "https://wa.me/254797809846?text=Hello%20Globalgigs%20I%20found%20a%20Bug"
        keyboard = [[
            InlineKeyboardButton("Report Bug via WhatsApp", url=url)
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Click the button below to report a bug:", reply_markup=reply_markup)
    else:
        await query.edit_message_text("Wiriama never Created this button")

async def department(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Teaching", callback_data="teaching"),
            InlineKeyboardButton("Security", callback_data="security"),
            InlineKeyboardButton("Developer", callback_data="developer")
        ],
        [
            InlineKeyboardButton("Business Related", callback_data="biz"),
            InlineKeyboardButton("Engineering", callback_data="engineer"),
            InlineKeyboardButton("Hospitality", callback_data="hospitality")
        ],
        [
            InlineKeyboardButton("Medical Related", callback_data="medical"),
            InlineKeyboardButton("Search", callback_data="search")
        ],
        [
            InlineKeyboardButton("Report A Bug", callback_data="bug")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text("Choose Your option:", reply_markup=reply_markup)


def search(keyword):
    gigs = ask_database()
    found = []
    count = 0
    from spellchecker import SpellChecker
    spell = SpellChecker()
    misspelled = spell.unknown(keyword.split())
    if not misspelled:
        word = keyword
    else:
        corrected = ' '.join([spell.correction(word) for word in keyword.split()])
        word = corrected
    for row in gigs:
        title = row[1].lower()
        if word.lower() in title:
            found.append(row)
            count += 1
    return (count, word, found)


async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    get_user(update)

    if "hello" in user_message or "hey" in user_message:
        await update.message.reply_text("Hello, Can I Help You Find a gig?")
        await start(update, context)
    elif "gigs" in user_message or "jobs" in user_message:
        await update.message.reply_text("Here are latest gigs for you")
        for row in gigs:
            await update.message.reply_text(f"{row[1]}\n{row[3]}")
        await start(update, context)
        
    else:
        if context.user_data.get("awaiting_keyword"):
            keyword = update.message.text
            count, words, found = search(keyword)
            await update.message.reply_text(
                f"Your Search: *{words}* Got {count} jobs",
                parse_mode="Markdown"
            )
            context.user_data["gigs"] = found
            context.user_data["page"] = 0
            await send_gigs_page(update, context)
            context.user_data["awaiting_keyword"] = False
        else:
            await update.message.reply_text("Sorry, Ask for something relevant\nTry This")
        await start(update, context)

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))
bot_app.add_handler(CallbackQueryHandler(handle_callback))