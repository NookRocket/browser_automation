from playwright.sync_api import sync_playwright

def test_pages(page_data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        for data in page_data:
            page.goto(data['url'])
            for selector, value in data['fields'].items():
                page.fill(selector, value)
            page.click('button[type={}]'.format(data['submit_button']))
            assert (
                page.text_content(data['result_selector'])
                .strip()
                .startswith(data['expected_result'])
            ), 'Test failed: Not match with the expected result'

        browser.close()
        print("All tests Completed")


test_data = [
    {
        'url': 'https://the-internet.herokuapp.com/login',
        'fields': {'#username': 'tomsmith', '#password': 'SuperSecretPassword!'},
        'submit_button': 'submit',
        'result_selector': '#flash',
        'expected_result': 'You logged into a secure area!',
    },
    {
        'url': 'https://the-internet.herokuapp.com/login',
        'fields': {'#username': 'test_user', '#password': 'test_password!'},
        'submit_button': 'submit',
        'result_selector': '#flash',
        'expected_result': 'Your username is invalid!',
    },
]

test_pages(test_data)
