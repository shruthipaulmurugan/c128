from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

scraped_data = []

def scrape():
    for i in range(0,10):
        print(f'Scraping page {i+1} ...')
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for ul_tag in soup.find_all("ul", attrs={"class", "stars"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []

            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            
            stars_data.append(temp_list)
    print(stars_data[1])
    
scrape()

headers = ["proper_name", "bayer_designation", "distance", "spectral_class", "mass", "radius", "luminosity"]
stars_df_1 = pd.DataFrame(stars_data, columns=headers)
stars_df_1.to_csv('scraped_data.csv', index=True, index_label="id")