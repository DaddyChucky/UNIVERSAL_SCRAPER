__title__       = 'utils.py'
__doc__         = 'Utility for the main algorithm.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo.'


###
#   --> UTILS <--
###


from time import sleep
from random import randint as ri


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
