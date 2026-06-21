import asyncio
import aiohttp

# Async API call
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",   # Dummy post
        "https://jsonplaceholder.typicode.com/users/1",   # Dummy user
        "https://jsonplaceholder.typicode.com/todos/1"    # Dummy todo
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        post, user, todo = results
        print("Post:", post)
        print("User:", user)
        print("Todo:", todo)

asyncio.run(main())
