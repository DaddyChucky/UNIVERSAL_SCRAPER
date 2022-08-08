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

CONSTANTS_FILE_PATH = 'csts.JSON'

try:
    with open(CONSTANTS_FILE_PATH) as CONSTANTS_FILE:
        CONSTANTS = load(CONSTANTS_FILE)

except FileNotFoundError as e:
    print(e)
    exit("FATAL: Could not find specified file")

try:
    DEBUG                           = CONSTANTS ["DEBUG"]
    CHROME_DRIVER_PATH              = CONSTANTS ["CHROME_DRIVER_PATH"]
    POLYMTL_MASTER_PROGRAMS_PAGE    = CONSTANTS ["POLYMTL_MASTER_PROGRAMS_PAGE"]
    INPUTS                          = CONSTANTS ["INPUTS"]
    POLYMTL_OPTIONS_CLASS_NAME      = INPUTS    ["POLYMTL_OPTIONS_CLASS_NAME"]

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
