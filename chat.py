import asyncio
import aiofiles
from datetime import datetime

import requests.exceptions


async def read_message_from_reader(reader):
    """Чтение сообщения из объекта StreamReader.

    Чтение одного сообщения из объекта StreamReader
    :param reader: StreamReader: Объект из которого происходит чтение
    :return: str: Сообщение из чата
    """
    message_bytes = await reader.readline()
    message = message_bytes.decode('utf8').strip()
    return message


async def write_message_to_writer(writer, message):
    """Отправка сообщения через объект StreamWriter.

    Отправка сообщения через объект StreamWriter.
    :param writer: str: Текст сообщения
    :param message: StreamWriter: Объект через который происходит отправка
    :return: None
    """
    message_clear = message.replace('\n', '')
    writer.write(f'{message_clear}\n\n'.encode())
    await writer.drain()


async def register(host, port, user_name, file_to_save=None):
    """Регистрация пользователя.

    Функция для регистрации пользователя с возможностью записи регистрационных данных в файл
    :param host: str: host сервера для регистрации
    :param port: int: порт сервера для регистрации
    :param user_name: str: имя пользователя
    :param file_to_save: str: optional: Путь к файлу для сохранения регистрациооных данных (опционально)
    :return: None
    """
    reader, writer = await asyncio.open_connection(host, port)
    try:
        await read_message_from_reader(reader)
        await write_message_to_writer(writer, '')
        await read_message_from_reader(reader)
        await write_message_to_writer(writer, user_name)
        data_registration_user = await read_message_from_reader(reader)
        print(data_registration_user)
        if file_to_save:
            async with aiofiles.open(file_to_save, mode='w', encoding='utf8') as f:
                await f.write(f'{data_registration_user}\n')
    finally:
        writer.close()


async def send_message_to_server(host, port, token, message):
    """Отправка сообщения.

    Отправка сообщения в указанный сервер. Необходим токен авторизации.
    :param host: str: host сервера для отправки
    :param port: int: порт сервера для отправки
    :param token: str: токен авторизации пользователя
    :param message: str: сообщение
    :return: None
    """
    reader, writer = await asyncio.open_connection(host, port)
    try:
        await write_message_to_writer(writer, token)
        message_token_confirm = await read_message_from_reader(reader)
        if message_token_confirm == 'null':
            print('Неизвестный токен. Проверьте его или зарегистрируйте заново.')
        else:
            await write_message_to_writer(writer, message)
    finally:
        writer.close()


async def read_chat_from_server(host, port, path_to_file_history=None):
    """Чтение чата из указанного сервера.

    Подключение к серверу, чтение переписки и вывод переписки в stdout. Опционально можно сохранять всю историю чата в файл.
    :param host: str: host сервера для чтения
    :param port: int: порт сервера для чтения
    :param path_to_file_history: str: optional: Путь к файлу для сохранения истории чата (опционально)
    :return: None
    """
    reader, writer = await asyncio.open_connection(host, port)
    try:
        while True:
            try:
                message_bytes = await reader.readline()
                message = message_bytes.decode('utf8').strip()
                message_datetime = datetime.now()
                message_with_datetime = f'[{message_datetime.strftime("%d.%m.%Y %H:%M")}] {message}'
                print(message_with_datetime)
                if path_to_file_history:
                    async with aiofiles.open(path_to_file_history, mode='a', encoding='utf8') as f:
                        await f.write(f'{message_with_datetime}\n')
            except requests.exceptions.ConnectionError:
                reader, writer = await asyncio.open_connection(host, port)
    finally:
        writer.close()
