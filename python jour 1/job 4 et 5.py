import string
def listAlphabet():
    return list(string.ascii_lowercase)[::-1]
print(listAlphabet())