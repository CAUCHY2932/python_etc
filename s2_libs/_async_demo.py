# coding: utf-8
import asyncio


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


def run_async_tasks():
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(hello())
    loop.close()


async def hello2(first_print, second_print):
    print(first_print)
    await asyncio.sleep(1)
    print(second_print)


asyncio.run(hello2("welcome", "Good-bye"))
