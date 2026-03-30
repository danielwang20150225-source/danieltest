import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=['--no-sandbox'])
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = await context.new_page()
        
        print('Opening Kimi...')
        await page.goto('https://kimi.moonshot.cn', timeout=60000, wait_until='domcontentloaded')
        await asyncio.sleep(3)
        
        title = await page.title()
        print(f'Page title: {title}')
        
        # Based on the screenshot, the input has placeholder "尽管问..."
        # Let's try different selectors
        selectors = [
            'textarea[placeholder*="问"]',
            'textarea[placeholder*="..."]',
            '.chat-input textarea',
            'div[contenteditable="true"]',
            '[placeholder*="尽管"]',
            '.input-area textarea',
            '.message-input',
            'div[role="textbox"]',
            '.kimi-input',
            '.prompt-input'
        ]
        
        print('\nTrying selectors:')
        for sel in selectors:
            try:
                el = await page.query_selector(sel)
                if el:
                    visible = await el.is_visible() if el else False
                    placeholder = await el.get_attribute('placeholder') if el else None
                    tag = await el.evaluate('e => e.tagName') if el else None
                    print(f'  FOUND: {sel} -> tag={tag}, placeholder={placeholder}, visible={visible}')
                else:
                    print(f'  NOT FOUND: {sel}')
            except Exception as e:
                print(f'  ERROR {sel}: {e}')
        
        # Also check for iframes
        iframes = await page.query_selector_all('iframe')
        print(f'\nFound {len(iframes)} iframes')
        
        # Try getting all textboxes
        textboxes = await page.query_selector_all('[role="textbox"]')
        print(f'Found {len(textboxes)} textboxes')
        
        # Check shadow DOM
        shadows = await page.evaluate('''() => {
            const shadows = [];
            document.querySelectorAll('*').forEach(el => {
                if (el.shadowRoot) shadows.push(el.tagName + ' shadowRoot');
            });
            return shadows;
        }''')
        print(f'Shadow DOMs: {shadows}')
        
        await page.screenshot(path='kimi_input.png', full_page=True)
        print('\nScreenshot saved to kimi_input.png')
        
        await browser.close()

asyncio.run(main())