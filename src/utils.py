__title__       = 'utils.py'
__doc__         = 'Utility for the main algorithm.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo.'


###
#   --> UTILS <--
###


from taste_the_rainbow import *
from time import sleep
from random import randint as ri
from os import mkdir, getcwd
from os.path import exists

from constants_loader import CATEGORY


CATEGORY = "UTILS"


def humanize_action() -> None:
    """
    Humanizes an action (gives a delay betwen 100-500ms)

    Args:
        None
            
    Returns:
        None
    """
    MIN_MS      = 100
    MAX_MS      = 500
    MS_FACTOR   = 1000
    sleep(ri(MIN_MS, MAX_MS) / MS_FACTOR)


def verify_folders_rich_presence(folder: str) -> bool:
    """
    Verifies crucial folder's rich presence

    Args:
        (str) folder: Folder to check rich presence for
            
    Returns:
        (bool) Whether folder exists
    
    Exception:
        Any exception is catched, and outputed
    """
    try:
        return exists(getcwd() + folder)
    except Exception as e:
        print_failure(CATEGORY, "Fatal error during verify_folders_rich_presence")
        print(e)
        exit()


def create_folders(pre: bool = False, post: bool = False, out_pre_folder: str | None = None, out_post_folder: str | None = None) -> None:
    """
    Creates pre, post, or both folders

    Args:
        (bool)          pre:                Whether pre's folder is to be created   |   default: False
        (bool)          post:               Whether post's folder is to be created  |   default: False
        (str | None)    out_pre_folder:     Out's pre folder name                   |   default: None
        (str | None)    out_post_folder:    Out's post folder name                  |   default: None
            
    Returns:
        None (folders are created)
    
    Exception:
        Any exception is catched, and outputed
    """
    try:
        if pre and not verify_folders_rich_presence(out_pre_folder):    mkdir(getcwd() + out_pre_folder)
        if post and not verify_folders_rich_presence(out_post_folder):  mkdir(getcwd() + out_post_folder)
    except Exception as e:
        print_failure(CATEGORY, "Fatal error during create_folders")
        print(e)
        exit()
