# Generated by Selenium IDE
from resources.Imports_Packages import *


class TestOlx():
    def __init__(self, data_input):
        self.data = data_input
        self.TableName = None
        self.SqlCredentials = {
            "host": "localhost",
            "user": "root",
            "pwd": "W@qq@w125",
            "db": "olxdata"
        }


    # loads json data as dict
    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as file:
            Data = json.load(file)
        return Data

    # dynamic selection of selector for selenium find_element()
    @staticmethod
    def selector_mapper(selector):
        by_mapping = {
            'ID': By.ID,
            'NAME': By.NAME,
            'XPATH': By.XPATH,
            'CSS_SELECTOR': By.CSS_SELECTOR,
            'TAG_NAME': By.TAG_NAME,
            # Add more mappings as needed
        }
        return by_mapping.get(selector)

    # Extracts id from olx ad website
    @staticmethod
    def extract_iid_from_url(url):
        regex_pattern = r'iid-(\d+)'
        match = re.search(regex_pattern, url)

        if match:
            return int(match.group(1))
        else:
            return None

    # Converts the provided string date statement of DMY sql format
    @staticmethod
    def convert_relative_time_to_datetime(relative_time):
        now = datetime.now()

        if "minute" in relative_time:
            delta = relativedelta(minutes=int(relative_time.split()[0]))
        elif "hour" in relative_time:
            delta = relativedelta(hours=int(relative_time.split()[0]))
        elif "day" in relative_time:
            delta = relativedelta(days=int(relative_time.split()[0]))
        elif "week" in relative_time:
            delta = relativedelta(weeks=int(relative_time.split()[0]))
        elif "year" in relative_time:
            delta = relativedelta(years=int(relative_time.split()[0]))
        else:
            raise ValueError("Unsupported time unit")

        result_datetime = now - delta
        return result_datetime.strftime('%Y-%m-%d %H:%M:%S')

    # Open database and update self.TableName = data["Search"]
    def access_database_and_create_table(self):
        self.TableName = data["search"].replace(" ", "_")
        print(self.TableName)
        connection = None
        try:
            # Attempt to connect to the MySQL server
            connection = mysql.connector.connect(
                host=self.SqlCredentials["host"], user=self.SqlCredentials["user"], password=self.SqlCredentials["pwd"],
                database=self.SqlCredentials["db"]
            )

            # Check if the connection is successful
            if connection.is_connected():
                print("Connected to the MySQL database!")
                # Create a cursor object to interact with the database
                cursor = connection.cursor()

                # Check if the table already exists
                table_exists_query = f"SHOW TABLES LIKE '{self.TableName}'"
                cursor.execute(table_exists_query)
                # Fetch the result
                table_exists = cursor.fetchone()

                # Table does not exist so create table
                if not table_exists:
                    # Define the table creation query with a dynamic table name
                    create_table_query = f"""
                         CREATE TABLE {self.TableName} (
                             id INT PRIMARY KEY,
                             Title VARCHAR(255),
                             Price INT,
                             Location VARCHAR(255),
                             CreatedDate DATETIME,
                             Website VARCHAR(255)
                             
                         )
                         """

                    # Execute the table creation query
                    cursor.execute(create_table_query)
                    # Commit the changes and close the connection
                    print("querry executed")
                    connection.commit()
            else:
                print("Connection failed")
                return ("Connection failed")
        except mysql.connector.Error as err:
            return (f"Error: {err}")
        finally:
            return(connection)


    # close the database
    @staticmethod
    def close_database(connection):
        # Close the connection, if open
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            return ("Db Closed")
        return ("Db not closed")

    def setup_method(self, ):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, ):
        self.driver.quit()

    def click_element_until_hidden_or_disabled(self, CSS_selector, timeout=60, sleep_interval=1):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                element = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_selector))
                )
                element.click()
            except TimeoutException:
                # Handle timeout (element not found, disabled, or hidden)
                break
            except Exception as e:
                # Handle other exceptions if necessary
                print(f"An error occurred: {e}")
                break
            time.sleep(sleep_interval)

    def remove_element(self, selector, selectorValue ):
        while True:
            try:
                # Wait for the presence of the element with the given ID
                element_to_remove = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((self.selector_mapper(selector), selectorValue))
                )
                # Execute JavaScript to remove the element from the DOM
                self.driver.execute_script("arguments[0].remove();", element_to_remove)
            except TimeoutException:
                # No more instances found, break out of the loop
                break

    def test_olx(self):
        # 1 | open | https://www.olx.com.pk/ |
        self.driver.get(self.data["website"])
        # 2 | setWindowSize | 1240x703 |
        self.driver.set_window_size(1240, 703)
        # 3 | click | css=.\_162767a9:nth-child(1) |
        self.driver.find_element(By.CSS_SELECTOR, ".\\_162767a9:nth-child(1)").click()
        # 4 | type | css=.\_162767a9:nth-child(1) | ipad mini 6
        self.driver.find_element(By.CSS_SELECTOR, ".\\_162767a9:nth-child(1)").send_keys(self.data["search"])
        # 5 | sendKeys | css=.\_162767a9:nth-child(1) | ${KEY_ENTER}
        self.driver.find_element(By.CSS_SELECTOR, ".\\_162767a9:nth-child(1)").send_keys(Keys.ENTER)
        # 6 | click | css=.\_95dae89d > .\_4408f4a8 |
        self.click_element_until_hidden_or_disabled(".\\_4408f4a8 > .\\_5079de6b:nth-child(1)")
        # 7 | runScript | window.scrollTo(0,4517.14990234375) |
        self.driver.execute_script("window.scrollTo(0,4517.14990234375)")
        # 8 | click | css=.\_4408f4a8 > .\_5079de6b:nth-child(1) |

        self.remove_element("CSS_SELECTOR", '[id^="ad-placement-middle-"]')

        try:
            # Find all <li> elements that match the specified structure
            matching_elements = self.driver.find_elements(By.XPATH,
                                                     '//ul[@class="ba608fb8 de8df3a3"]/li[@aria-label="Listing"]/article[@class="_7e3920c1"]')

            # Access database and create table if not exists
            connection = self.access_database_and_create_table()

            # Process the matching elements
            for element in matching_elements:
                link = element.find_element(By.TAG_NAME,'a').get_attribute('href')
                price = element.find_element(By.CSS_SELECTOR, '[aria-label="Price"] span').text
                location = element.find_element(By.CSS_SELECTOR, '[aria-label="Location"]').text
                title = element.find_element(By.CSS_SELECTOR, '[aria-label="Title"] p').text
                creation_date = element.find_element(By.CSS_SELECTOR, '[aria-label="Creation date"]').text

                # refined the above values
                IdInt = self.extract_iid_from_url(link)
                TitleStr = title
                priceInt = int(''.join(filter(str.isdigit, price)))
                LocationStr = location
                CreationDate = self.convert_relative_time_to_datetime(creation_date)
                WebsiteStr = link

                # data insert into database
                cursor = connection.cursor()

                # Insert data into the table
                insert_data_query = f"""
                    INSERT IGNORE INTO {self.TableName} (id, Title, Price, Location, CreatedDate, Website)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """

                # Execute the query with the data to insert
                cursor.execute(insert_data_query, (IdInt,TitleStr, priceInt, LocationStr, CreationDate, WebsiteStr))
                # Commit the changes
                connection.commit()

            self.close_database(connection)

        finally:
            # Close the browser
            self.driver.quit()

jsonpath= r"./DataWrapped.json"
data = TestOlx.load_json(jsonpath)
testolx = TestOlx(data)
testolx.setup_method()
testolx.test_olx()
