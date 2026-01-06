import asyncio

async def brew_chai():
    print("brewing chai....")
    await asyncio.sleep(2)
    print("Chai is ready")

asyncio.run(brew_chai())