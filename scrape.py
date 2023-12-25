
#File was changed in local at line no 2
import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
#new
from selenium.webdriver.common.action_chains import ActionChains



downloadLink="https://newsroom.consilium.europa.eu/events/20230608-justice-and-home-affairs-council-june-2023"

download_dir = rf"D:\Python_Projects\WebScrapper\downloadLink"   # Replace with your download directory path
options = Options()

# 0 means to download to the desktop, 1 means to download to the default "Downloads" directory, 2 means to use the directory
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", download_dir)

driver = webdriver.Firefox(options=options)
driver.get(downloadLink)
driver.implicitly_wait(10)

cookie_section = driver.find_element(By.CLASS_NAME, 'cookie-section')
accept_button = cookie_section.find_element(By.CLASS_NAME, 'btn-accept-cookies')
accept_button.click()

Image_section= driver.find_element(By.ID,"ngb-nav-1")
Image_section.click()
time.sleep(2)




# Define the pagination element
paginationClass=driver.find_element(By.CLASS_NAME,"pagination")
page_links = paginationClass.find_elements(By.CLASS_NAME, "page-link")

element = driver.find_element(By.XPATH, "//*[text()='Next']")
time.sleep(2)
element.click()


# while next_button.is_displayed():

#     print(1)
#     next_button.click()
#     time.sleep(2)  # Add a delay to allow the page to load; adjust as needed
#     next_button = pagination.find_element(By.CSS_SELECTOR, 'li.page-item a[aria-label="Next"]')
#

# imageGallery = driver.find_element(By.ID, 'navContent')
# thumbnails = imageGallery.find_elements(By.TAG_NAME, 'nwsr-photo-thumbnail')
# time.sleep(2)
# for thumbnail in thumbnails:
#     #get image name
#     img_elements = thumbnail.find_elements(By.TAG_NAME, 'img')
#
#     image_url = None
#     for img_element in img_elements:
#         image_url = img_element.get_attribute("src")
#         if image_url:
#             break
#
#     # Print the image URL
#     print("Image URL:", image_url)
#     time.sleep(2)
#     thumbnail.click()
#     # break
#
#     image_modal = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, 'modal-body'))
#         )
#     download_button=image_modal.find_element(By.CLASS_NAME,"btn-primary").click()
#
#
#     close_button = image_modal.find_element(By.CLASS_NAME,"close").click()
#     time.sleep(2)
#
# driver.quit()