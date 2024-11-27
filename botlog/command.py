import aiogram
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import message, InlineKeyboardMarkup, InlineKeyboardButton
from kbord import inlinekbord

rout = Router()

@rout.message(Command('start'))
async def start(message):
    await message.answer('Привет, я бот wish list, со мной ты можешь создать список своих хотелок и посмотреть что хотят другие люди, если ты напишешь свое желание то есть шанс что незнакомец его исполнит, так же и ты можешь исполнять чьи-то желания',
                         reply_markup=inlinekbord.openapp())
    
    