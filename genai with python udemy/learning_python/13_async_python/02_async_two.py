import asyncio
import time

async def brew(name):
    print(f"Brewing {name} chai....")
    # await asyncio.sleep(3)
    time.sleep(3)
    print(f"{name} chai is ready....")

async def main():
    await asyncio.gather(
        brew("masala"),
        brew("elaichi"),
        brew("ginger")
    )

asyncio.run(main())