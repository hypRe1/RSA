import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations

FILE_NAME: str = "encrypted.txt"
SHOW_GRAPH: bool = False
SHOW_CHARS: bool = False
SEP = "\\"

def main() -> None:
    distribution = []
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
    
    print("Creating character distribution... ")
    
    for char in text:
        if char and char not in characters:
            prob = round(text.count(char) * (1/nChars), 3)
            characters.append(char)
            distribution.append((char, prob))
    
    distribution = sorted(distribution, key = lambda prob: prob[1], reverse=True)
    space_code = distribution[0][0]
    print(distribution[:5])
    
    if SHOW_GRAPH:
        print("Visualising distribution")
        
        if SHOW_CHARS:
            x = np.array(list(char for char in distribution))
        else:
            x = np.array(list(i for i in range(len(distribution))))
            
        y = np.array(list(char[1] for char in distribution))

        plt.bar(x,y)
        plt.show()
    
    print("Creating ngram distribution...")
    n=3
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
        
    ngramDistribution = sorted(ngramDistribution.items(), key = lambda prob: prob[1], reverse=True)
    print(ngramDistribution[:5])

main()