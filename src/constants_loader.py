__title__       = 'constants_loader.py'
__doc__         = 'Load constants.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo.'


###
#   --> GET CONSTANTS <--
###

from taste_the_rainbow import *
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
CATEGORY            = "CONSTANTS_LOADER"

try:
    with open(os.getcwd() + CONSTANTS_FILE_PATH) as CONSTANTS_FILE:
        CONSTANTS = load(CONSTANTS_FILE)

except FileNotFoundError as e:
    print_failure(CATEGORY, "Constants file not found @ " + os.getcwd() + CONSTANTS_FILE_PATH)
    print_failure(CATEGORY, e)
    exit()

try:
    # Controls
    CONTROLS                        = CONSTANTS["CONTROLS"]
    DEBUG                           = CONTROLS["DEBUG"]
    SAVE_DATA                       = CONTROLS["SAVE_DATA"]
    SAVE_DATA_ON_N                  = CONTROLS["SAVE_DATA_ON_N"]
    SAVE_DATA_FACTOR                = CONTROLS["SAVE_DATA_FACTOR"]
    DO_PRINT                        = CONTROLS["DO_PRINT"]
    DO_HUMANIZE                     = CONTROLS["DO_HUMANIZE"]
    CHROME_DRIVER_PATH              = CONTROLS["CHROME_DRIVER_PATH"]
    MAIN_CATEGORY                   = CONTROLS["MAIN_CATEGORY"]
    DATA_OUT_SAVE_FILE_NAME         = CONTROLS["DATA_OUT_SAVE_FILE_NAME"]
    DATA_OUT_FORMAT                 = CONTROLS["DATA_OUT_FORMAT"]
    DATA_OUT_OPEN_MODE              = CONTROLS["DATA_OUT_OPEN_MODE"]
    DATA_ENCODING                   = CONTROLS["DATA_ENCODING"]
    DATA_OUT_PRE_FOLDER             = CONTROLS["DATA_OUT_PRE_FOLDER"]
    DUMP_ENSURE_ASCII               = CONTROLS["DUMP_ENSURE_ASCII"]
    DUMP_CHECK_CIRCULAR             = CONTROLS["DUMP_CHECK_CIRCULAR"]
    DUMP_ALLOW_NAN                  = CONTROLS["DUMP_ALLOW_NAN"]
    DUMP_INDENT                     = CONTROLS["DUMP_INDENT"]

    # Inputs
    INPUTS                          = CONSTANTS["INPUTS"]
    WAIT_FOR_GLOBAL_PAGE_LOAD_XPATH = INPUTS["WAIT_FOR_GLOBAL_PAGE_LOAD_XPATH"]
    ALL_LINKS_XPATH                 = INPUTS["ALL_LINKS_XPATH"]
    BODY_XPATH                      = INPUTS["BODY_XPATH"]
    LINK_ATTRIBUTE                  = INPUTS["LINK_ATTRIBUTE"]
    MIN_RELATED_LINK                = INPUTS["MIN_RELATED_LINK"]
    ANTI_ANCHOR                     = INPUTS["ANTI_ANCHOR"]
    ITERATOR_SEPARATOR              = INPUTS["ITERATOR_SEPARATOR"]

    # Pages
    PAGES                           = CONSTANTS["PAGES"]
    POLYMTL                         = PAGES["POLYMTL"]
    ETS                             = PAGES["ETS"]
    HEC                             = PAGES["HEC"]
    SHERBROOKE                      = PAGES["SHERBROOKE"]

except KeyError as e:
    print_failure(CATEGORY, "Errors getting constants/invalid key")
    print_failure(CATEGORY, e)
    exit()

OPTIONS = Options()

if not DEBUG:
    OPTIONS.add_argument("--headless")
    OPTIONS.add_argument("window-size=1920,1080")
    OPTIONS.add_argument("start-maximized")
    OPTIONS.add_argument("incognito")
    OPTIONS.add_argument("disable-extensions")
    OPTIONS.add_argument("disable-popup-blocking")
    OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])
    OPTIONS.add_experimental_option("excludeSwitches", ['enable-automation'])

SERVICE             = Service(CHROME_DRIVER_PATH)
DRIVER              = webdriver.Chrome(service=SERVICE, options=OPTIONS)
SECS_MAX_TIMEOUT    = 10
WAIT                = WebDriverWait(DRIVER, SECS_MAX_TIMEOUT)
