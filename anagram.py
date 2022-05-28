# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(own, won):
    # [assignment] Add your code here
    if (sorted(own) == sorted(won)):
        answer = True
    else:
        answer = False
    print (answer)

            

strl = input("put in the first word: ")
strl = input("put in the second word: ")
find_anagram(strl, strl)

