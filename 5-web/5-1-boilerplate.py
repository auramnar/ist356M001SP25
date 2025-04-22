
'''
This is a boilerplate code for web scraping using Playwright.
Playwright is a Node.js library to automate Chromium, Firefox, and WebKit with a single API. It is used for web scraping and testing web applications.


Launch a browser
Create new browser content
Open a ne page with in context
Go to web page
Retrieve the HTML source code as a string
Close the page and browser


'''






from playwright.sync_api import Playwright, sync_playwright, expect
# expect is used for assertions i.e. checking if the page has loaded correctly


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) # launch Chromium browser
    # headless=False means the browser will be visible
    context = browser.new_context()
    # open a new tab in your browser
    page = context.new_page()
    # address to go to 
    page.goto("https://www.imdb.com/chart/top/")
    # retrieves HTML source code as a string
    content = page.content()
    print(content)
    
    # ---------------------
    context.close() # close any open page within the context 
    browser.close() # close the Chromium browser

# this is the execution block that runs the code above
# start the code and shuts down when finished
with sync_playwright() as playwright:
    run(playwright)