from Imports_Packages import *

downloadLink = "https://www.olx.com.pk/q-ipad-mini-6"
options = Options()
driver = webdriver.Edge(options=options)
driver.get(downloadLink)
driver.implicitly_wait(2)
# googlesignIn = driver.find_element(By.ID, 'container').find_element(By.ID,"close").click()

google_signin_frame = WebDriverWait(driver, 3).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[contains(@src, "accounts.google.com/gsi/iframe")]'))
)

close = driver.find_element(By.ID, "close")
close.click()

button_xpath = "//a[@class='_95dae89d']/button"
# ButtonAV = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, button_xpath))
#     )

load_more_button = driver.find_element(By.XPATH, button_xpath)

# Click the button
load_more_button.click()








parent_div = driver.find_element(By.CLASS_NAME, '_1e7904e8')

# Find the search input field within the parent div
search_input = parent_div.find_element(By.CLASS_NAME, '_162767a9')
search_input.clear()
search_input.send_keys("Search THIS")
search_button = parent_div.find_element(By.CLASS_NAME, 'a3e390b5')
search_button.click()
