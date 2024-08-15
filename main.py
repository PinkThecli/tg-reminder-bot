from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ContentType
from aiogram.filters import CommandStart
from aiogram.types import Message

import rutimeparser as rtp  # type: ignore
from scheduler.asyncio import Scheduler

import asyncio
from datetime import datetime
import os
import sys
import logging


async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    api_token = os.getenv("API_TOKEN")
    if api_token is None:
        logging.error("Environment variable API_TOKEN is not set")
        exit(-1)

    sch = Scheduler()
    dp = Dispatcher()
    bot = Bot(
        token=api_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        await message.answer("Hi! I am Freyja!")

    @dp.message()
    async def message_handler(message: Message) -> None:
        if message.content_type != ContentType.TEXT or not message.text:
            return

        dt: datetime = rtp.parse(message.text)

        if not dt:
            return

        msg = f"You asked to be reminded on {dt.strftime('%x')} at {dt.strftime('%X')} about:\n\"{message.text}\""
        sch.once(dt, remind, args=(message, msg))

        await message.answer(f"Sure, I will remind you about it on {dt.strftime('%x')} at {dt.strftime('%X')}")

    async def remind(message: Message, msg: str) -> None:
        await message.answer(msg)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
