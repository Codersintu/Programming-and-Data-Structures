from collections import Counter
freq = Counter("tree")

sorted_chars=sorted(freq.items(),key=lambda x:x[1],reverse=True)
print(sorted_chars)