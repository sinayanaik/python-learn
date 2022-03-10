import asyncio                #asyncio module : asyncio is a library to write concurrent code using the async/await syntax.
import time

async def say_after(delay, what):               # async def : async function
    await asyncio.sleep(delay)                  # await : wait for the result of an asynchronous operation
    print(what)                                 # print : print the result of an asynchronous operation 

async def main():                                      # async def : async function
    print(f"started at {time.strftime('%X')}")         # print : print the result of an asynchronous operation

    await say_after(1, 'hello')                        # await : wait for the result of an asynchronous operation
    await say_after(2, 'world')                        # await : wait for the result of an asynchronous operation

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())                              # asyncio.run : run the main function