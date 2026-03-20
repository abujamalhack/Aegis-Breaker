import aiohttp
import asyncio

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies
        self.valid = []

    async def validate_pool(self):
        async with aiohttp.ClientSession() as s:
            tasks = [self._check(s, p) for p in self.proxies]
            await asyncio.gather(*tasks)
        return self.valid

    async def _check(self, s, p):
        try:
            async with s.get("https://m.facebook.com", proxy=p, timeout=5) as r:
                if r.status == 200: self.valid.append(p)
        except: pass
          
