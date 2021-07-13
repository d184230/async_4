import asyncio
import aiofiles
import argparse
from datetime import datetime


async def chat_reader(host, port, path_to_file_history):
    reader, writer = await asyncio.open_connection(host, port)
    while True:
        message_bytes = await reader.readline()
        message = message_bytes.decode('utf8').strip()
        message_datetime = datetime.now()
        message_with_datetime = f'[{message_datetime.strftime("%d.%m.%Y %H:%M")}] {message}'
        print(message_with_datetime)
        async with aiofiles.open(path_to_file_history, mode='a', encoding='utf8') as f:
            await f.write(f'{message_with_datetime}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Settings for char_reader')
    parser.add_argument('--host', dest='host', help='Host to read', type=str, default='minechat.dvmn.org')
    parser.add_argument('--port', dest='port', help='Port to read', type=int, default=5000)
    parser.add_argument('--history', dest='history', help='Path to file, with save history', type=str, default='chat_log.history')
    args = parser.parse_args()
    asyncio.run(chat_reader(args.host, args.port, args.history))
