
#problem 4 most frequent word

import sys

filename = sys.argv[1]

with open(filename,'r') as f:
    wordlist = f.read()
f.close()

wordlist = wordlist.split()

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


freqdict = wordListToFreqDict(wordlist)

sorteddict = sortFreqDict(freqdict) 

with open("popular_words.txt",'w') as f:
        f.write('(\'freq\', \'word\')')
        f.write('\n')
f.close()
most_used_words = sorteddict[0:20]

for s in most_used_words:
    with open("popular_words.txt",'a') as f:
        f.write(str(s))
        f.write('\n')
    
f.close()
