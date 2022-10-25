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

CATEGORY        = "PURGATORY"

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

def get_current_iterated_file_content(iterated_file) -> dict:
    out_files_name                  = get_out_files_name()
    dict_out_files_name_and_number  = {}
    for out_file_name in out_files_name:
        out_file_number = out_file_name[:-5]
        out_file_number = int(out_file_number[5:])
        dict_out_files_name_and_number[out_file_number] = out_file_name
    try:
        for key in sorted(dict_out_files_name_and_number.keys()):
            if (iterated_file == key):
                print(iterated_file, key)
                with open(os.getcwd() + DATA_OUT_PRE_FOLDER + dict_out_files_name_and_number[key]) as f:
                    return json.load(f)
    
    except Exception as e:
        print_failure(CATEGORY, "Can't open ITERATED_FILE #" + str(iterated_file))
        print_failure(CATEGORY, e)
        exit()

def run_purgatory(iterated_file) -> None:
    split_char:                     str     = "\n"
    current_iterated_file_content = get_current_iterated_file_content(iterated_file)
    for iterated_key in current_iterated_file_content.keys(): 
        current_iterated_file_content[iterated_key] = current_iterated_file_content[iterated_key].split('\n')
    others_content:                 list[dict] = []
    temp_iterated_file = iterated_file
    while True:
        iterated_file -= 51
        current_file_content = get_current_iterated_file_content(iterated_file)
        if current_file_content is None: break
        others_content.append(current_file_content)
    iterated_file = temp_iterated_file
    while True:
        iterated_file += 51
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
                    # current_iterated_file_content[iterated_key].replace(other_content, "")


    print(current_iterated_file_content)
    # for i in range(len(others_content)):
    #     for other_sentence in others_content[i]:
    #         current_iterated_file_content.replace(other_sentence, "")

    # print(current_iterated_file_content.split(split_char))

    # for out_file_name in get_out_files_name():
    #     with open(os.getcwd() + DATA_OUT_POST_FOLDER + out_file_name, DATA_OUT_OPEN_MODE, encoding=DATA_ENCODING) as f:
    #         json.dump(data, f, ensure_ascii=DUMP_ENSURE_ASCII, check_circular=DUMP_CHECK_CIRCULAR, allow_nan=DUMP_ALLOW_NAN, indent=DUMP_INDENT)

    # current_website_visited:        str     = sorted(current_iterated_file_content.keys())[ITERATED_FILE - 1]
    # current_content_visited:        list    = current_iterated_file_content[current_website_visited].split(split_char)
    
    # try:
    #     for out_file_name in get_out_files_name():
    #         data = dict()
    #         with open(os.getcwd() + DATA_OUT_PRE_FOLDER + out_file_name) as f:
    #             data = json.load(f)
    #             for key in data.keys():
    #                 if key != current_website_visited:
    #                     data_to_key:        str = data[key] 
    #                     new_data_to_key:    str = ''
    #                     for sentence in data_to_key.split(split_char):
    #                         if sentence not in current_content_visited:
    #                             # print("def:", current_content_visited[0], "sentence:", sentence)
    #                             new_data_to_key += sentence
    #                     data[key] = new_data_to_key
    #         with open(os.getcwd() + DATA_OUT_POST_FOLDER + out_file_name, DATA_OUT_OPEN_MODE, encoding=DATA_ENCODING) as f:
    #             # print(data)
    #             json.dump(data, f, ensure_ascii=DUMP_ENSURE_ASCII, check_circular=DUMP_CHECK_CIRCULAR, allow_nan=DUMP_ALLOW_NAN, indent=DUMP_INDENT)

    # except Exception as e:
    #     print_failure(CATEGORY, "Can't open ITERATED_FILE #" + str(ITERATED_FILE))
    #     print_failure(CATEGORY, e)
    #     exit()

run_purgatory(51)
