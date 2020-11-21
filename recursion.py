
def fibonnaci(n):
    
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    
    if s1 == '' and s2 == '':
        return 0
    elif ord(s1[0]) > ord(s2[0]):
        return 0 + ord(s1[0])
    elif ord(s1[0]) < ord(s2[0]):
        return 0 - ord(s2[0])
    elif s1[1:2] == '' and not s2[1:2] == '':
        return 0 - ord(s2[0])
    elif s2[1:2] == '' and not s1[1:2] == '':
        return 0 + ord(s1[0])
    elif s1[1:2] == '' and s2[1:2] == '':
        return 0
    else:
        return compareTo(s1[1:], s2[1:])

#print (fibonnaci(9))