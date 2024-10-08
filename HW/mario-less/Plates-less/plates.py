def is_valid(s):
    """
    Tests to make sure Vanity Plate follows rules to be valid:
    - All vanity plates must start with at least two letters.
    - vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    - Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable Passenger vanity plate; AAA22A would not be acceptable. The first number used cannot be a "0".
    - No periods, spaces, or punctuation marks are allowed.
    """
    if len(s) < 2 or len(s) > 6:
        return False
    
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    found_number = False

    for i in range (len(s)):
        if s[i].isdigit():
            if s[i] == "0"  and not found_number:
                return False
            found_number = True

        elif found_number:
            return False
        
        if not s[i].isalnum():
            return False 
        
    return True

def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


main()