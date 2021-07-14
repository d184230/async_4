# Скрипты для подключения к подпольному чату

## Как установить
Для работы микросервиса нужен Python версии не ниже 3.6.

```
pip install -r requirements.txt
```

## Скрипт чтения чата
Скрипт подключается к подпольному чату и выводит все содержимое в stdout.
Также есть возможность записывать содержимое чата в файл.

Запуск скрипта:
```
python read_chat.py
```
Параметры скрипта:
```
--host указание хоста подпольного чата, по умолчанию minechat.dvmn.org
--host указание порта подпольного чата, по умолчанию 5000
--history указание пути до файла, куда будет записываться история сообщений
```

## Скрипт регистрации пользователя
Скрипт подключается к подпольному чату и регистрирует пользователя

Запуск скрипта:
```
python register.py --username testuser
```
Параметры скрипта:
```
--host указание хоста подпольного чата, по умолчанию minechat.dvmn.org
--host указание порта подпольного чата, по умолчанию 5050
--username имя пользователя, обязательное поле
```

## Скрипт отправки сообщения в подпольный чат
Скрипт подключается к подпольному чату и отправляет сообщение

Запуск скрипта:
```
python send_message.py --token testtoken --message hello
```
Параметры скрипта:
```
--host указание хоста подпольного чата, по умолчанию minechat.dvmn.org
--host указание порта подпольного чата, по умолчанию 5050
--token токен пользователя, обязательное поле
--message сообщение, обязательное поле
```
