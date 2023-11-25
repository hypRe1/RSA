from typing import Optional


FILE_NAME: str = "encrypted.txt"
OUTPUT_FILE: str = "revealed.txt"
SEPARATOR: Optional[str] = "\\"  # Set to None for normal text


def main() -> None:
    replace_dict = {
        "70879": " ",  
        "1518473": "e",
        "1797": "t",
        "1150197": "h",
        "1713388": "r"
    }
    
    print(f"Reading file {FILE_NAME}")
    
    with open(FILE_NAME) as f:
        text = f.read().strip()
    
    if SEPARATOR:
        text = text.split(SEPARATOR)
    
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