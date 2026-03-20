import aiohttp

class ContentFetcher:
    async def fetch_full(self, page, target):
        await page.goto(f"https://www.facebook.com/{target}", wait_until="networkidle")
        posts = await page.locator("//div[@role='article']").all()
        results = []
        async with aiohttp.ClientSession() as s:
            for p in posts[:15]:
                text = await p.inner_text()
                imgs = [await i.get_attribute("src") for i in await p.locator("img").all() if "scontent" in (await i.get_attribute("src") or "")]
                img_files = []
                for url in imgs:
                    async with s.get(url) as r:
                        if r.status == 200: img_files.append(await r.read())
                results.append({"text": text, "img_files": img_files})
        return results
      
