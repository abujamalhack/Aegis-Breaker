from playwright.async_api import async_playwright
import asyncio

async def extract():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.facebook.com/login")
        print("[!] Please login manually. Press Enter in this terminal once done...")
        input()
        await context.storage_state(path="data/sessions/manual_bot.json")
        print("[+] Session saved to data/sessions/manual_bot.json")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(extract())
  
