#26
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/")

    # Let's scrape the page!
    # use pandas read_html to parse the HTML

    # get a list of all tables on the page
    dfs = pd.read_html(page.content())

    # print the first table
    print(dfs[0])
    
    assign = dfs[0]
    assign.to_csv("assign.csv", index=False)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)