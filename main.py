import random
import os
import time
import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.types.dice import DiceEmoji
from aiogram.filters import Command
from aiogram.types import Message, Sticker
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher() 

caslose = [7, 8, 10, 12, 14, 15, 19, 20, 25, 28, 29, 31, 34, 36, 37, 40, 45, 46, 50, 51, 53, 55, 57]
casduo = [2, 3, 4, 5, 6, 9, 11, 13, 16, 17, 18, 21, 23, 24, 26, 27, 30, 32, 33, 35, 38, 39, 41, 42, 44, 47, 48, 49, 52, 54, 56, 58, 59, 60, 61, 62, 63]
caswin = [1, 22, 43, 64]

@dp.message(Command('ustart'))
async def start(message: Message):
    await message.answer("Hello from UIlaI and UIlaIBot(0.5?)\nuse /uhelp for commands")
 
@dp.message(Command('uhelp'))
async def help(message: Message):
    await message.answer("используй / вместо ! \n!ustart\n!uhelp\n!777\n!footbik\n!basket\n!kosti\n!bigyaitsa\n!dart")
    

@dp.message(Command('777'))
async def slots(message: Message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEOF_hn1v7eMRPeKjHV3MEM24j6-MCHUwACZXMAAvjhsEpI0O_5SB1XnjYE', message_thread_id=message.message_thread_id)
    time.sleep(2.2)
    await bot.delete_message(message.chat.id, message.message_id+1)
    result: Message = await message.answer_dice(DiceEmoji.SLOT_MACHINE)
    # await message.answer(str(result.dice.value))
    if result.dice.value in caslose:
        time.sleep(1.5)
        await bot.send_message(message.chat.id, "lose", message_thread_id=message.message_thread_id)
        
    elif result.dice.value in casduo:
        time.sleep(1.5)
        await bot.send_message(message.chat.id, "duo", message_thread_id=message.message_thread_id)
        
    elif result.dice.value in caswin:
        time.sleep(1.5)
        await bot.send_message(message.chat.id, "win", message_thread_id=message.message_thread_id)
        

@dp.message(Command('footbik'))
async def football(message: Message):
    result: Message = await message.answer_dice(DiceEmoji.FOOTBALL)
    #await message.answer(str(result.dice.value))
    if result.dice.value in [3, 4, 5]:
        time.sleep(1.5)
        await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEOF_xn1v_gygl6Me6PlX-E0t-jIV2Q7gAC_2sAAqJDuEqO4dJb14g9izYE', message_thread_id=message.message_thread_id)
        


@dp.message(Command('basket'))
async def basketball(message: Message):
    result: Message = await message.answer_dice(DiceEmoji.BASKETBALL)
    #await message.answer(str(result.dice.value))
    

@dp.message(Command('kosti'))
async def dice(message: Message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEOGWBn1_5aZAy_HmP6nQye8fWFWZPy3QAClWsAAgJrwUoqfojSb1iAhDYE')
    time.sleep(2.2)
    await bot.delete_message(message.chat.id, message.message_id+1)
    result: Message = await message.answer_dice(DiceEmoji.DICE)
    #await message.answer(str(result.dice.value))
    
    

@dp.message(Command('bigyaitsa'))
async def bowling(message: Message):
    result: Message = await message.answer_dice(DiceEmoji.BOWLING)
    #await message.answer(str(result.dice.value))
    

@dp.message(Command('dart'))
async def dart(message: Message):
    result: Message = await message.answer_dice(DiceEmoji.DART)
    #await message.answer(str(result.dice.value))
    

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
        
        