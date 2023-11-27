FILE_NAME: str = "encrypted.txt"
SEP = "\\"

def ngramDistribution(n: int, text: list[str] | str, space_code: str) -> list:
    nChars = len(text)
    ngramDistribution = {}
    for i in range(nChars-n):
        isSpace = False
        for j in range(n):
            if text[i+j] == space_code:
                isSpace = True
                break
        if not isSpace:
            ngram = tuple(text[i+j] for j in range(n))
            if ngramDistribution.get(ngram) is not None:
                ngramDistribution[ngram] += 1
            else:
                ngramDistribution[ngram] = 1
        
    return sorted(ngramDistribution.items(), key = lambda prob: prob[1], reverse=True)


def main() -> None:
    charDistribution = []
    characters = []
    space_code =  None
    
    print(f"Reading file {FILE_NAME}...")
    
    with open(FILE_NAME) as f:
        raw_text = f.read().strip()
    
    if SEP:
        text = raw_text.split(SEP)
    else:
        text = raw_text
    
    nChars = len(text)
    
    for char in text:
        if char and char not in characters:
            prob = round(text.count(char) * (1/nChars), 3)
            characters.append(char)
            charDistribution.append((char, prob))
    
    charDistribution = sorted(charDistribution, key = lambda prob: prob[1], reverse=True)
    space_code = charDistribution[0][0]
    
    bigramDistribution = ngramDistribution(2, text, space_code)
    trigramDistribution = ngramDistribution(3, text, space_code)
    quadrigramDistribution = ngramDistribution(4, text, space_code)
    
    print("Character Distribution: ")
    [print(char) for char in charDistribution[:5]]

    print(f"\n\n(n-gram distributions exclude suspected space code - {space_code})")

    print("\nBigram Distribution: ")
    [print(bigram) for bigram in bigramDistribution[:5]]

    print("\nTrigram Distribution: ")
    [print(trigram) for trigram in trigramDistribution[:5]]

    print("\nQuadrigram Distribution: ")
    [print(quadrigram) for quadrigram in quadrigramDistribution[:5]]

main()