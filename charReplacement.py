FILE_NAME: str = "encrypted.txt"
OUTPUT_FILE: str = "revealed.txt"
SEP: str = "\\"


def main() -> None:
    replace_dict = {
        "code": "character",  # example
    }

    print(f"Reading file {FILE_NAME}")

    with open(FILE_NAME) as f:
        text = f.read().strip().split(SEP)

    revealed_text = []
    for char in text:
        if char in replace_dict.keys():
            revealed_text.append(replace_dict[char])
        else:
            revealed_text.append("_")

    with open(OUTPUT_FILE, "w") as f:
        f.write("".join(revealed_text))

    print(f"Written to file {OUTPUT_FILE}")


main()
