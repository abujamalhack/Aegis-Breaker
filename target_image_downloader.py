import asyncio
import os
import aiohttp
import yaml
from playwright.async_api import async_playwright
from core.logger import log

async def download_target_assets(target_id, session_path):
    # التأكد من وجود المجلد
    if not os.path.exists("data/targets"):
        os.makedirs("data/targets")

    log.info(f"[*] Starting asset extraction for target: {target_id}")

    async with async_playwright() as p:
        # تشغيل المتصفح (يفضل وضع مرئي للتأكد من تجاوز أي حاجز مبدئي)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=session_path)
        page = await context.new_page()

        try:
            await page.goto(f"https://www.facebook.com/{target_id}", wait_until="networkidle")
            
            # محدد صورة البروفايل لعام 2026 (يعتمد على الدور التشريحي للصورة في الصفحة)
            profile_img_selector = "//div[@aria-label='Profile picture' or @aria-label='صورة الملف الشخصي']//img"
            
            await page.wait_for_selector(profile_img_selector, timeout=10000)
            img_url = await page.get_attribute(profile_img_selector, "src")

            if img_url:
                async with aiohttp.ClientSession() as session:
                    async with session.get(img_url) as resp:
                        if resp.status == 200:
                            content = await resp.read()
                            file_path = f"data/targets/{target_id}.jpg"
                            with open(file_path, "wb") as f:
                                f.write(content)
                            log.info(f"[+] Success: Target image saved to {file_path}")
                        else:
                            log.error(f"[-] Failed to download image. Status: {resp.status}")
            else:
                log.error("[-] Profile image URL not found.")

        except Exception as e:
            log.error(f"[-] Error during extraction: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    # مثال للتشغيل الفردي قبل الهجوم
    with open("config.yaml", "r") as f:
        cfg = yaml.safe_load(f)
    # يستخدم أول جلسة متاحة للقيام بعملية الاستطلاع
    asyncio.run(download_target_assets(cfg['target_info']['id'], "data/sessions/bot_example.json"))
  
