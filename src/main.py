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

def humanize_action():
    MIN_MS      = 300
    MAX_MS      = 500
    MS_FACTOR   = 1000
    sleep(ri(MIN_MS, MAX_MS) / MS_FACTOR)

def start():
    page = POLYMTL_PAGE
    DRIVER.get(page)
    RELATED_PAGE    = page[MIN_RELATED_LINK:]
    VISITED_LINKS   = set()
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
            current_link = upcoming_links.popleft()
            
            if last_link == current_link or ANTI_ANCHOR in current_link or RELATED_PAGE not in current_link or current_link in VISITED_LINKS: continue
            
            VISITED_LINKS.add(current_link)
            print("Currently visiting link:", current_link)
            
            DRIVER.get(current_link)
            humanize_action()

            page_links = DRIVER.find_elements(By.XPATH, ALL_LINKS_XPATH)
            humanize_action()

            for page_link in page_links:
                upcoming_links.append(page_link.get_attribute(LINK_ATTRIBUTE))

            CONTENT[current_link] = DRIVER.find_element(By.XPATH, BODY_XPATH).text
            print("Saved", len(CONTENT[current_link]), "characters. Continuing.")

            humanize_action()

            last_link = current_link
        
    except Exception as e:
        print("Fatal error:", e)

if __name__ == "__main__":
    start()
