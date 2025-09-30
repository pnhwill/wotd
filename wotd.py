# Word of the Day
# Will Harrington
# 29 Sep 2025

import random
from pathlib import Path

from freedictionaryapi.clients.sync_client import DictionaryApiClient

INPUT_FILE = Path(
    "/Users/will/Library/Mobile Documents/iCloud~md~obsidian/Documents/Random/words.md"
)
SECTION_SEPARATOR = "---"

if __name__ == "__main__":
    with INPUT_FILE.open() as file:
        # Skip empty lines and remove newlines
        words = list(word for word in (line.strip() for line in file) if word)
        # Only use lines in first section of document (until first "---")
        words = words[: words.index(SECTION_SEPARATOR)]

        word = random.choice(words)
        print()
        print(word)
        print()
        

        with DictionaryApiClient() as client:
            parser = client.fetch_parser(word)
            # print(parser.word.phonetics)
            for meaning in parser.word.meanings:
                print(meaning.part_of_speech)
                for definition in meaning.definitions:
                    print("-", definition.definition)
                print()
