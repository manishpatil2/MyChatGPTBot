import openai
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load API keys
TELEGRAM_BOT_TOKEN = os.getenv("7587526157:AAH74xksIwNH4guIbf10_2q2U9ybZM2Ae0g")
OPENAI_API_KEY = os.getenv("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")

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Initialize bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# Function to generate ChatGPT response
async def chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Handle messages
@dp.message_handler()
async def handle_message(message: Message):
    user_input = message.text
    response = await chatgpt_response(user_input)
    await message.reply(response)

# Start bot
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
