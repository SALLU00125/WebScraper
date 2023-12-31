# Description
 Makes a Sql table with data (  from olx.com.pk about a search querry.
 Helpful in gathering data about a specific product on olx.
 - Search: "Ipad mini 6" ( tableName= "Ipad_mini_6" )
 > > **|   id      |   Title   |   Price   |   Location    |   CreatedDate |   Website |**
 

# Usage and Installation
## Installations:

- Make sure sql is installed ( mysql, mariadb etc) and below credentials are valid:
> 1. host
> 2. user
> 3. password
> 4. databaseName

- Install required python packages
> pip install -r requirements.txt

## Usage:
- Change whatever querry search u like in olx in by make editing in "DataWrapped.json" for "search": $keyword e.g:
> "search": "ipad mini 6"

## Results:
 - Results saved in sql table like:
> **|   id      |   Title   |   Price   |   Location    |   CreatedDate |   Website |**

- search result of all ads of querry search "ipad mini 6"
![Results Image](resources/Results.png)

## TestOlx Class
This class is used to scrape data from the OLX website. It contains methods for loading JSON data, mapping selectors, extracting IDs from URLs, converting relative time to datetime, accessing and creating tables in a database, closing a database, setting up and tearing down methods, clicking elements until they are hidden or disabled, removing elements, and running the main test.

## Methods

### __init__(self, data_input)
This is the constructor method that initializes the TestOlx object. It takes a dictionary as an input and assigns it to the data attribute. It also initializes the TableName attribute to None and sets the SQL credentials.

### load_json(filename)
This static method loads a JSON file and returns it as a dictionary. It takes the filename as an input.

### selector_mapper(selector)
This static method maps a string selector to a selenium By object. It takes the selector as an input and returns the corresponding By object.

### extract_iid_from_url(url)
This static method extracts the id from an OLX ad URL using regex. It takes the URL as an input and returns the id as an integer.

### convert_relative_time_to_datetime(relative_time)
This static method converts a relative time string to a datetime object. It takes the relative time string as an input and returns the datetime object.

### access_database_and_create_table(self)
This method accesses the MySQL database and creates a table if it doesn't exist. It sets the TableName attribute to the search term from the data attribute.

### close_database(connection)
This static method closes the database connection. It takes the connection as an input.

### setup_method(self)
This method sets up the selenium webdriver and initializes the vars attribute.

### teardown_method(self)
This method quits the selenium webdriver.

### click_element_until_hidden_or_disabled(self, CSS_selector, timeout=60, sleep_interval=1)
This method clicks an element until it is hidden or disabled. It takes the CSS selector, timeout, and sleep interval as inputs.

### remove_element(self, selector, selectorValue)
This method removes an element from the DOM. It takes the selector and selector value as inputs.

### test_olx(self)
This is the main method that runs the test. It opens the OLX website, searches for a term, scrolls through the results, removes ads, finds matching elements, accesses the database, processes the matching elements, inserts the data into the database, and finally closes the database and the browser.
