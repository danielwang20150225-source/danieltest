import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://localhost:9224')
        
        contexts = browser.contexts
        if contexts and contexts[0].pages:
            page = contexts[0].pages[0]
        else:
            return
        
        # Wait a bit more for full response
        print('Waiting more for full response...')
        await asyncio.sleep(15)
        
        await page.screenshot(path='doubao_full.png', full_page=True)
        print('Full response screenshot saved')
        
        # Try to get all visible text
        body_text = await page.evaluate('''() => {
            const elements = document.querySelectorAll('[class*="content"], [class*="message"]');
            let text = '';
            elements.forEach(el => {
                if (el.offsetParent !== null) { // visible
                    text += el.innerText + '\n---\n';
                }
            });
            return text.slice(0, 3000);
        }''')
        print('Extracted text:')
        print(body_text)
        
        await browser.close()

asyncio.run(main())