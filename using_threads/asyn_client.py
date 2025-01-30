import asyncio

async def my_client(msg):
    reader, writer = await asyncio.open_connection('localhost', 8889)
    print('Client is sending a message')
    writer.write(msg.encode()) # every network transactin must be encoded
    writer.close()

if __name__ == '__main__':
    asyncio.run(my_client('lunchtime'))