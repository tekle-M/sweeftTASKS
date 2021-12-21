n=int(input('enter n - number of words: '))
words=[input().strip() for _ in range(n)]
word_occurrence={}

for w in words:
	if w in word_occurrence:
		word_occurrence[w]+=1
	else: word_occurrence[w]=1

print(len(words))
print(' '.join([str(w) for w in word_occurrence.values()]))
