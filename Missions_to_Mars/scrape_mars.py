# Import dependencies

from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import json 
import splinter 

def Initialization():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

MarsScraping = {}

def MarsNews():
    browser = Initialization()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html,"html.parser")

    Content = soup.find('div', class_ = 'content_page')

    Title = Content.find_all('div', class_ = 'content_title')
    NewsTitle = Title[0].text.strip()
    MarsScraping['NewsTitle'] = NewsTitle

    NewsParagraph = soup.find('div', class_ = 'article_teaser_body').text
    MarsScraping['NewsParagraph'] = NewsParagraph

    return MarsScraping

def FeaturedImage():
    browser = Initialization()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html,"html.parser")

    browser.find_by_id("full_image").click()
    browser.find_by_text("more info     ").click()
    html = browser.html
    soup = bs(html,"html.parser")
    featured_image = soup.find("img", class_ = "main_image")["src"]

    featured_image_url = f"https://www.jpl.nasa.gov{featured_image}"
    featured_image_url

    MarsScraping['featured_image_url'] = featured_image_url
    
    return MarsScraping

def MarsFacts():
    browser = Initialization()
    FactsUrl = 'https://space-facts.com/mars/'
    browser.visit(FactsUrl)
    Facts = pd.read_html(FactsUrl)
    #Facts
    
    FactsTable = Facts[0].rename(columns = {0:"Profile",1:"Data"})
    FactsTable = FactsTable.set_index("Profile")
    MarsFactsData = FactsTable.to_html()

    MarsScraping['MarsFactsData'] = MarsFactsData

    return MarsScraping

def Hemispheres():
    browser = Initialization()
    HomeURL = 'https://astrogeology.usgs.gov'
    AstrogelogySite = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(AstrogelogySite)
    html = browser.html
    soup = bs(html,"html.parser")

    HemispheresEnhanced = soup.find('div', class_ = 'collapsible results')
    MarsHemispheresEnhanced = HemispheresEnhanced.find_all('div', class_='item')

    Hemisphere_Image_URLs = []


    for results in MarsHemispheresEnhanced:
    
        try:
    
            MarsHemispheres = results.find('div', class_ = "description")
            Title = MarsHemispheres.h3.text
    
    
            MarsHemispheresUrl = MarsHemispheres.a["href"]    
            browser.visit(HomeURL + MarsHemispheresUrl)
    
            Img_html = browser.html
            Img_soup = bs(Img_html, 'html.parser')
    
            Img_link = Img_soup.find('div', class_='downloads')
            Img_url = Img_link.find('li').a['href']

    
            #Img_dict = {}
            #Img_dict['Title'] = Title
            #Img_dict['Img_url'] = Img_url

            HemData = dict({"Title": Title, "Img_url": Img_url})


        
            Hemisphere_Image_URLs.append(HemData)
     
            #print(Hemisphere_Image_URLs)
            #print("--------------------------------------")
        
        except:
            pass

    MarsScraping['Hemisphere_Image_URLs'] = Hemisphere_Image_URLs

    return MarsScraping











