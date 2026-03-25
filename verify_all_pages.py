import os
import time
from playwright.sync_api import sync_playwright

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        cwd = os.getcwd()
        pages = {
            "home": f"file://{cwd}/index.html",
            "marketplace": f"file://{cwd}/marketplace.html",
            "about": f"file://{cwd}/about.html",
            "connect": f"file://{cwd}/connect.html",
            "report": f"file://{cwd}/report.html",
        }

        os.makedirs("verification", exist_ok=True)

        for name, url in pages.items():
            print(f"Capturing {name}...")
            page.goto(url)
            time.sleep(1)
            page.screenshot(path=f"verification/{name}.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    capture_screenshots()
