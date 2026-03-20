import asyncio
import yaml
import json
import os
from core.browser_pool import BrowserPool
from core.ai_engine import DualAIEngine
from core.content_fetcher import ContentFetcher
from core.logger import log

async def main():
    with open("config.yaml", "r") as f: config = yaml.safe_load(f)
    with open("data/bots.json", "r") as f: bots = json.load(f)
    
    node_id = int(os.getenv("NODE_ID", 0))
    replicas = int(os.getenv("REPLICAS", 1))
    # تقسيم البوتات على الحاويات لضمان عدم التكرار
    my_bots = bots[node_id::replicas]

    log.info(f"--- Aegis-Breaker 2099: Node {node_id} Initiated ---")

    pool = BrowserPool(config)
    ai = DualAIEngine()
    fetcher = ContentFetcher()
    target = config['target_info']['id']
    
    tasks = [pool.execute_task(bot, target, ai, fetcher) for bot in my_bots]
    await asyncio.gather(*tasks)
    
    log.info(f"--- Node {node_id}: All Operations Completed ---")

if __name__ == "__main__":
    asyncio.run(main())
  
