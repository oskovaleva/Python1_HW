user_str = input('Input a sentence: ')
for ind, el in enumerate(user_str.split(), 1):
    print(ind, el[:10])
