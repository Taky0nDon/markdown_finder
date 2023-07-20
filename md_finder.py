import os
from typing import Iterator
import re
from pprint import pprint

DEFAULT_DIR = r"C:\users\mourn\100_days_of_code"
PROJECT_DIR = r"C:\Users\Mourn\my_project\markdown_finder"
directory_walk = os.walk(DEFAULT_DIR)

def get_file_paths(walk: Iterator) -> list[str]:
    result = []
    for root, dirs, files in walk:
        for file in files:
            result.append(fr"{root}\{file}")
    return result

paths = get_file_paths(directory_walk)


# with open(r"C:\Users\Mourn\my_project\markdown_finder\readmes", "w") as file:
#     for path in paths:
#         file_name = path.split("\\")[-1]
#         if "readme" in file_name and "python_samples_google" not in path[0]:
#             output = fr"[{file_name}]({path})"
#             print(output, file=file)

# TODO sort by root
files = []
# {
# "fileName": {
# "day": num
#   }
# }
for path in paths:
    file_name = path.split("\\")[-1]
    parent_dir = path.split("\\")[-2]
    if "readme" in file_name and "python_samples_google" not in path[0]:
        day_number = re.search(r"\d+", parent_dir)
        if day_number is None:
            print(file_name)
            print(parent_dir)
            print(path)
        else:
            entry = {
                file_name: {
                    "day": day_number.group(0),
                    "parent": parent_dir
                }
            }
            files.append(entry)

sorted_list = sorted(files, key = lambda d: int([i for i in d.items()][0][1]['day']))
pprint(sorted_list, indent=2)
first = files[0]