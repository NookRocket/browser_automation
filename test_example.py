import re
import pytest
from playwright.sync_api import Page, expect

url = 'https://playwright.dev/'

def test_has_title(page: Page):
    page.goto(url)

    expect(page).to_have_title(re.compile('Playwright'))

def test_get_started_link(page: Page):
    page.goto(url)
    # Click the get started link.
    page.get_by_role('link', name='Get started').click()

    expect(page.get_by_role('heading', name='Installation')).to_be_visible()

