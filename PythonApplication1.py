def readFile(file_name):
    f = open(file_name, encoding = 'UTF-8')
    return  f.read().split('\n')
    f.close()
    


all_files = {'1.txt': readFile('1.txt'), '2.txt': readFile('2.txt'), '3.txt': readFile('3.txt')}
all_files = sorted(all_files.items(), key = lambda item: len(item[1]))

for file in all_files:
    print(file[0], '\n', len(file[1]))
    for text in file[1]:
        print(text)


