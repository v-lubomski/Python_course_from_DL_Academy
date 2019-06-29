import os

path = os.path.join('secondfolder', 'text.txt')
file = open(path, 'r', encoding='UTF-8')

print(file.readlines())
file.close()

file = open(path, 'a', encoding='UTF-8')
file.write('\nNew line')
file.close()

with open(path, 'r', encoding='UTF-8') as f:
    print(f.readlines())
