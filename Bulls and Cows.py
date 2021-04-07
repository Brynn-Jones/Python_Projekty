import random

#constants
GREET = 'Hi there!'
DIVIDER = 47 * '-'
TEXT = '''I've generated a random 4 digit number for you.
Let's play a Bulls & Cows game.
To exit the game, type \'exit\'.'''
DIGITNUM = 4

#global variables
attempts = 0

def generate_code():
  code = [0] * DIGITNUM
  while code[0] == 0: # nesmí začínat nulou
    code = random.sample(range(0, 10), DIGITNUM) # .sample zaručí unikátnost číslic
  return code

def guess_validity(numbers: list) -> bool:
  value = True
  try:
    numbers = [int(i) for i in numbers] # integer
    if not len(numbers) == DIGITNUM:
      value = False
      print(f'Your guess must be a {DIGITNUM} digit number!')
      print(divider)
    elif numbers[0] == 0:
      value = False
      print('Your guess cannot start with a zero!')
      print(divider)
    elif len(set(numbers)) < DIGITNUM: # množina unikátních číslic
      value = False
      print(f'Your guess must include {DIGITNUM} unique digits!')
      print(divider)

  except:
    value = False
    print('Your guess must be a number!')
    print(divider)

  return value


def bulls_cows(code: list) -> bool:
  global attempts
  bulls = 0
  cows = 0

  str_guess = input('Enter your guess: ')

  if str_guess == 'exit':
    answer = str(code[0]) + str(code[1]) + str(code[2]) + str(code[3])
    print(divider)
    print(f'''I am sorry to see you go!
The secret number was {answer}.''')
    return False

  guess = list(str_guess)
  if guess_validity(guess):
    attempts += 1
    guess = [int(i) for i in guess] # již zkontrolováno

    # number of bulls
    for i in range(DIGITNUM):
      if guess[i] == code[i]:
        bulls += 1
    # number of cows
    for i in range(DIGITNUM):
      for x in range(DIGITNUM):
        if guess[i] == code[x]:
          cows += 1
    cows = cows - bulls

    if bulls == DIGITNUM: #pokud uhodnuto
      print(f'Congratulations! You\'ve guessed the correct number in {attempts} ' + ('attempt!' if attempts == 1 else 'attempts!'))
      return False

    else:
      print(f'{bulls} ' + ('bull' if bulls == 1 else 'bulls') + ', ' + f'{cows} ' + ('cow' if cows == 1 else 'cows'))
      print(DIVIDER)

  return True


def main():
  global gameEnd
  print(GREET)
  print(DIVIDER)
  print(TEXT)
  print(DIVIDER)

  secret_number = generate_code()
  while bulls_cows(secret_number):
    continue

main()