import asyncio
import argparse
from config import config
from chat import register


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Settings for send_message')
    parser.add_argument('--host', dest='host', help='Host to register', type=str, default=config['default_write_host'])
    parser.add_argument('--port', dest='port', help='Port to register', type=int, default=config['default_write_port'])
    parser.add_argument('--username', dest='user_name', help='User name', type=str, required=True)
    args = parser.parse_args()
    asyncio.run(register(args.host, args.port, args.user_name))
