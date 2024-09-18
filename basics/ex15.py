#count lower and upper case characters in a line

def case_checker(line):
    lower_count = sum(+1 for char in line if char.islower())  
    # Count lowercase letters
    upper_count = sum(+1 for char in line if char.isupper())  
    # Count uppercase letters
    misc_count = len(line) - (lower_count + upper_count)     
    # Count miscellaneous characters

    print(f"Lower case letters: {lower_count}")
    print(f"Upper case letters: {upper_count}")
    print(f"Miscellaneous characters: {misc_count}")

# Test the function with an example input
case_checker("Hey, hello there")


        