import asyncio
import yaml
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

async def test_selectors():
    # 1. تحميل المحددات من الملف الخارجي
    try:
        with open("selectors.yaml", "r", encoding="utf-8") as f:
            sel_config = yaml.safe_load(f)['facebook_v2026']
    except Exception as e:
        print(f"[-] Error loading selectors.yaml: {e}")
        return

    target_url = "https://www.facebook.com/zuck" # مثال للحساب المستهدف للاختبار
    session_path = "data/sessions/test_bot.json" # يجب أن يكون لديك جلسة صالحة هنا

    print("[*] Starting Selector Validation Mission...")

    async with async_playwright() as p:
        # تشغيل المتصفح بوضع مرئي (Headless=False) لمراقبة الاختبار
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(storage_state=session_path)
        await stealth_async(context)
        page = await context.new_page()

        try:
            print(f"[*] Navigating to target: {target_url}")
            await page.goto(target_url, wait_until="networkidle")
            
            # اختبار محدد المنشورات (Post Container)
            posts = page.locator(sel_config['post_container'])
            count = await posts.count()
            print(f"[+] Found {count} posts using primary selector.")

            if count > 0:
                # اختبار الزر "المزيد" (More Button) مع الـ Fallbacks
                print("[*] Testing 'More' button fallbacks...")
                found_more = False
                for i, selector in enumerate(sel_config['more_button']):
                    try:
                        btn = page.locator(selector).first
                        if await btn.is_visible(timeout=3000):
                            print(f"  [!] Success: Selector Level {i+1} is WORKING: {selector}")
                            found_more = True
                            # محاكاة الضغط لفتح القائمة واختبار خيار الإبلاغ
                            await btn.click()
                            await asyncio.sleep(2)
                            break
                    except:
                        print(f"  [-] Failed: Selector Level {i+1} is broken.")

                if found_more:
                    # اختبار خيارات الإبلاغ (Report Options)
                    print("[*] Testing 'Report' link fallbacks...")
                    for i, selector in enumerate(sel_config['report_link']):
                        try:
                            report_btn = page.locator(selector).first
                            if await report_btn.is_visible(timeout=3000):
                                print(f"  [!] Success: Report Link Level {i+1} is WORKING.")
                                break
                        except:
                            continue

            print("\n[V] Validation Complete. Check the logs above for broken selectors.")
        
        except Exception as e:
            print(f"[-] Critical Test Error: {e}")
        finally:
            await asyncio.sleep(5) # وقت للمعاينة البصرية قبل الإغلاق
            await browser.close()

if __name__ == "__main__":
    asyncio.run(test_selectors())
              
