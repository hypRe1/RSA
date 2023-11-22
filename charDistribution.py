import matplotlib.pyplot as plt
import numpy as np

FILE_NAME: str = "secret.txt"
SHOW_GRAPH: bool = True
SHOW_CHARS: bool = True

def main() -> None:
    distribution = []
    characters = []
    
    print(f"Reading file {FILE_NAME}...")
    
    with open(FILE_NAME) as f:
        text = f.read().strip().split("\\")
    
    nChars = len(text)
    
    print("Creating character distribution... ")
    
    for char in text:
        if char and char not in characters:
            prob = text.count(char) * (1/nChars)
            characters.append(char)
            distribution.append((char, prob))
    
    distribution = sorted(distribution, key = lambda prob: prob[1], reverse=True)
    
    print(distribution)
    
    if SHOW_GRAPH:
        print("Visualising distribution")
        
        if SHOW_CHARS:
            x = np.array(list(char for char in distribution))
        else:
            x = np.array(list(i for i in range(len(distribution))))
            
        y = np.array(list(char[1] for char in distribution))

        plt.bar(x,y)
        plt.show()

main()