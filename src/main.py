__title__       = 'main.py'
__doc__         = 'Scraps university courses.'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2022'


###
#   --> RUN FILE <--
###

from loadcsts import *
from time import sleep
from random import randint as ri
from collections import deque
import json

def humanize_action():
    MIN_MS      = 300
    MAX_MS      = 500
    MS_FACTOR   = 1000
    sleep(ri(MIN_MS, MAX_MS) / MS_FACTOR)

def start(page: str):
    DRIVER.get(page)
    RELATED_PAGE    = page[MIN_RELATED_LINK:]
    VISITED_LINKS   = set()
    VISITED_LINKS.add(page)
    humanize_action()
    CONTENT = {}

    try:
        main_links = DRIVER.find_elements(By.XPATH, ALL_LINKS_XPATH)
        humanize_action()

        upcoming_links = deque()
        for link in main_links:
            href = link.get_attribute(LINK_ATTRIBUTE)
            if href == page or ANTI_ANCHOR in href or RELATED_PAGE not in href: continue
            upcoming_links.append(href)
        
        last_link = page

        CONTENT[last_link] = DRIVER.find_element(By.XPATH, BODY_XPATH).text
        humanize_action()

        # Breadth First Search (BFS) Algorithm
        while len(upcoming_links) > 0:
            print(len(upcoming_links))
            current_link = upcoming_links.popleft()
            
            try:
                if current_link in VISITED_LINKS or ANTI_ANCHOR in current_link or RELATED_PAGE not in current_link or last_link == current_link: continue

                VISITED_LINKS.add(current_link)
                print("Currently visiting link:", current_link)
                
                DRIVER.get(current_link)

                page_links = DRIVER.find_elements(By.XPATH, ALL_LINKS_XPATH)

                for page_link in page_links:
                    try:
                        upcoming_links.append(page_link.get_attribute(LINK_ATTRIBUTE))
                    except Exception:
                        continue

                CONTENT[current_link] = DRIVER.find_element(By.XPATH, BODY_XPATH).text
                print("Saved", len(CONTENT[current_link]), "characters for", current_link, "Continuing...")

                last_link = current_link

                with open(os.getcwd() + r"\out\data.json", "w+", encoding="utf-8") as f:
                    json.dump(CONTENT, f, ensure_ascii=True, check_circular=True, allow_nan=True, indent=4)
            
            except Exception:
                continue
        
    except Exception as e:
        print("Fatal error:", e)

if __name__ == "__main__":
    start(POLYMTL_PAGE)
