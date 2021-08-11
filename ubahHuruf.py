vowel = ['a','i','u','e','o']
kata = 'i love Javascript'
s = ""

for i in kata:
    if (i in vowel):
        s += '$'
    else:
        s += i
print(s)