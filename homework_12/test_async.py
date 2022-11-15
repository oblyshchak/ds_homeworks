import asyncio

async def greeting():
    print("Hello from greeting!")
    await asyncio.sleep(2)
    print("After SLEEP")
    
async def new(name):
    print(f"{name}, hello. Its second function!")
    await asyncio.sleep(5)
    print(f"AFTER SlEEP second function")
    
asyncio.run(greeting())
asyncio.run(new('sanichka'))