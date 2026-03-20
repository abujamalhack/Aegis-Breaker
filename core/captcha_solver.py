import aiohttp
import asyncio

class CaptchaSolver:
    def __init__(self, key): self.key = key
    async def solve(self, site_key, url):
        async with aiohttp.ClientSession() as s:
            params = {'key': self.key, 'method': 'userrecaptcha', 'googlekey': site_key, 'pageurl': url, 'json': 1}
            async with s.post("http://2captcha.com/in.php", data=params) as r:
                res = await r.json()
                if res['status'] != 1: return None
                rid = res['request']
            for _ in range(20):
                await asyncio.sleep(5)
                async with s.get(f"http://2captcha.com/res.php?key={self.key}&action=get&id={rid}&json=1") as r:
                    res = await r.json()
                    if res['status'] == 1: return res['request']
        return None
      
