# alphabet + 5 num +3
dictt = {"a": "e", "A": "E", ' ': ' ',
         "b": "f", "B": "F", '1': '3',
         'c': 'g',
         'x': 'b', 'X': 'B',
         'y': 'c', 'Y': 'C',
         'z': 'd', 'Z': 'D',

         ';': ';',
         ':': ':',
         '!': '!',
         '@': '@',
         '#': '#',
         '%': '%', 'C': 'G', '2': '4',
         'd': 'h', 'D': 'H', '3': '5',
         'e': 'i', 'E': 'I', '4': '6',
         'f': 'j', 'F': 'J', '5': '7',
         'g': 'k', 'G': 'K', '6': '8',
         'h': 'l', 'H': 'L', '7': '9',
         'i': 'm', 'I': 'M', '8': '0',
         'j': 'n', 'v': 'z', 'V': 'Z',
         'w': 'a', 'W': 'A',
         '*': '*',
         '&': '&',
         '-': '-',
         '+': '+',
         '=': '=',
         '/': '/',
         '?': '?',
         "'": "'",
         '''"''': '''"''', 'J': 'N', '9': '1',
         'k': 'o', 'K': 'O', '0': '2',
         'l': 'p', 'L': 'P', '.': '.',
         'm': 'q', 'M': 'Q', ',': ',',
         'n': 'r', 'N': 'R',
         'o': 's', 'O': 'S',
         'p': 't', 'P': 'T',
         'q': 'u', 'Q': 'U',
         'r': 'v', 'R': 'V',
         's': 'w', 'S': 'W',
         't': 'x', 'T': 'X',
         'u': 'y', 'U': 'Y',
         '\n': '\n'
         }
enc = ""
decdict = dict()
for key in dictt:
    val = dictt[key]
    decdict[val] = key
# a = input()
with open("test.sani", "r") as wri:
    a = wri.read()
for i in range(len(a)):
    print(decdict[a[i]], end="")
    enc=enc+decdict[a[i]]
with open("decode.sani", "a") as wri:
    wri.write(enc + '\n')
