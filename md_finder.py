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

def compose_file_data(paths: list[str]) -> list[dict]:
    files = []
    for path in paths:
        file_name = path.split("\\")[-1]
        parent_dir = path.split("\\")[-2]

        if "readme" in file_name and "python_samples_google" not in path[0]:
            day_number = re.findall(r"\d+(?!])", path)
            if not day_number:
                print(file_name)
                print(path)
            else:
                entry = {
                    file_name: {
                        "day": day_number[-1],
                        "path": path
                    }
                }
                files.append(entry)
    return files


def make_file(data: list[dict]) -> None:
    for dict in data:
        file_name = [k for k in dict.keys()][0]
        day = dict[file_name]["day"]
        path = dict[file_name]["path"]
        link_text = f"Day {day}: {file_name}"
        with open(r"C:\Users\Mourn\my_project\markdown_finder\readmes", "a") as file:
            output = fr"[{link_text}]({path})"
            print(output, file=file)


paths = get_file_paths(directory_walk)
file_data = compose_file_data(paths)


sorted_file_data = sorted(file_data, key = lambda d: int([i for i in d.items()][0][1]['day']))
# pprint(sorted_file_data, indent=2)
make_file(sorted_file_data)


