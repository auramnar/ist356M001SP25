'''
47Scrape the additional textbook recommendations from:

https://ist256.com/fall2023//syllabus/

for each recommendation print it in a loop:

'''


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023//syllabus/")

    textbooks_section = page.query_selector("h3#textbooks")
    next = textbooks_section.query_selector("~ *")
    # skip ahead 3 siblings
    for i in range(3):
        next = next.query_selector("~ *")

    # print the inner text of each <li> element
    for item in next.query_selector_all("li"):
        print(item.inner_text())
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)




'''
part 2

'''


from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/syllabus")
    
    start_element = page.query_selector('h4#criteria-for-project-grade')
    #print(start_element.inner_text())
    next_element = start_element.query_selector("~ *")
    bullet_elements = next_element.query_selector_all("li")
    
    criteria = []
    for bullet_element in bullet_elements:
        criteria.append(bullet_element.inner_text())
    


    
    # ---------------------
    context.close()
    browser.close()

    return criteria

with sync_playwright() as playwright:
    criteria = run(playwright)
    print(criteria)
