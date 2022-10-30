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
from threading import Thread


CATEGORY = "PURGATORY"


def get_out_files_name() -> list:
    """
    Gets the name of the files in the output folder

    Args:
        None
            
    Returns:
        (list) Name of the files in the output folder

    Exception:
        Any exception is catched, and outputed
    """
    try:
        return os.listdir(os.getcwd() + DATA_OUT_PRE_FOLDER)
    except Exception as e:
        print_failure(CATEGORY, "Can't list out files name @ " + os.getcwd() + DATA_OUT_PRE_FOLDER)
        print_failure(CATEGORY, e)
        exit()


def get_out_file_number(out_file_name: str) -> int:
    """
    Gets the file number based on its name

    Args:
        (str) out_file_name: File's name, including its extension
            
    Returns:
        (int) The file's associated number

    Exception:
        Any exception is catched, and outputed
    """
    try:
        out_file_number = out_file_name[:-FILE_NAME_CUTOFF]
        return int(out_file_number[FILE_NAME_CUTOFF:])
    except Exception as e:
        print_failure(CATEGORY, "Fatal error during get_out_file_number")
        print_failure(CATEGORY, e)
        exit()


def get_current_iterated_file_content(iterated_file: int) -> dict:
    """
    Gets the current iterated file's content

    Args:
        (int) iterated_file: File's number
            
    Returns:
        (dict) The file's content

    Exception:
        Any exception is catched, and outputed
    """
    try:
        out_files_name:                 list = get_out_files_name()
        dict_out_files_name_and_number: dict = dict()
        for out_file_name in out_files_name:
            out_file_number: int                            = get_out_file_number(out_file_name)
            dict_out_files_name_and_number[out_file_number] = out_file_name
            for key in sorted(dict_out_files_name_and_number.keys()):
                if (iterated_file == key):
                    with open(os.getcwd() + DATA_OUT_PRE_FOLDER + dict_out_files_name_and_number[key]) as f:
                        return json.load(f)
    except Exception as e:
        print_failure(CATEGORY, "Can't open ITERATED_FILE #" + str(iterated_file))
        print(e)
        exit()


def do_clean(dict_to_be_cleaned: dict) -> dict:
    """
    Strips, and cleans non-sentences for all entries of the given dict

    Args:
        (dict) dict_to_be_cleaned: Dictionary to be cleaned
            
    Returns:
        (dict) The cleaned dictionary

    Exception:
        Any exception is catched, and outputed
    """
    try:
        new_dict: dict = dict()
        for key in dict_to_be_cleaned.keys():
            new_content: list = []
            for content in dict_to_be_cleaned[key]:
                content = content.strip()
                for kill_word in KILL_WORDS:
                    if content.find(kill_word.lower()) != FIND_NOT_FOUND: continue
                if content == CLEAN_INVALID_DATA or len(content.split(CLEAN_SENTENCE_CHAR_VERIFIER)) < CLEAN_MIN_SENTENCE_LENGTH: continue
                new_content.append(content)
            if new_content: new_dict[key] = new_content
        return new_dict
    except Exception as e:
        print_failure(CATEGORY, "Fatal error during do_clean")
        print(e)
        exit()


def purgatory(iterated_file: int, cutoff: int) -> dict:
    """
    Purges common sentences, and keywords between all dictionaries in the OUT folder

    Args:
        (int) iterated_file:    Iterated file's number, not to be compared with itself
        (int) cutoff:           Cutoff to retrieve other files for comparison

    Returns:
        (dict) The cleaned, and purged dictionary related to iterated file's content

    Exception:
        Any exception is catched, and outputed
    """
    try:
        split_char:                     str     = "\n"
        current_iterated_file_content:  dict    = get_current_iterated_file_content(iterated_file)
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


def do_purge(start: int, end: int) -> None:
    """
    Runs purgatory for every file present in the OUT folder

    Args: 
        (int) start:    index of start file number
        (int) end:      index of end file number

    Returns:
        None, purged files are under purged folder

    Exception:
        Any exception is catched, and outputed
    """
    try:
        out_files_name: list = get_out_files_name()
        for i in range(start, end):
            print_header(CATEGORY, "Currently purging: " + out_files_name[i] + " (" + str(round(i / len(out_files_name) * PURGE_PERCENT_FACTOR_PURGE, PURGE_ROUND_PRECISION_PURGE_STATUS)) + " %)")
            with open(os.getcwd() + DATA_OUT_POST_FOLDER + out_files_name[i], DATA_OUT_OPEN_MODE, encoding=DATA_ENCODING) as f:
                json.dump(purgatory(get_out_file_number(out_files_name[i]), PURGE_CUTOFF), f, ensure_ascii=DUMP_ENSURE_ASCII, check_circular=DUMP_CHECK_CIRCULAR, allow_nan=DUMP_ALLOW_NAN, indent=DUMP_INDENT)
                print_success(CATEGORY, "Successfully purged " + out_files_name[i] + " !")
    except Exception as e:
        print_failure(CATEGORY, "Fatal error during do_purge")
        print(e)
        exit()

def do_threaded_purge(n_threads: int = N_THREADS):
    """
    Runs threaded purgatory for every file present in the OUT folder

    Args: 
        (int) n_threads: number of threads to be created

    Returns:
        None, purged files are under purged folder

    Exception:
        Any exception is catched, and outputed
    """
    n_files: int = len(get_out_files_name()) - 1
    jobs:       list[int]       = []
    job:        int             = -1
    threads:    list[Thread]    = []
    for _ in range(n_threads):
        job += 1
        jobs.append(job)
        job += n_files // n_threads
        jobs.append(job)
    for i in range(n_threads):
        t: Thread = Thread(target=do_purge, args=[jobs[i], jobs[i + 1]])
        threads.append(t)
    for thread in threads:
        thread.start()


if __name__ == '__main__':
    create_folders(pre=True, post=True, out_pre_folder=DATA_OUT_PRE_FOLDER, out_post_folder=DATA_OUT_POST_FOLDER)
    do_threaded_purge()
