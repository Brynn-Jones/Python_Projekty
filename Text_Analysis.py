users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
text1 = '''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.'''
text2 = '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.'''
text3 = '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
texts = [text1, text2, text3]

isOk = True

username = input('Username: ')
password = input('Password: ')

if not (username, password) in users.items():
    print(40 * '-')
    print(f'Invalid password or username.')
    print(40 * '-')
    isOk = False

if isOk == True:
    print(40 * '-')
    print(f'Welcome to the Text Analysis app, {username}!')
    print(40 * '-')
    print(f'''You can choose from the following texts:

1) {text1[:34]}...
2) {text2[:34]}...
3) {text3[:34]}...''')
    print(40 * '-')

    choice = input('Number of the chosen text: ')
    if not choice.isdigit():
        print('Error: Input has to be a number!')
        isOk = False

if isOk == True:
    n_choice = int(choice) - 1
    if not (n_choice in range(len(texts))):
        print('The text you have chosen does not exist.')
        isOk = False

if isOk == True:
    print(40 * '-')
    print(f'ANALYSIS OF TEXT NUMBER {choice}:')
    print(40 * '-')
    chosen_text = texts[n_choice]
    words = chosen_text.split()

    # odstraníme znaky .,!:? ze začátků a konců slov
    # pokud se slovo skládá pouze z těchto znaků, výsledkem je slovo s nulovou délkou
    # POZOR, zbývající kód musí s nulovými délkami počítat
    clean_words = []
    for word in words:
        clean_words.append(word.strip('.,!:?'))
    print(f'Number of words: {len(clean_words)}')

    title_words = []
    for word in clean_words:
        if word.istitle() == True:
            title_words.append(word)
    print(f'Number of titlecase words: {len(title_words)}')

    uppercase_words = []
    for word in clean_words:
        if word.isalpha() == True and word.isupper() == True:
            uppercase_words.append(word)
    print(f'Number of uppercase words: {len(uppercase_words)}')

    lowercase_words = []
    for word in clean_words:
        if word.isalpha() == True and word.islower() == True:
            lowercase_words.append(word)
    print(f'Number of lowercase words: {len(lowercase_words)}')

    numbers = []
    for word in clean_words:
        if word.isdigit() == True:
            numbers.append(int(word))
    print(f'Number of numeric strings: {len(numbers)}')

    sum_numbers = sum(numbers)
    print(f'Sum of the numbers in text: {sum_numbers}')
    print(40 * '-')

    lengths = dict()
    for word in clean_words:
        if lengths.get(len(word)) == None:
            lengths[len(word)] = 1
        else:
            lengths[len(word)] += 1

    print('LEN|     OCCURENCES     |NR.')
    print(40 * '-')
    for item in sorted(lengths):
        print(f'{item}'.rjust(3), '|', (lengths[item] * '*').ljust(20), '|', f'{lengths[item]}', sep='')
    print(40 * '-')
