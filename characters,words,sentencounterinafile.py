from asyncore import read
g= open("abc.txt","r")
s = g.read()
k = 0
sentences = s.count('\n')
words = s.count(' ')
for i in s: 
    k = k+1
print('sentences in file are',sentences+1)
print('words in file are',sentences + words + 1)
print('words in file are',k - sentences)
g.close()

