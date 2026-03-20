import os

class IdentitySpoofer:
    async def execute_spoof(self, page, name, img_path):
        if not os.path.exists(img_path): return
        await page.goto("https://www.facebook.com/me")
        try:
            await page.click("//div[@aria-label='Edit profile' or @aria-label='تعديل الملف الشخصي']", timeout=5000)
            await page.set_input_files("//input[@type='file']", img_path)
            await page.click("text='Save' or text='حفظ'")
        except: pass
          
