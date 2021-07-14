import asyncio
import argparse
from config import config
from chat import submit_message

# 5d457500-e4ca-11eb-8c47-0242ac110002
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Settings for send_message')
    parser.add_argument('--host', dest='host', help='Host to write', type=str, default=config['write_host'])
    parser.add_argument('--port', dest='port', help='Port to write', type=int, default=config['write_port'])
    parser.add_argument('--token', dest='token', help='User token', type=str, required=True)
    parser.add_argument('--message', dest='message', help='Message to send', type=str, required=True)
    args = parser.parse_args()
    asyncio.run(submit_message(args.host, args.port, args.token, args.message))
