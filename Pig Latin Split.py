def first_vowel(word):
    count = 0
    for i in word:
        if i in "AEIOUaeiou":
            return count
        count += 1
    return -1


def piglatin(word):
    if word[0] in "AEIOUaeiou":
        latin = word + "way"
    else:
        vowel = first_vowel(word)
        first = word[ :vowel]
        pig = word[vowel: ]
        latin = pig + first + "ay"
    return latin

def piglatin_sentence(word):
    words = word.split()
    
    for i in words:
        print(piglatin(i), end=" ")

piglatin_sentence("Hello how are you")