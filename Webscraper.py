#Web scraper because I'm bored

# Import Libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup



import os
os.getcwd()

# Set if you need to
os.chdir("")


# Grab URL
my_url = 'https://www.newegg.com/p/pl?d=graphics+cards&N=100007709&name=Desktop%20Graphics%20Cards'



print(my_url)


# Grab Entire Web Page from URL...
uClient = uReq(my_url)


# Read-in Raw Site Data
page_html = uClient.read()
uClient.close()


# Now we need to parse the html because it's currently just a huge chunk of text
page_soup = soup(page_html, "html.parser")


# check header/content inside the parsed data
page_soup.h1

# Just grabbing random tags from HTML to see what's inside
page_soup.body.span


# Grabs Each Product..."item-container" s
containers = page_soup.findAll("div", {"class":"item-container"})

# How many unique products do we have?
len(containers)



# vvv TESTING/LOOP PROTOTYPING vvv #

# This contains a single product/graphics card: indexing the first container
container = containers[0]

# This references the "a" tag in the html
print(container)




# All nested tags within item-info div for first container/product

# Two-different ways of doing the same thing
divWithInfo = containers[0].find("div","item-branding")
divWithInfo = container.find("div","item-info") 
print(divWithInfo)



# Returns the brand name of the product in container at position 0 (the first container)
divWithInfo.div.a.img["title"]



# Now we want to grab another thing...the description/actual item...a different "a" tag in HTML
container_description = divWithInfo.find("a",{"class":"item-title"})
print(container_description)


# Now that we have the correct HTML "a-"Tag/Chunk...we now want to grab the text description within it
container_description.text



# GRABBING LAST PIECE OF INFO: SHIPPING
# If you are unfamiliar with html/ hypertest markup..."LI" in HTML just means list
shipping_info = divWithInfo.find("li",{"class": "price-ship"})
print(shipping_info)

shipping_info.text.strip()
# END TESTING #




# Put it into CSV File
filename = "products.csv"
f = open(filename,"w")

headers = "Brand, Product_Name, Shipping\n"
f.write(headers)


# Now the for-loop...grabbing titles from all "containers (37)"
# The for-loop works! It displays all brand names, description, and shipping from website

for container in containers:
    # Grabbing Brand
    conInfo = container.find("div","item-info")
    brand = conInfo.div.a.img["title"]
    
    # Grabbing Description
    con_description = conInfo.find("a",{"class":"item-title"})
    actual_description = con_description.text
    
    # Grabbing Shipping
    ship_info = conInfo.find("li",{"class": "price-ship"})
    actual_ship = ship_info.text.strip()
    
    
    
    print(brand)
    print(actual_description)
    print(actual_ship)
    
    f.write(brand + "," + actual_description.replace(",", "|") + "," + actual_ship + "\n")
f.close

