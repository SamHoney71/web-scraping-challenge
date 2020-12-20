from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd


def init_browser():
    executable_path = {"executable_path": r"C:\users\gjete\bin\chromedriver"}
    return Browser("chrome", executable_path, headless=False)
    

#NASA Mars News function
def scrape_news():
    browser = init_browser()

    # visit mars.nansa.gov
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    #scape page into Soup
    mars_html = browser.html
    news_soup = BeautifulSoup(mars_html, 'html.parser')
    lists = news_soup.find("div", class_="list_text")

    # Get title and news teaser
    news_title = lists.find("div", class_= "content_title").text
    news_p = lists.find("div", class_= "article_teaser_body").text
 
    # put lists into dictionary
    scrape_dict = {"news_title": news_title,
                "new_headline": news_p
                }

    browser.quit()
    
    return scrape_dict
  

# #JPL Mars Space Images - Featured Image function
def scrape_space_image():
    browser = init_browser()

    #visit jpl.nasa.gov
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    
    time.sleep(1)

    # scrape into Soup
    image_html = browser.html
    image_soup = BeautifulSoup(image_html, 'html.parser')

    # locate the html
    feature_image_wide = image_soup.find("div", class_="carousel_container")
    dirty_feature_image_url = feature_image_wide.find("article", class_="carousel_item")["style"]

    # clean the unneeded text
    featured_image_url_1 = dirty_feature_image_url.replace('background-image: url(','')
    featured_image_url_2 = featured_image_url_1.replace(');','')[1:-1]

    # make & print the url link
    featured_image_url = "https://www.jpl.nasa.gov"+featured_image_url_2

    image_url_dict = {"image_url": featured_image_url}

    browser.quit()

    return image_url_dict


# Mars Facts Table Funtion
def scrape_fact_table():
    browser = init_browser()

    #visit space-facts.com 
    url = "https://space-facts.com/mars/"
    browser.visit(url)

    time.sleep(1)

    #Scrape into Soup
    facts_html = browser.html
    facts_soup = BeautifulSoup(facts_html, 'html.parser')

    # locate the html for the fact table
    mars_facts_wide = facts_soup.find("table", class_="tablepress tablepress-id-p-mars")

    #scrape data into list
    table_rows = facts_soup.find('tbody').find_all('tr')
    l=[]
    for tr in table_rows:
        td=tr.find_all('td')
        row = [str(tr.get_text()).strip() for tr in td]
        l.append(row)

    #convert to a pandas dataframe
    mars_fact_df = pd.DataFrame(l)
    #convert to html
    mars_fact_html = mars_fact_df.to_html()

    browser.quit()
   
    return mars_fact_html


# # Mars Hemispheres

def scrape_mars_hemi():
    browser = init_browser()
    #visit website
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    #make into Soup
    hemi_html = browser.html
    hemi_soup = BeautifulSoup(hemi_html, 'html.parser')

    # Narrow scrape to right area
    hemi_image_wide = hemi_soup.find("div", class_="collapsible results").find_all("div", class_="item")

    # Scrape title and image url into dictionary
    image_dict =[]
    for image in hemi_image_wide:
        image_url = "https://astrogeology.usgs.gov" + image.find("a", class_="itemLink product-item")["href"]  
        image_title = image.find("h3").get_text()
        image_dict.append({"title": image_title, "img_url": image_url})

    browser.quit()
   
    return image_dict


def master_scrape():

    master_scrape_dict = {}
    
    master_scrape_dict["mars_news"] = scrape_news()
    master_scrape_dict["jpl_image"] = scrape_space_image()
    master_scrape_dict["mars_facts"] = scrape_fact_table()
    master_scrape_dict["mars_hemi"] = scrape_mars_hemi()
    
    return master_scrape_dict
