import asyncio
import yaml
import random
from core.spoofing import IdentitySpoofer
from core.logger import log

class ExecutionCore:
    def __init__(self, config, context):
        self.config = config
        self.context = context
        with open("selectors.yaml", "r") as f:
            self.sel = yaml.safe_load(f)['facebook_v2026']

    async def run(self, bot, target, ai, fetcher):
        page = await self.context.new_page()
        try:
            # 1. Spoofing
            spoofer = IdentitySpoofer()
            await spoofer.execute_spoof(page, target, f"data/targets/{target}.jpg")
            
            # 2. AI Analysis
            content = await fetcher.fetch_full(page, target)
            category = await ai.analyze(content)
            
            # 3. Report Click Sequence
            for key in ["more_button", "report_link"]:
                for s in self.sel[key]:
                    try:
                        await page.click(s, timeout=5000)
                        break
                    except: continue
            
            # 4. Finalize
            await page.click(f"text='{category}'")
            await page.click(self.sel['submit_button'][0])
            log.info(f"Bot {bot['id']} Reported {target} as {category}")
        except Exception as e: log.error(f"Execution Error: {e}")
        finally: await page.close()
          
