def missingCharacters(s):
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
               'u', 'v', 'w', 'x', 'y', 'z'}
    num_input = set()
    letters_input = set()

    for _ in s:
        num_input.add(int(_)) if _.isdigit() else letters_input.add(_)
    num_output = sorted(numbers.difference(num_input))
    letter_output = sorted(letters.difference(letters_input))

    output = ''
    for v in num_output:
        output += str(v)
    for v in letter_output:
        output += v

    return output

print(missingCharacters('7985interdisciplinary12'))