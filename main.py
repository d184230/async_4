import asyncio


async def chat_reader(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    while True:
        message_bytes = await reader.readline()
        message = message_bytes.decode('utf8').strip()
        print(message)


asyncio.run(chat_reader('minechat.dvmn.org', 5000))
