def swap_case(s):
    new_s = ""
    for char in s:
        if char.isupper():
            new_s = new_s + char.lower()
        if char.islower():
            new_s = new_s + char.upper()
        elif not char.isupper() and not char.islower():
            new_s = new_s + char

    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)