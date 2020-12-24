#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### NASA Mars News

# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


html = browser.html


# In[5]:


soup = bs(html,"html.parser")


# In[6]:


print(soup.prettify())


# In[7]:


Content = soup.find('div', class_ = 'content_page')


# In[8]:


NewsTitle = Content.find_all('div', class_ = 'content_title')
print(NewsTitle[0].text.strip())


# In[9]:


NewsParagraph = soup.find('div', class_ = 'article_teaser_body').text
print (NewsParagraph)


# ### JPL Mars Space Images - Featured Image

# In[10]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[11]:


html = browser.html


# In[12]:


soup = bs(html,"html.parser")


# In[13]:


browser.find_by_id("full_image").click()


# In[15]:


browser.find_by_text("more info     ").click()


# In[16]:


html = browser.html
soup = bs(html,"html.parser")
featured_image = soup.find("img", class_ = "main_image")["src"]


# In[17]:


featured_image


# In[18]:


featured_image_url = f"https://www.jpl.nasa.gov{featured_image}"
featured_image_url


# ### Mars Facts

# In[19]:


FactsUrl = 'https://space-facts.com/mars/'


# In[20]:


Facts = pd.read_html(FactsUrl)
Facts


# In[21]:


Facts[0].rename(columns = {0:"Profile",1:"Data"})


# In[22]:


Facts[1]


# ### Mars Hemispheres

# In[23]:


HomeURL = 'https://astrogeology.usgs.gov'
AstrogelogySite = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(AstrogelogySite)


# In[24]:


html = browser.html


# In[25]:


soup = bs(html,"html.parser")


# In[26]:


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

    
        Img_dict = {}
        Img_dict['Title'] = Title
        Img_dict['Img_url'] = Img_url
        
        Hemisphere_Image_URLs.append(Img_dict)
     
        print(Hemisphere_Image_URLs)
        print("--------------------------------------")
        
    except:
        pass


# In[27]:


Hemisphere_Image_URLs


# In[ ]:





# In[ ]:





# In[ ]:




