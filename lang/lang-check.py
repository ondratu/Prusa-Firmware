#!/usr/bin/env python3
"""Check lang files."""
from argparse import ArgumentParser
from traceback import print_exc


def check_length(text, cols, rows, lines):
    if rows == 0:
        assert len(text) <= cols, (
            "Text: %s is longer then %d on line %d" % (text, cols, lines))


def parse_txt(lang):
    if lang == "en":
        file_path = "lang_en.txt"
    else:
        file_path = "lang_en_%s.txt" % lang

    lines = 0
    with open(file_path) as src:
        while True:
            comment = src.readline().split(' ')
            source = src.readline()
            translation = src.readline()
            lines = lines + 3

            if len(comment) > 1:
                cols = int(comment[1].split('=')[1])
                rows = int(comment[2].split('=')[1])
                check_length(translation, cols, rows, lines)

            if len(src.readline()) != 1:  # empty line
                break
            lines += 1


def main():
    parser = ArgumentParser(
        description=__doc__,
        usage="$(prog)s lang")
    parser.add_argument(
        "lang", nargs='?', default="en", type=str,
        help="Check lang file (en|cs|de|es|fr|it)")

    args = parser.parse_args()
    try:
        parse_txt(args.lang)
    except Exception as exc:
        print_exc()
        parser.error("%s" % exc)
        return 1


if __name__ == "__main__":
    exit(main())
