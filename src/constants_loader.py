__title__       = 'constants_loader.py'
__doc__         = 'Load constants.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo.'


###
#   --> CONSTANTS_LOADER <--
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


CONSTANTS_FILE_PATH:    str = '.\\src\\constants\\csts.JSON'
CATEGORY:               str = "CONSTANTS_LOADER"


try:
    with open(os.getcwd() + CONSTANTS_FILE_PATH) as CONSTANTS_FILE:
        CONSTANTS: dict = load(CONSTANTS_FILE)

except FileNotFoundError as e:
    print_failure(CATEGORY, "Constants file not found @ " + os.getcwd() + CONSTANTS_FILE_PATH)
    print_failure(CATEGORY, e)
    exit()

try:
    CONTROLS:                           dict        = CONSTANTS ["CONTROLS"]
    DEBUG:                              bool        = CONTROLS  ["DEBUG"]
    SAVE_DATA:                          bool        = CONTROLS  ["SAVE_DATA"]
    SAVE_DATA_ON_N:                     bool        = CONTROLS  ["SAVE_DATA_ON_N"]
    SAVE_DATA_FACTOR:                   int         = CONTROLS  ["SAVE_DATA_FACTOR"]
    DO_PRINT:                           bool        = CONTROLS  ["DO_PRINT"]
    DO_HUMANIZE:                        bool        = CONTROLS  ["DO_HUMANIZE"]
    CHROME_DRIVER_PATH:                 str         = CONTROLS  ["CHROME_DRIVER_PATH"]
    MAIN_CATEGORY:                      str         = CONTROLS  ["MAIN_CATEGORY"]
    DATA_OUT_SAVE_FILE_NAME:            str         = CONTROLS  ["DATA_OUT_SAVE_FILE_NAME"]
    DATA_OUT_FORMAT:                    str         = CONTROLS  ["DATA_OUT_FORMAT"]
    DATA_OUT_OPEN_MODE:                 str         = CONTROLS  ["DATA_OUT_OPEN_MODE"]
    DATA_ENCODING:                      str         = CONTROLS  ["DATA_ENCODING"]
    DATA_OUT_PRE_FOLDER:                str         = CONTROLS  ["DATA_OUT_PRE_FOLDER"]
    DATA_OUT_POST_FOLDER:               str         = CONTROLS  ["DATA_OUT_POST_FOLDER"]
    DUMP_ENSURE_ASCII:                  bool        = CONTROLS  ["DUMP_ENSURE_ASCII"]
    DUMP_CHECK_CIRCULAR:                bool        = CONTROLS  ["DUMP_CHECK_CIRCULAR"]
    DUMP_ALLOW_NAN:                     bool        = CONTROLS  ["DUMP_ALLOW_NAN"]
    DUMP_INDENT:                        int         = CONTROLS  ["DUMP_INDENT"]
    SECS_MAX_TIMEOUT:                   int         = CONTROLS  ["SECS_MAX_TIMEOUT"]
    LATEST_SAVE_CHECK:                  int         = CONTROLS  ["LATEST_SAVE_CHECK"]
    FILE_NAME_CUTOFF:                   int         = CONTROLS  ["FILE_NAME_CUTOFF"]
    CLEAN_INVALID_DATA:                 str         = CONTROLS  ["CLEAN_INVALID_DATA"]
    CLEAN_MIN_SENTENCE_LENGTH:          int         = CONTROLS  ["CLEAN_MIN_SENTENCE_LENGTH"]
    CLEAN_SENTENCE_CHAR_VERIFIER:       str         = CONTROLS  ["CLEAN_SENTENCE_CHAR_VERIFIER"]
    PURGE_CUTOFF:                       int         = CONTROLS  ["PURGE_CUTOFF"]
    PURGE_PERCENT_FACTOR_PURGE:         int         = CONTROLS  ["PURGE_PERCENT_FACTOR_PURGE"]
    PURGE_ROUND_PRECISION_PURGE_STATUS: int         = CONTROLS  ["PURGE_ROUND_PRECISION_PURGE_STATUS"]
    FIND_NOT_FOUND:                     int         = CONTROLS  ["FIND_NOT_FOUND"]
    KILL_WORDS:                         list[str]   = CONTROLS  ["KILL_WORDS"]

    INPUTS:                             dict    = CONSTANTS ["INPUTS"]
    WAIT_FOR_GLOBAL_PAGE_LOAD_XPATH:    str     = INPUTS    ["WAIT_FOR_GLOBAL_PAGE_LOAD_XPATH"]
    ALL_LINKS_XPATH:                    str     = INPUTS    ["ALL_LINKS_XPATH"]
    BODY_XPATH:                         str     = INPUTS    ["BODY_XPATH"]
    LINK_ATTRIBUTE:                     str     = INPUTS    ["LINK_ATTRIBUTE"]
    MIN_RELATED_LINK:                   int     = INPUTS    ["MIN_RELATED_LINK"]
    ANTI_ANCHOR:                        str     = INPUTS    ["ANTI_ANCHOR"]
    ITERATOR_SEPARATOR:                 str     = INPUTS    ["ITERATOR_SEPARATOR"]

    PAGES:                              dict    = CONSTANTS ["PAGES"]
    POLYMTL:                            str     = PAGES     ["POLYMTL"]
    ETS:                                str     = PAGES     ["ETS"]
    HEC:                                str     = PAGES     ["HEC"]
    SHERBROOKE:                         str     = PAGES     ["SHERBROOKE"]
    YOUR_WEBSITE_HERE:                  str     = PAGES     ["YOUR_WEBSITE_HERE"]

except KeyError as e:
    print_failure(CATEGORY, "Errors getting constants/invalid key")
    print_failure(CATEGORY, e)
    exit()

OPTIONS: Options = Options()

if not DEBUG:
    OPTIONS.add_argument            ("--headless")
    OPTIONS.add_argument            ("window-size=1920,1080")
    OPTIONS.add_argument            ("start-maximized")
    OPTIONS.add_argument            ("incognito")
    OPTIONS.add_argument            ("disable-extensions")
    OPTIONS.add_argument            ("disable-popup-blocking")
    OPTIONS.add_experimental_option ("excludeSwitches", ["enable-logging"])
    OPTIONS.add_experimental_option ("excludeSwitches", ['enable-automation'])
