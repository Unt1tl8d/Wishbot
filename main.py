import asyncio
from data import config
from aiogram import Bot, Dispatcher
from botlog import command


async def main():
    bot = Bot(config.token)
    dp = Dispatcher()
    dp.include_router(
        command.rout,
    )    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())