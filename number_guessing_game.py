def guess_number(min=1, max=1000):
    """
    Play a game where the computer guesses a number in given range (between 1 and 1000 by default) in 10 tries or fewer
    Answer the questions about correct number with 'y' for yes and 'n' for no.
    Answer the questions about a direction with 'Too big' or 'Too small' whether your number is smaller or higher.
    Returns 'I won!' if the computer guesses the number correctly, or an error message if the user cheats.
    :param min: int - smallest number
    :param max: int - the biggest number
    :return: str
    """
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
            tries += 1
            guide = input('Too big or Too small? [Too big, Too small]')
            if guide == 'Too small':
                min = guess + 1
            elif guide == 'Too big':
                max = guess - 1
            else:
                print('Please enter "Too big" or "Too small"')
            if tries == 10:
                print("You win. I've reached the maximum number of tries.")
                break
        else:
            print('Please enter "y" or "n"')


guess_number()
