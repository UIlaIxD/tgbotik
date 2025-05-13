import logging
logging.basicConfig(format='[%(levelname) %(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon import TelegramClient, events
from bdconfig import api_id, api_hash
import time


client = TelegramClient('pars', api_id, api_hash)
chat = -1002455226402


async def main():
    async for message in client.iter_messages(chat):
        print(message.id, ':', message.text)


with client:
    client.loop.run_until_complete(main())





