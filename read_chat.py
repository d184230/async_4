import asyncio
import argparse
from config import config
from chat import chat_reader


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Settings for char_reader')
    parser.add_argument('--host', dest='host', help='Host to read', type=str, default=config['read_host'])
    parser.add_argument('--port', dest='port', help='Port to read', type=int, default=config['read_port'])
    parser.add_argument('--history', dest='history', help='Path to file, with save history', type=str, default=config['file_to_log_chat'])
    args = parser.parse_args()
    asyncio.run(chat_reader(args.host, args.port, args.history))
