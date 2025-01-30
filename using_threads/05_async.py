import asyncio # NB recent Python only

# we must use async and await together
async def m():
    # await asyncio.sleep(1) # each time this function is invoked, the main thread will wait for this thread to end
    asyncio.sleep(1) # in this case the co-routine does NOT cause the main thread to wait
    print('thread is done')

if __name__ == '__main__':
    # we use asyncio.run() to ask python ton a finction in a thread
    with asyncio.Runner() as runner: # here we instantiate the Runner class
        runner.run(m())
        runner.run(m())
        runner.run(m())
        runner.run(m())
        runner.run(m())
        runner.run(m())
        runner.run(m())
        runner.run(m())
        runner.run(m())

    # or
    run2 = asyncio.Runner()
    run2.run(m())