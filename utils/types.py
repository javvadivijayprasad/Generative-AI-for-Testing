from playwright.sync_api import Playwright, Browser, Page

class CustomContext:
    page:Page
    browser:Browser
    playwright:Playwright