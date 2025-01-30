import asyncio

async def handle_requests(reader, writer):
    data = await reader.read(1024)
    msg = data.decode()
    addr = writer.get_extra_info('peerame')
    print(f'Server received {msg} from {addr}')
    writer.close() # good practice

async def main():
    server = await asyncio.start_server(handle_requests, 'localhost', 8889)
    print('server started')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run( main() )