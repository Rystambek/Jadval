from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,Dispatcher
from telegram import Update,Bot
from handler import (start,
                     menu
                     )
from flask import Flask, request
import os

# get token from environment variable
TOKEN = '6198972222:AAFMAYd6f3bJFSh-1FA6ZnqdZTtAIRhbjyE'

bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return 'OK'

