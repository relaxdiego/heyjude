from textwrap import dedent
from time import sleep

from aircraft import Plan


def main():
    song={
        verse1_line1: {
            "next": verse1_line2
        },
        verse1_line2: {
            "next": verse1_line3
        },
        verse1_line3: {
            "next": endpoint
        },
        endpoint: {}
    }


    p = Plan(
        api_version="plan/v1beta1",
        start_at=verse1_line1,
        rules=song
    )
    p.execute()


def verse1_line1(last_line):
    printverse("Hey Jude, don't make it bad")

    if not last_line:
        last_line = {"verse": 1, "line": 1}
    return ["next", last_line]


def verse1_line2(last_line):
    printverse("Take a sad song and make it better")

    last_line = {"verse": 1, "line": 2}
    return ["next", last_line]


def verse1_line3(last_line):
    printverse("Remember to let her into your heart")

    last_line = {"verse": 1, "line": 3}
    return ["next", last_line]


def endpoint(last_line):
    print("last line was: {}".format(last_line))
    return ["__done__", None]


def printverse(lyrics):
    print(lyrics)
    sleep(2)


if __name__ == "__main__":
    main()
