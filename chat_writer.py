import asyncio


async def chat_writer(host, port, token, message):
    reader, writer = await asyncio.open_connection(host, port)
    writer.write(f'{token}\n'.encode())
    writer.write(f'{message}\n\n'.encode())


if __name__ == '__main__':
    asyncio.run(chat_writer('minechat.dvmn.org', 5050, 'ad053564-e414-11eb-8c47-0242ac110002', 'HELLO 2'))
