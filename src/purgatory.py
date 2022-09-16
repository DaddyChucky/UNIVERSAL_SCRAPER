__title__       = 'main.py'
__doc__         = 'Clean the data for modeling.'
__author__      = 'DE LAFONTAINE, Charles.'
__copyright__   = 'See MIT license description on the GitHub repo.'


###
#   --> PURGATORY <--
###


from utils import *
from constants_loader import *
from taste_the_rainbow import *
import  json


CATEGORY:       str     = "PURGATORY"
ITERATED_FILE:  int     = 1


def get_out_files_name() -> list:
    """
    Gets the name of the files in the output folder

    Args:
        None
            
    Returns:
        (list) Name of the files in the output folder
    """
    try:
        return os.listdir(os.getcwd() + DATA_OUT_PRE_FOLDER)

    except Exception as e:
        print_failure(CATEGORY, "Can't list out files name @ " + os.getcwd() + DATA_OUT_PRE_FOLDER)
        print_failure(CATEGORY, e)
        exit()

def get_current_iterated_file_content() -> dict:
    out_files_name                  = get_out_files_name()
    dict_out_files_name_and_number  = {}
    for out_file_name in out_files_name:
        out_file_number = out_file_name[:-5]
        out_file_number = int(out_file_number[5:])
        dict_out_files_name_and_number[out_file_number] = out_file_name
    try:
        for key in sorted(dict_out_files_name_and_number.keys()):
            if (ITERATED_FILE <= key):
                with open(os.getcwd() + DATA_OUT_PRE_FOLDER + dict_out_files_name_and_number[key]) as f:
                    return json.load(f)
    
    except Exception as e:
        print_failure(CATEGORY, "Can't open ITERATED_FILE #" + str(ITERATED_FILE))
        print_failure(CATEGORY, e)
        exit()


def run_purgatory():
    current_iterated_file_content:  dict   = get_current_iterated_file_content()
    current_website_visited:        str    = sorted(current_iterated_file_content.keys())[ITERATED_FILE - 1]
    current_content_visited:        list   = current_iterated_file_content[current_website_visited].split('. ')
    try:
        for out_file_name in get_out_files_name():
            data: dict = dict()
            with open(os.getcwd() + DATA_OUT_PRE_FOLDER + out_file_name) as f:
                data = json.load(f)
                for key in data.keys():
                    if key != current_website_visited:
                        data_to_key:        str = data[key]
                        new_data_to_key:    str = ''
                        for sentence in data_to_key.split('. '):
                            if sentence not in current_content_visited:
                                new_data_to_key += sentence
                        data[key] = new_data_to_key
            with open(os.getcwd() + DATA_OUT_PRE_FOLDER + out_file_name, DATA_OUT_OPEN_MODE, encoding=DATA_ENCODING) as f:
                json.dump(data, f, ensure_ascii=DUMP_ENSURE_ASCII, check_circular=DUMP_CHECK_CIRCULAR, allow_nan=DUMP_ALLOW_NAN, indent=DUMP_INDENT)

    except Exception as e:
        print_failure(CATEGORY, "Can't open ITERATED_FILE #" + str(ITERATED_FILE))
        print_failure(CATEGORY, e)
        exit()

run_purgatory()
