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

CATEGORY = "PURGATORY"

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

def get_out_file_number(out_file_name) -> int:
    FILE_NAME_CUTOFF = 5
    out_file_number = out_file_name[:-FILE_NAME_CUTOFF]
    return int(out_file_number[FILE_NAME_CUTOFF:])

def get_current_iterated_file_content(iterated_file) -> dict:
    out_files_name                  = get_out_files_name()
    dict_out_files_name_and_number  = {}
    for out_file_name in out_files_name:
        out_file_number = get_out_file_number(out_file_name)
        dict_out_files_name_and_number[out_file_number] = out_file_name
    try:
        for key in sorted(dict_out_files_name_and_number.keys()):
            if (iterated_file == key):
                with open(os.getcwd() + DATA_OUT_PRE_FOLDER + dict_out_files_name_and_number[key]) as f:
                    return json.load(f)
    except Exception as e:
        print_failure(CATEGORY, "Can't open ITERATED_FILE #" + str(iterated_file))
        print(e)
        exit()

def do_clean(dict_to_be_cleaned: dict) -> dict:
    INVALID_DATA            = ""
    MIN_SENTENCE_LENGTH     = 15
    SENTENCE_CHAR_VERIFIER  = " "
    new_dict: dict = dict()
    for key in dict_to_be_cleaned.keys():
        new_content: list = []
        for content in dict_to_be_cleaned[key]:
            content = content.strip()
            if content == INVALID_DATA or len(content.split(SENTENCE_CHAR_VERIFIER)) < MIN_SENTENCE_LENGTH: continue
            new_content.append(content)
        if new_content: new_dict[key] = new_content
    return new_dict

def purgatory(iterated_file: int, cutoff: int) -> dict:
    try:
        split_char:                     str     = "\n"
        current_iterated_file_content: dict     = get_current_iterated_file_content(iterated_file)
        for iterated_key in current_iterated_file_content.keys(): 
            current_iterated_file_content[iterated_key] = current_iterated_file_content[iterated_key].split('\n')
        others_content:                 list[dict] = []
        temp_iterated_file = iterated_file
        while True:
            iterated_file -= cutoff
            current_file_content = get_current_iterated_file_content(iterated_file)
            if current_file_content is None: break
            others_content.append(current_file_content)
        iterated_file = temp_iterated_file
        while True:
            iterated_file += cutoff
            current_file_content = get_current_iterated_file_content(iterated_file)
            if current_file_content is None: break
            others_content.append(current_file_content)
        for i in range(len(others_content)):
            for key in others_content[i].keys():
                for other_content in others_content[i][key].split(split_char):
                    for iterated_key in current_iterated_file_content.keys():
                        for z, iterated_sentence in enumerate(current_iterated_file_content[iterated_key]):
                            if other_content == iterated_sentence:
                                current_iterated_file_content[iterated_key][z] = ""
                                break
        return do_clean(current_iterated_file_content)
    except Exception as e:
        print_failure(CATEGORY, "Fatal error during purgatory")
        print(e)
        exit()

def do_purge() -> None:
    CUTOFF                          = 51
    PERCENT_FACTOR_PURGE            = 100
    ROUND_PRECISION_PURGE_STATUS    = 2
    try:
        out_files_name: list = get_out_files_name()
        for i, out_file_name in enumerate(out_files_name):
            print_header(CATEGORY, "Currently purging: " + out_file_name + " (" + str(round(i / len(out_files_name) * PERCENT_FACTOR_PURGE, ROUND_PRECISION_PURGE_STATUS)) + " %)")
            with open(os.getcwd() + DATA_OUT_POST_FOLDER + out_file_name, DATA_OUT_OPEN_MODE, encoding=DATA_ENCODING) as f:
                json.dump(purgatory(get_out_file_number(out_file_name), CUTOFF), f, ensure_ascii=DUMP_ENSURE_ASCII, check_circular=DUMP_CHECK_CIRCULAR, allow_nan=DUMP_ALLOW_NAN, indent=DUMP_INDENT)
                print_success(CATEGORY, "Successfully purged " + out_file_name + " !")
    except Exception as e:
        print_failure(CATEGORY, "Fatal error during do_purge")
        print(e)
        exit()

if __name__ == '__main__':
    do_purge()
