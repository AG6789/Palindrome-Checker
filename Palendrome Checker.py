#palendrome checker
import string
word = input("Give me a word, I shall check if 'tis a palendrome. ").translate({ord(c): None for c in string.whitespace})
string = []
b = len(word)
x=1
while b >= x:
    v = word[b-x]
    string.append(v)
    x+=1
ulta = (''.join(string))
if ulta == word:
    print("\n") 
    print("Thy word hath the properties of le palendrome.")
else:
    print("\n") 
    print("Thy word is not worthy of le palendrome.")