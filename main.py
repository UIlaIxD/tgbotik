import random
import logging
import json
import os
import time
import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.types.dice import DiceEmoji
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, Sticker
from dotenv import load_dotenv

global randvalue
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher() 


caslose = [7, 8, 10, 12, 14, 15, 19, 20, 25, 28, 29, 31, 34, 36, 37, 40, 45, 46, 50, 51, 53, 55, 57, 58]
casduo = [2, 3, 4, 5, 6, 9, 11, 13, 16, 17, 18, 21, 23, 24, 26, 27, 30, 32, 33, 35, 38, 39, 41, 42, 44, 47, 48, 49, 52, 54, 56, 59, 60, 61, 62, 63]
caswin = [1, 22, 43, 64]

anekdots = []

def rand():
    global randvalue
    randvalue = random.randint(1, 2)

@dp.message(Command('ustart'))
async def start(message: Message):
    await message.answer("Хеллоу от UIlaIBot(0.6.0?) и UIlaI\nпиши /uhelp для всех комманд")
 
 
@dp.message(Command('uhelp'))
async def help(message: Message):
    await message.answer("используй / вместо ! \n!ustart\n!uhelp\n!777\n!footbik\n!basket\n!kosti\n!bigyaitsa\n!dart")

with open("anekdotlist.json", "w") as file:
    json.dump([90, 91], file)

@dp.message(F.text.lower() == "id")
async def showid(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    if message.reply_to_message != None:
        print(message.reply_to_message.message_id)


@dp.message(F.text.lower() == "p")
async def poslat(message: Message):
    m = message.reply_to_message.message_id
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.chat.id, "динаху", reply_to_message_id=m)

@dp.message(Command('s'))
async def echo(message: Message, command: CommandObject):
    saying = command.args
    await bot.delete_message(message.chat.id, message.message_id)
    if message.from_user.id == 1307118150:
        if message.reply_to_message != None:
            m = message.reply_to_message.message_id
            await bot.send_message(message.chat.id, saying, reply_to_message_id=m)
        else:
            await bot.send_message(message.chat.id, saying)
    else:
        await message.answer("ю донт хэв права")
    #print(message.from_user.id)


#@dp.message(F.text.lower() == "дроч")
#async def droch(message: Message):
    #if message.reply_to_message.from_user.id == 1307118150:
    #    pass
    #else:
    #    pass


@dp.message(Command('anekdot', 'анекдот'))
async def Funcanekdot(message: Message):
    joke = await bot.copy_message(message.chat.id, message_id=random.choice(), message_thread_id=message.message_thread_id)
    print(joke)


@dp.message(Command('777'))
async def slots(message: Message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEOF_hn1v7eMRPeKjHV3MEM24j6-MCHUwACZXMAAvjhsEpI0O_5SB1XnjYE', message_thread_id=message.message_thread_id)
    time.sleep(2.2)
    await bot.delete_message(message.chat.id, message.message_id+1)
    result: Message = await message.answer_dice(DiceEmoji.SLOT_MACHINE)
    # await message.answer(str(result.dice.value))
    if result.dice.value in caslose:
        time.sleep(3.5)
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOGAABZ9cAAU4tOhA_xWh5K3AftQ1k06vcAAL-LAACfVu4S1e6n5Rzp8WKNgQ", message_thread_id=message.message_thread_id)
        
    elif result.dice.value in casduo:
        time.sleep(3.5)
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOGbRn2A7bnccY55FdXBpi4wK0tTfKpgACLGgAAgd5wUpCOiZZ-eYknjYE", message_thread_id=message.message_thread_id)
        
    elif result.dice.value in caswin:
        time.sleep(3.5)
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOH1Rn26b6EHUUBCmDPS_m93qgRp8txQACa3AAAnvJ2Ur1BH4FE_wL1zYE", message_thread_id=message.message_thread_id)
        

@dp.message(Command('footbik'))
async def football(message: Message):
    result: Message = await message.answer_dice(DiceEmoji.FOOTBALL)
    #await message.answer(str(result.dice.value))
    if result.dice.value in [3, 4, 5]:
        time.sleep(3.2)
        await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEOF_xn1v_gygl6Me6PlX-E0t-jIV2Q7gAC_2sAAqJDuEqO4dJb14g9izYE', message_thread_id=message.message_thread_id)
        


@dp.message(Command('basket'))
async def basketball(message: Message):
    result: Message = await message.answer_dice(DiceEmoji.BASKETBALL)
    if result.dice.value in [4, 5]:
        rand()
        if randvalue == 1:
            time.sleep(3.7)
            await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOF_5n1v_9lq6aa3E3EsvwHo-bMllVwQAC2mUAAjLHuUh_X0a94GwmTDYE", message_thread_id=message.message_thread_id)
        elif randvalue == 2:
            time.sleep(3.7)
            await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOGWVn2AHOHQOmW2y9_Cexb06mgzKZqwAClW0AAuZOwEpGLpiQKo7usDYE", message_thread_id=message.message_thread_id)
    if result.dice.value == 3:
            time.sleep(3.7)
            await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOH2Fn27VRl1IUaQ-ClpnXMxwH4TCq-gACVhMAAiY0qEl6mTdDjkmdUzYE", message_thread_id=message.message_thread_id)
    #await message.answer(str(result.dice.value))
    if result.dice.value in [1, 2]:
        time.sleep(3.7)
        await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOIM1n3PakyNYKgBShAf6IAXVMwBOzewACoQoAAkPzkEsBtfl0U9zjOjYE", message_thread_id=message.message_thread_id)

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
    await message.answer(str(result.dice.value))
    



async def main():
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
        
        