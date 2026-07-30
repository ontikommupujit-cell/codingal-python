def match_words(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            list.append(word)
    print('list of words with first and last lettter same',list)
    return ctr
count=match_words(['aba','bcb','gbg','hjh','jgj'])
print('number of words having first and last letters are',count)
    