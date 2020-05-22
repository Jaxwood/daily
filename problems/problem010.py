import asyncio

async def schedule(delay, fn):
    """text"""
    await asyncio.sleep(delay)
    return fn()