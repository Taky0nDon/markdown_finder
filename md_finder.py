import os
import shutil
from typing import Iterator
import re
from pprint import pprint

DEFAULT_DIR = r"C:\users\mourn\100_days_of_code"
OBSIDIAN_DIR = r"C:\Users\Mourn\Documents\100 Days of Code\Directory"
PROJECT_DIR = r"C:\Users\Mourn\my_project\markdown_finder"


def copy_file_to_obsidian_folder(file_data: list[dict], dest: str = r"C:\Users\Mourn\Documents\100 Days of Code\Directory") -> None:
    for file in file_data:
        name = [k for k in file.keys()][0]
        extension = name.split(".")[-1]
        if extension in ["md"]:
            path = file[name]["path"]
            day = file[name]["day"]
            prefix = fr"Day {day} - "
            destination = fr"{dest}\{prefix}{name}"
            print(f"Copying {path}... to {destination}")
            shutil.copy2(src=path, dst=destination)

def get_file_paths(walk: Iterator) -> list[str]:
    result = []
    for root, dirs, files in walk:
        for file in files:
            result.append(fr"{root}\{file}")
    return result

def compose_file_data(paths: list[str]) -> list[dict]:
    files = []
    excluded = ["python_samples_google",
                "venv",
                "Lib"]
    for path in paths:
        file_name = path.split("\\")[-1]
        parent_dir = path.split("\\")[-2]
        extension = file_name.split(".")[-1]
        if any([e in path for e in excluded]):
            continue
        if "readme" in file_name.lower():
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
    with open(r"C:\Users\Mourn\my_project\markdown_finder\readmes", "a") as file:
        for dict in data:
            file_name = [k for k in dict.keys()][0]
            day = dict[file_name]["day"]
            path = dict[file_name]["path"]
            link_text = f"Day {day}: {file_name}"
            output = fr"[{link_text}]({path})"
            print(output, file=file)

directory_walk = os.walk(OBSIDIAN_DIR)
paths = get_file_paths(directory_walk)
file_data = compose_file_data(paths)
sorted_file_data = sorted(file_data, key = lambda d: int([i for i in d.items()][0][1]['day']))
make_file(sorted_file_data)
# copy_file_to_obsidian_folder(sorted_file_data)

