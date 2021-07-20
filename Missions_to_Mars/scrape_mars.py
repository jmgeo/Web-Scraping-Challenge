#import dependencies
import pandas as pd
from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

#define the scraping function
def scrape():
    # FEATURED IMAGE SCRAPE
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    img = [i.get("src") for i in soup.find_all("img", class_="headerimage fade-in")]
    featured_image_url = url + img[0]

