from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from handler import start,menu


TOKEN='6162217632:AAEnncQeDNHOnSCAlMw0PTxbkJpAQQdL2X4'


updater = Updater(token=TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
# dp.add_handler(MessageHandler(Filters.text, text))
dp.add_handler(CallbackQueryHandler(menu))

if __name__ == "__main__":
    updater.start_polling()
    updater.idle()