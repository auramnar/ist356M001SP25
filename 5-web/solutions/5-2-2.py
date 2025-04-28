'''
Use Playwright to automate fetching the Syracuse University football schedule 
for a given year, 
extract the schedule table using Pandas, 
output it as an HTML table.

'''

from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from time import sleep # pause execution to allow page to load
import sys # provides access to system-specific parameters and functions

# Function takes playwright object and year as input
def run(playwright: Playwright, year) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://cuse.com/sports/football/schedule/{year}")
    # wait for the entire page to load
    page.wait_for_load_state("load")
    sleep(1) # pause to allow table to render
    # find the table view button and click it
    page.get_by_role("tab", name="Table View not selected").click()
    sleep(1)
    dfs = pd.read_html(page.content())
    
    
    # ---------------------
    context.close()
    browser.close()
    return dfs[0].to_html(index=False)


with sync_playwright() as playwright:
    year = input()
    html_table = run(playwright, year = str(year))
    print (html_table)