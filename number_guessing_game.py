def guess_number(min=1, max=1000):
    tries = 0
    while True:
        guess = (min + max) // 2
        answer = input(f'My guess is {guess}. Did i guess correctly? (yes[y]/no[n]) ')
        tries += 1
        if answer == 'y':
            print(f'I win! Took me {tries} tries to guess')
            break


guess_number()