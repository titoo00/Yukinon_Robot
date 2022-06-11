from typing import List
import yaml

languages = {}
commands = {}

def get_command(value: str) -> List:
    return commands["command"][value]

def get_string(lang: str):
    return languages["en"]

commands["en"] = yaml.safe_load(
            open(r"./lang/en.yml", encoding="utf8")
        )

languages["en"] = yaml.safe_load(
            open(r"./lang/en.yml", encoding="utf8")
        )

languages["en"] = yaml.safe_load(
    open(r"./lang/en.yml", encoding="utf8")
)
for item in languages["en"]:
    if item not in languages["en"]:
        languages["en"][item] = languages["en"][item]