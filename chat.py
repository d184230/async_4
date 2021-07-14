import asyncio
import aiofiles
from datetime import datetime


async def read_message(reader):
    """Чтение сообщения из чата"""
    message_bytes = await reader.readline()
    message = message_bytes.decode('utf8').strip()
    return message


def write_message(writer, message):
    """Отправка сообщения в чат"""
    message_clear = message.replace('\n', '')
    writer.write(f'{message_clear}\n\n'.encode())


async def register(host, port, user_name, file_to_save=None):
    """Регистрация пользователя"""
    reader, writer = await asyncio.open_connection(host, port)
    await read_message(reader)
    write_message(writer, '')
    await read_message(reader)
    write_message(writer, user_name)
    data_registration_user = await read_message(reader)
    print(data_registration_user)
    if file_to_save:
        async with aiofiles.open(file_to_save, mode='w', encoding='utf8') as f:
            await f.write(f'{data_registration_user}\n')


async def submit_message(host, port, token, message):
    """Отправка сообщения"""
    reader, writer = await asyncio.open_connection(host, port)
    write_message(writer, token)
    message_token_confirm = await read_message(reader)
    if message_token_confirm == 'null':
        print('Неизвестный токен. Проверьте его или зарегистрируйте заново.')
    else:
        write_message(writer, message)


async def chat_reader(host, port, path_to_file_history=None):
    reader, writer = await asyncio.open_connection(host, port)
    while True:
        message_bytes = await reader.readline()
        message = message_bytes.decode('utf8').strip()
        message_datetime = datetime.now()
        message_with_datetime = f'[{message_datetime.strftime("%d.%m.%Y %H:%M")}] {message}'
        print(message_with_datetime)
        if path_to_file_history:
            async with aiofiles.open(path_to_file_history, mode='a', encoding='utf8') as f:
                await f.write(f'{message_with_datetime}\n')
