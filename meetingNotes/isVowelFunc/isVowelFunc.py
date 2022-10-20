# James Taddei
# isVowel Function
# 10/19/22

def main():
    curr = isVowel("a")
    print(f"'a': {curr}")
    curr = isVowel("O")
    print(f"'O': {curr}")
    curr = isVowel("k")
    print(f"'k': {curr}")
    curr = isVowel("ae")
    print(f"'ae': {curr}")
    curr = isVowel("8")
    print(f"'8': {curr}")

def isVowel(string: str) -> bool:
    """
    Reuturns a bool of whether or not the string is vowel.
    """
    string = string.lower() # Accounts for uppercase vowels
    return (string == "a") or (string == "e") or (string == "i") or (string == "o") or (string == "u")

main()