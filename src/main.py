__title__       = 'main.py'
__doc__         = 'Generic scraper for any website.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo.'


###
#   --> RUN FILE <--
###

from utils import *
from constants_loader import *
from taste_the_rainbow import *
from collections import deque
import json


def do_save(content: dict) -> None:
    if SAVE_DATA: # Double check
        if not os.path.exists(os.getcwd() + DATA_OUT_PRE_FOLDER):
            os.makedirs(os.getcwd() + DATA_OUT_PRE_FOLDER)

        with open(os.getcwd() + DATA_OUT_PRE_FOLDER + DATA_OUT_SAVE_FILE_NAME + DATA_OUT_FORMAT, DATA_OUT_OPEN_MODE, encoding=DATA_ENCODING) as f:
            json.dump(content, f, ensure_ascii=DUMP_ENSURE_ASCII, check_circular=DUMP_CHECK_CIRCULAR, allow_nan=DUMP_ALLOW_NAN, indent=DUMP_INDENT)

def start(pages: list[str]) -> None:
    #TODO Add multiprocessing/threading here!
    for page in pages:
        start(page)

def bfs(upcoming_links: deque, visited_links: set[str], related_page: str, content: dict, last_link: str) -> None:
    N_WEBSITES_VISITED  = 1
    TRUE_COUNT          = N_WEBSITES_VISITED
    while len(upcoming_links) > 0:
        if DO_PRINT:
            print_header(MAIN_CATEGORY, "Visited " + str(N_WEBSITES_VISITED) + " website(s) and counting...")
            print_warning(MAIN_CATEGORY, "Number of upcoming links: " + str(len(upcoming_links)))

        current_link = upcoming_links.popleft()
        print(related_page not in current_link or last_link == current_link)
        try:
            if current_link in visited_links or ANTI_ANCHOR in current_link or related_page not in current_link or last_link == current_link: continue

            visited_links.add(current_link)

            if DO_PRINT:
                print_header(MAIN_CATEGORY, "Currently visiting link: " + current_link)
            
            DRIVER.get(current_link)
            if DO_HUMANIZE:
                humanize_action()

            N_WEBSITES_VISITED  += 1
            TRUE_COUNT          += 1

            page_links = DRIVER.find_elements(By.XPATH, ALL_LINKS_XPATH)
            if DO_HUMANIZE:
                humanize_action()

            for page_link in page_links:
                try:
                    upcoming_links.append(page_link.get_attribute(LINK_ATTRIBUTE))
                except Exception:
                    continue

            content[current_link] = DRIVER.find_element(By.XPATH, BODY_XPATH).text
            if DO_HUMANIZE:
                humanize_action()

            if DO_PRINT:
                print_success(MAIN_CATEGORY, "Saved " + str(len(content[current_link])) + " characters for " + current_link)

            last_link = current_link

            if SAVE_DATA:
                if SAVE_DATA_ON_N and TRUE_COUNT % SAVE_DATA_FACTOR != 0: continue
                TRUE_COUNT = 0
                do_save(content)
        
        except Exception:
            continue

def start(page: str) -> None:
    DRIVER.get(page)
    RELATED_PAGE        = page[MIN_RELATED_LINK:]
    VISITED_LINKS       = set()
    CONTENT             = dict()
    VISITED_LINKS.add(page)

    try:
        main_links = DRIVER.find_elements(By.XPATH, ALL_LINKS_XPATH)
        if DO_HUMANIZE:
            humanize_action()

        upcoming_links = deque()
        for link in main_links:
            href = link.get_attribute(LINK_ATTRIBUTE)
            if href == page or ANTI_ANCHOR in href or RELATED_PAGE not in href: continue
            upcoming_links.append(href)
        
        last_link = page

        CONTENT[last_link] = DRIVER.find_element(By.XPATH, BODY_XPATH).text
        if DO_HUMANIZE:
            humanize_action()

        if DO_PRINT:
            print_header(MAIN_CATEGORY, "Starting BFS algorithm")
        bfs(upcoming_links, VISITED_LINKS, RELATED_PAGE, CONTENT, last_link)
        
    except Exception as e:
        print_failure(MAIN_CATEGORY, "Fatal error")
        print_failure(MAIN_CATEGORY, e)
        exit()

if __name__ == "__main__":
    start(POLYMTL)
