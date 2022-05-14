#ver 2.0
import itertools

print("╔═══╗╔══╗╔══╗╔══╗╔═══╗╔═══╗╔╗ ╔╗")
print("║╔═╗║║╔╗║║╔═╝║╔═╝║╔══╝║╔══╝║╚═╝║")
print("║╚═╝║║╚╝║║╚═╗║╚═╗║║╔═╗║╚══╗║╔╗ ║")
print("║╔══╝║╔╗║╚═╗║╚═╗║║║╚╗║║╔══╝║║╚╗║")
print("║║   ║║║║╔═╝║╔═╝║║╚═╝║║╚══╗║║ ║║")
print("╚╝   ╚╝╚╝╚══╝╚══╝╚═══╝╚═══╝╚╝ ╚╝")

def split(s):
    return [char for char in password]

password = str(input('pass: '))
tailpass = str(input('tail-pass: '))
MyList = [password]
lenght = len(password)

NewPass = split(password)

def rSubset(NewPass):
    return list(itertools.permutations(NewPass))
    
f = open('file.txt', 'w')

for i in NewPass:
    line = ' '.join(str(x) for x in i)
    line = line + tailpass
    f.write(line + '\n')
f.close()
