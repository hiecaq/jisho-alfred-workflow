#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import unicodedata

import requests


def get_json(input_string):
    # necessary to make sure the input is not in KFKD form
    normalized = unicodedata.normalize("NFKC", input_string)
    r = requests.get(
        f"http://beta.jisho.org/api/v1/search/words",
        params={"keyword": normalized}
    )
    r.raise_for_status()
    return json.loads(r.text)


def get_name(item):
    return (
        item["japanese"][0]["word"]
        if "word" in item["japanese"][0] else item["japanese"][0]["reading"]
    )


def map_to_items(data):
    return {
        "items": [{
            "uid":
                get_name(item),
            "title":
                get_name(item),
            "subtitle":
                item["japanese"][0]["reading"]
                if "reading" in item["japanese"][0] else "",
            "variables": {
                "definition":
                    "\n\n".join([
                        ";".join(x["english_definitions"])
                        for x in item["senses"]
                    ])
            },
            "arg":
                "https://jisho.org/search?utf8=%E2%9C%93&keyword=" + (
                    item["japanese"][0]["word"]
                    if "word" in item["japanese"][0] else
                    item["japanese"][0]["reading"]
                )
        } for item in data["data"][:10]]
    }


def main():
    j = get_json(" ".join(sys.argv[1:]))
    print(json.dumps(map_to_items(j)))


if __name__ == "__main__":
    main()
