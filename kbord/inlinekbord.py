from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from data import config


def openapp():
    markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= 'Открыть wish list', web_app=WebAppInfo(url=config.webapp))]])
    return markup