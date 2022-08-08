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

def humanized_action():
    MIN_MS      = 123
    MAX_MS      = 555
    MS_FACTOR   = 1000
    sleep(ri(MIN_MS, MAX_MS) / MS_FACTOR)

def start():
    DRIVER.get(POLYMTL_MASTER_PROGRAMS_PAGE)

    try:
        WAIT.until(PRESENCE((By.CLASS_NAME, POLYMTL_OPTIONS_CLASS_NAME)))

        PROGRAMS_IGNORE_LIST    = ['Niveaux de formation', 'résultats', '']
        PROGRAMS                = DRIVER.find_elements(By.XPATH, '//h3')
        FILTERED_PROGRAM_NAMES  = []
        ALL = dict()
        for prog in PROGRAMS:
            add = True
            for word in prog.text.split(' '):
                for ignore in PROGRAMS_IGNORE_LIST:
                    for ignored_word in ignore.split(' '):
                        if word.lower() == ignored_word.lower():
                            add = False
                            break
                    if not add:
                        break
                if not add:
                    break
            if add:
                FILTERED_PROGRAM_NAMES.append(prog.text)

        SUB_PROGRAMS = DRIVER.find_elements(By.XPATH, '//a')

        #print(FILTERED_PROGRAM_NAMES)
        FILTERED_SUB_PROGRAM_NAMES = []
        SUB_PROGRAMS_IGNORE_LIST = ['et', 'des', 'génie', 'Femmes et génie']
        SUB_PROGRAMS_ADDITION_LIST = ['option']
        COUNT = [6, 1, 2, 3, 3, 1, 3, 6, 10, 6, 3, 1, 1 ,1]
        latest_idx = 0
        latest_program = FILTERED_PROGRAM_NAMES[latest_idx]
        ALL[latest_program] = dict()
        for sub_program in SUB_PROGRAMS:
            add = False
            for sub_program_word in sub_program.text.split(' '):
                #print(sub_program_word)
                for filtered_program_word in FILTERED_PROGRAM_NAMES:
                    for program_word in filtered_program_word.split(' '):
                        if sub_program_word.lower() == program_word.lower() and sub_program_word.lower() not in SUB_PROGRAMS_IGNORE_LIST and program_word.lower() not in SUB_PROGRAMS_IGNORE_LIST or sub_program_word.lower() in SUB_PROGRAMS_ADDITION_LIST or program_word.lower() in SUB_PROGRAMS_ADDITION_LIST:
                            # print('word match!', sub_program_word.lower(),program_word.lower())
                            add = True
                            break
                    if add:
                        break
                if add:
                    break
            if add:
                do_add = True
                for sub_program_ignore in SUB_PROGRAMS_IGNORE_LIST:
                    if sub_program.text == sub_program_ignore:
                        do_add = False
                if do_add:
                    FILTERED_SUB_PROGRAM_NAMES.append(sub_program.text)
                    if sub_program.text == latest_program:
                        continue
                    else:
                        if sub_program.text.lower() == FILTERED_PROGRAM_NAMES[latest_idx + 1].lower():
                            latest_idx += 1
                            latest_program = FILTERED_PROGRAM_NAMES[latest_idx]
                            ALL[latest_program] = dict()
                        else:

                            #print(sub_program.text)
                            ALL[latest_program][sub_program.text] = ''
    
        print(FILTERED_SUB_PROGRAM_NAMES)
        print(len(FILTERED_SUB_PROGRAM_NAMES))
        # print( ALL)

    except Exception as e:
        #print(e)
        print("Fatal error.")

if __name__ == "__main__":
    start()
