import asyncio

async def schedule(delay, fn):
    """Implement a job scheduler which takes in a function f and an integer
    n, and calls f after n milliseconds"""
    await asyncio.sleep(delay)
    return fn()