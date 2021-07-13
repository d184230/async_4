import asyncio
import aiofiles
from datetime import datetime


async def chat_reader(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    while True:
        message_bytes = await reader.readline()
        message = message_bytes.decode('utf8').strip()
        message_datetime = datetime.now()
        message_with_datetime = f'[{message_datetime.strftime("%d.%m.%Y %H:%M")}] {message}'
        print(message_with_datetime)
        async with aiofiles.open('chat_log.txt', mode='a', encoding='utf8') as f:
            await f.write(f'{message_with_datetime}\n')


asyncio.run(chat_reader('minechat.dvmn.org', 5000))
