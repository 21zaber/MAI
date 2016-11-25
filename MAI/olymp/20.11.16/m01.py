#!/usr/bin/python3.5

conv = {'.-':'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z'}

while True:
    try: 
        s = input()
    except:
        break

    words = s.split('//')
    for w in words:
        letters = [conv[i] for i in w.split('/')]
        print(''.join(letters), end='')
        print(' ', end = '')

    print()
