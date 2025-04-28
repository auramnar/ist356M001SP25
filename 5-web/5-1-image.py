from playwright.sync_api import Playwright, sync_playwright, expect
import requests

# function takes a url as input, i.e. the URL of an image
def download_image(url): 
    # extract the filename from the URL
    # the filename is the last part of the URL after the last "/"
    filename = url.split("/")[-1]
    response = requests.get(url) 
    # open the file in binary write mode
    # and write the content of the response to the file
    with open(filename, 'wb') as file: 
        file.write(response.content)
    return filename # the filename of the downloaded image

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    site = "https://ist256.com/fall2023/"
    page.goto(site)
    
    
    
    # find the image element using a CSS selector
    # the image element has a class of "logo"
    image = page.query_selector("img.logo")
    #retrieve the image  using get_attribute method
    image_source = image.get_attribute("src")
    print(image_source)

    filename = download_image(site + image_source)
    print(filename)
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)