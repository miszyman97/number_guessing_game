def guess_number(min=1, max=1000):
    tries = 0
    while True:
        guess = (min + max) // 2
        answer = input(f'My guess is {guess}. Did i guess correctly? (yes[y]/no[n]) ').lower()
        if answer not in ('y', 'n'):
            print("Please answer with: 'y' for Yes or 'n' for No")
            continue
        elif answer == 'y':
            tries += 1
            print(f'I win! Took me {tries} tries to guess')
            break
        elif answer == 'n':
            guide = input('Too big or Too small? [Too big, Too small]')
            if guide == 'Too small':
                tries += 1
                min = guess + 1
            elif guide == 'Too big':
                tries += 1
                max = guess - 1
            else:
                print('Please enter "Too big" or "Too small"')
            if tries == 10:
                print("You win. I've reached the maximum number of tries.")
                break
        else:
            print('Please enter "y" or "n"')


guess_number()
