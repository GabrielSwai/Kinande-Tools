# Simple script that returns surface tones given a romanized phrase.
# E.g. "Tukándisyá tasáta kwȇ?" -> "L-H-L-H L-H-L HL"

H_VOWEL_LIST = ["á", "é", "í", "ó", "ú"]
L_VOWEL_LIST = ["a", "e", "i", "o", "u"]
F_VOWEL_LIST = ["â", "ê", "î", "ô", "û", "ȃ", "ȇ", "ȋ", "ȏ", "ȗ"]

def parse(phrase):
    result = ""

    for char in phrase:
        if char == " ":
            result = result[0:len(result)-1]
            result += " "
        for vowel in H_VOWEL_LIST:
            if char == vowel:
                result += "H-"
        for vowel in L_VOWEL_LIST:
            if char == vowel:
                result += "L-"
        for vowel in F_VOWEL_LIST:  
            if char == vowel:
                result += "HL-"

    result = result[0:len(result)-1]

    return result

if __name__ == "__main__":
    phrase = input("Kinande phrase: ")
    
    print(parse(phrase))