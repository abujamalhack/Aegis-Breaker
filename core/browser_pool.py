from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import asyncio
from core.execution import ExecutionCore

class BrowserPool:
    def __init__(self, config):
        self.config = config
        self.semaphore = asyncio.Semaphore(config['system_settings']['max_browsers'])
        self.playwright = None

    async def execute_task(self, bot, target, ai, fetcher):
        async with self.semaphore:
            if not self.playwright: self.playwright = await async_playwright().start()
            browser = await self.playwright.chromium.launch(headless=self.config['system_settings']['headless'], proxy={"server": bot['proxy']})
            context = await browser.new_context(storage_state=bot['cookie_path'], user_agent=bot['ua'])
            await stealth_async(context)
            
            executor = ExecutionCore(self.config, context)
            await executor.run(bot, target, ai, fetcher)
            await browser.close()
          
