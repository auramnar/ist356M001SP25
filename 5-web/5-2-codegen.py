import re # import for regular expression
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    course = "IST 356" # course code to search for

    # playwright codegen
    browser = playwright.chromium.launch(headless=False) # lauch Chromium browser
    context = browser.new_context() # new context
    page = context.new_page() # open new page
    page.goto("about:blank") # navigate to initial blank page
    page.goto("http://coursecatalog.syr.edu/") # course catalog
    # finds the search field using a CSS selector
    # the search field has a class of "search-field"
    page.get_by_label("Search Keyword Field").click()
    # fill the search field with the course code using the course variable
    # the search field has a class of "search-field"
    page.get_by_label("Search Keyword Field, required").fill(course)
    # simulate pressing the Enter key to submit 
    # the search field has a class of "search-field"
    page.get_by_label("Search Keyword Field, required").press("Enter")
    #find the link element and match the search 
    page.get_by_role("link", name=f"Best Match: {course}").click()
    # create a pop up window for printing  
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Print (opens a new window) ").click()
    
        page1 = page1_info.value # show the pop up window
        # wait for the page to load
        page1.goto(page1.url)

        course_selector = page1.query_selector("table")
        course_text = course_selector.inner_text()
        print(course_text)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
