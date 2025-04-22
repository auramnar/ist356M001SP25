'''

 Open the IMDb Top 250 page, 
 Find the main heading, extracts its tag name ("H1") and its text content (like "Top 250 Movies"), 
 Print  and then closes the browser


'''




from playwright.sync_api import Playwright, sync_playwright, expect

# one argument, playwright, which is expected to be an instance of the Playwright class
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # browser context with the launched browser
    # open a new tab in your browser
    page = context.new_page()
    page.goto("https://www.imdb.com/chart/top/")

    # Let's scrape the heading off the page!
    # use a CSS selector "h1" to find the first HTML element loaded page that match the selector
    # the selector is a string of the value or None if nothing is found
    heading = page.query_selector("h1")

    # the tag name of the element
    # JS function to get the tag name of the element
    # the evaluate method takes a function as an argument and runs it in the browser context
    tag =heading.evaluate("el => el.tagName")
    print(tag)

    # the contents of the element
    # the inner_text method returns the text content of the element
    print(heading.inner_text())
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)