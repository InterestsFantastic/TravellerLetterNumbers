'''This module handles a d66 roll, conversion of numbers to Traveller
letternumbers and back, and generates random character stats, returning
a list or a string, depending on your preference.'''

# Python 3.x

from random import randint

letternumbers = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'

def rd6():
    return randint(1,6)

def r2d6():
    return rd6() + rd6()

def rd66():
    return rd6() * 10 + rd6()

def letter_to_number(letter):
    '''Returns the number corresponding to a Traveller numberletter.
    This includes 0 through 9.'''
    assert len(letter) == 1, 'Single letter required.'
    letter = letter.upper()
    out = letternumbers.find(letter)
    assert out != -1, 'Unknown character requested for translation.'
    return out

def number_to_letter(num):
    return letternumbers[num]

def numbers_to_letters(numbers):
    '''Returns a string of all numbers converted to characters.'''
    out = ''
    for n in map(number_to_letter, numbers):
        out += n
    return out
    
def chargen():
    '''Returns list of six random 2d6 rolls.'''
    stats = []
    for x in range(6):
        stats.append(r2d6())
    return stats

def chargen_str():
    '''Returns string of Traveller letternumbers for six 2d6 rolls.'''
    return numbers_to_letters(chargen())


def test():
    for x in range(50):
        print(rd66(), end=', ')
    print()

    print(number_to_letter(10))
    print(number_to_letter(12))
    print(number_to_letter(20))
    print(number_to_letter(33))
    print(letter_to_number('z'))
    
    print(letter_to_number('a'))

    print(chargen())
    print(chargen_str())

if __name__ == '__main__':
    test()
