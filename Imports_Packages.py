# Built-in modules/packages
import os
import time
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import json
import re

# 3rd party packages that need to be installed #

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# SqlClient
import mysql.connector

# Dateutil
from dateutil.relativedelta import relativedelta

# cryptography
from cryptography.fernet import Fernet