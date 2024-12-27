import asyncio
import json
import time
import aiofiles
from bs4 import BeautifulSoup
import aiohttp

async def get_sport_href(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.text()
        
    soup = BeautifulSoup(response, 'html.parser')
    soup = soup.prettify()
    # with open("test.html", "w", encoding="utf-8") as f:
    #     f.write(soup)
    # print(soup)
    response = BeautifulSoup(response, 'html.parser')
    res = response.find_all('ul')
    res: BeautifulSoup = res[2]
    # print(res.prettify())
    # print(res)
    sport_href = []
    for i in res:
        tag = i.find('a')
        sport_href.append([i.text, tag['href']])
        # print(i.text, tag['href'])
    with open("sport_href.json", "w", encoding="utf-8") as f:
        json.dump(dict(sport_href), f, indent=4, ensure_ascii=False)


async def get_sport_html(name, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            res = await response.text()
            soup = BeautifulSoup(res, 'html.parser')
            soup = soup.prettify()
            with open(f"{name}.html", "w", encoding='utf-8') as f:
                f.write(soup)
            # print(soup, '\n\n')


async def main():
    # await get_sport_href("https://betboom.ru/sport")
    with open('sport_href.json', 'r', encoding="utf-8") as f:
        data: dict = json.load(f)
    tasks = [get_sport_html(name, url) for name, url in data.items()]
    # Run all tasks concurrently
    await asyncio.gather(*tasks)



# asyncio.run(main())

import requests

res = requests.get("https://betboom.ru/sport/snooker/48/8038/1167024")
res = BeautifulSoup(res.text, 'html.parser')
print(res.prettify())

