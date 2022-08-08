__title__       = 'loadcsts.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'


###
#   --> GET CONSTANTS <--
###

from json import load
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located  as PRESENCE
from selenium.webdriver.support.expected_conditions import element_to_be_clickable  as CLICKABLE
import os

CONSTANTS_FILE_PATH = '.\\src\\constants\\csts.JSON'
print(os.getcwd() + CONSTANTS_FILE_PATH)

try:
    with open(os.getcwd() + CONSTANTS_FILE_PATH) as CONSTANTS_FILE:
        CONSTANTS = load(CONSTANTS_FILE)

except FileNotFoundError as e:
    print(e)
    exit("FATAL: Could not find specified file")

try:
    DEBUG                           = CONSTANTS ["DEBUG"]
    CHROME_DRIVER_PATH              = CONSTANTS ["CHROME_DRIVER_PATH"]
    POLYMTL_PAGE                    = CONSTANTS ["POLYMTL_PAGE"]
    INPUTS                          = CONSTANTS ["INPUTS"]
    WAIT_FOR_GLOBAL_PAGE_LOAD_XPATH = CONSTANTS ["INPUTS"]["WAIT_FOR_GLOBAL_PAGE_LOAD_XPATH"]
    ALL_LINKS_XPATH                 = CONSTANTS ["INPUTS"]["ALL_LINKS_XPATH"]
    BODY_XPATH                      = CONSTANTS ["INPUTS"]["BODY_XPATH"]
    LINK_ATTRIBUTE                  = CONSTANTS ["INPUTS"]["LINK_ATTRIBUTE"]
    MIN_RELATED_LINK                = CONSTANTS ["INPUTS"]["MIN_RELATED_LINK"]
    ANTI_ANCHOR                     = CONSTANTS ["INPUTS"]["ANTI_ANCHOR"]

except KeyError as e:
    print(e)
    exit("FATAL: Could not find required constant")

OPTIONS = Options()

if not DEBUG:
    OPTIONS.add_argument("--headless")
    OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])
    OPTIONS.add_argument("window-size=1920,1080")
    OPTIONS.add_argument("start-maximized")
    OPTIONS.add_argument("incognito")
    OPTIONS.add_argument("disable-extensions")
    OPTIONS.add_argument("disable-popup-blocking")
    OPTIONS.add_experimental_option("excludeSwitches", ['enable-automation'])

SERVICE                     = Service(CHROME_DRIVER_PATH)
DRIVER                      = webdriver.Chrome(service=SERVICE, options=OPTIONS)
SECS_MAX_TIMEOUT            = 10
WAIT = WebDriverWait(DRIVER, SECS_MAX_TIMEOUT)
