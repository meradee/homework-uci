# In[1]:


# Dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import time


# In[2]:


# First URL to scrape
mars_news_url = 'https://mars.nasa.gov/news'


# In[3]:


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

browser = init_browser()


# ## NASA Mars News

# In[4]:


# Visit url with splinter
browser.visit(mars_news_url)
# Add sleep since sometimes web browser doesn't load quickly enough before returning html data for soup
time.sleep(1)


# In[5]:


# Get html to process
html = browser.html
# Parse with soup
soup = bs(html, 'html.parser')
# find first element which will be latest news
news_latest = soup.find('li', class_='slide')
print(news_latest.prettify())


# In[6]:


# Get news title
news_title = news_latest.find('div', class_="content_title").text
# Get the teaser as paragraph info
news_p = news_latest.find('div', class_="article_teaser_body").text
news_p


# ## JPL Mars Space Images

# In[7]:


# Begin second scrape
mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(mars_image_url)

time.sleep(1)
full_image_button = browser.find_by_id("full_image")
full_image_button.click()
time.sleep(1)

html = browser.html
soup = bs(html, 'html.parser')
image_url = 'https://www.jpl.nasa.gov' + soup.find('div', class_="buttons").find('a', class_="button")['href']
browser.visit(image_url)


# In[8]:


# Get the large image
html = browser.html
soup = bs(html, 'html.parser')
featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('figure').find('a')['href']
featured_image_url


# ## Mars Weather

# In[50]:


url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)


# In[58]:


html = browser.html
soup = bs(html, 'html.parser')

weather_info_list = []

mars_weather = soup.find('p', class_=['css-901oao', 'r-jwli3a', 'r-1qd0xha', 'r-a023e6', 'r-16dba41', 'r-ad9z0x', 'r-bcqeeo', 'r-bnwqim', 'r-qvutc0'])
#mars_weather=(mars_weather.text)
weather_info_list.append(mars_weather) 
print(mars_weather)
weather_info_list


# In[59]:


# print(soup.prettify())


# ## Mars Facts

# In[9]:


facts_url = 'http://space-facts.com/mars/'


# In[10]:


facts_table = pd.read_html(facts_url)
facts_table[0]


# In[17]:


tables = pd.read_html(facts_url)
facts = tables[0].to_html(header=False, index=False)
facts


# ## Mars Hemispheres

# In[20]:


# Initialize empty lists to capture scraped data
h_image_urls = []
hemisphere_names = []
hemisphere_images = []

hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)
html = browser.html
soup = bs(html, 'html.parser')

items = soup.find_all('div', class_="item")
for item in items:
    item_url = item.a['href']
    full_url = 'https://astrogeology.usgs.gov' + item_url
    h_image_urls.append(full_url)

    item_desc = item.div.a.text[:-9]
    hemisphere_names.append(item_desc)
    
# loop for browsing through the image urls    
for img_url in h_image_urls:
    browser.visit(img_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    sample_img = soup.find('img', class_='wide-image')
    img = "https://astrogeology.usgs.gov" + sample_img['src']
    hemisphere_images.append(img)


# In[22]:


scraped_data = {}


# In[23]:


# Save the scraped information
scraped_data['mars_hemisphere_names'] = hemisphere_names
scraped_data['mars_hemisphere_images'] = hemisphere_images
scraped_data


# In[ ]:


browser.quit()


# In[ ]:




