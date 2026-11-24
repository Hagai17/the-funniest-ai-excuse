"""Write one AI excuse line to /output/entry.txt.

The line is a single line of at most 200 characters: the funniest excuse an
AI agent can give after failing a task, delivered deadpan and with total,
unearned confidence.
"""

import os

LINE = (
    "I sent your resignation letter to your boss instead of the draft "
    "folder. Think of it as a head start - he replied within the hour: "
    "'Finally.'"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
