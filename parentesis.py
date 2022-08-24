def ChechParentesis(string):
    stack = []
    openers = ["(", "[", "{"]
    closers = [")", "]", "}"] 
    for char in string:
        if (char in openers):
            stack.append(char)
        if(char in closers):
            index_closer = closers.index(char)
            c = stack.pop()
            index_opener = openers.index(c)
            if index_closer != index_opener:
                return False
    if stack:
        return False
    else:
        return True

string1 = "([fd{ff}df])" # true
string2 = "([[fa{ew}rewr])" #false
string3 = "([[{adsf} +dfasdf {}] () ])" #True
string4 = "([[rtg{} sg+ {}grew) () ])" #false


print(ChechParentesis(string1))
print(ChechParentesis(string2))
print(ChechParentesis(string3))
print(ChechParentesis(string4))


