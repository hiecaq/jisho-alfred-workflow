#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import unicodedata

import requests

OUTPUT = """{{
    "items": [
        {{
            "uid": "{0}",
            "title": "{1}",
            "subtitle": "Title",
            "arg": "{2}"
        }},
        {{
            "uid": "lower",
            "title": "another test",
            "subtitle": "Lower",
            "arg": "another test"
        }},
        {{
            "uid": "upper",
            "title": "ANOTHER TEST",
            "subtitle": "Upper",
            "arg": "ANOTHER TEST"
        }}
    ]
}}
""".format(sys.version_info, sys.version_info, sys.version_info)

# necessary to make sure the input is not in KFKD form
input_string = unicodedata.normalize("NFKC", " ".join(sys.argv[1:]))
r = requests.get(
    f"http://beta.jisho.org/api/v1/search/words",
    params={"keyword": input_string}
)
r.raise_for_status()
output = json.loads(r.text)


def get_name(item):
    return (
        item["japanese"][0]["word"]
        if "word" in item["japanese"][0] else item["japanese"][0]["reading"]
    )


data = [{
    "uid":
        get_name(item),
    "title":
        get_name(item),
    "subtitle":
        item["japanese"][0]["reading"]
        if "reading" in item["japanese"][0] else "",
    "variables": {
        "definition":
            "\n"
            .join([";".join(x["english_definitions"]) for x in item["senses"]])
    },
    "arg":
        "https://jisho.org/search?utf8=%E2%9C%93&keyword=" + (
            item["japanese"][0]["word"] if "word" in item["japanese"][0] else
            item["japanese"][0]["reading"]
        )
} for item in output["data"][:10]]

print(json.dumps({"items": data}))
