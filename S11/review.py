def contains_no_vowel(s):
    """
    Return true if there are no vowel letters, otherwise return False

    Check every letter in the string: 
        if the letter is vowel:
            return False # return will stop the function
        else:
            return
        
    """
    for letter in s: 
        if letter in "aeiou":
            return False
        else:
            return True


print(contains_no_vowel("babson")) #False
print(contains_no_vowel("bbc")) #True