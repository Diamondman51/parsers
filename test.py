import asyncio
import time
from currency_parser.main2 import get_currencies


# st = '/tinkoff-to-bitcoin.html'

# print(st.strip('/html.'))

url = 'https://www.bestchange.app/v2'

dir = 'main2'

l = [1, 2]
k, m = l
print(k, m)

async def main():
    cur = await get_currencies(dir, url)
    # print(cur)

start = time.time()
asyncio.run(main())
end = time.time()
print(end - start)
