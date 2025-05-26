import sys
from collections import Counter



words=[]
for line in sys.stdin:
    line=line.strip()
    if line:
        words.extend(line.split())

word_counts=Counter( word.lower() for word in words)

print(len(word_counts))

sorted_words =sorted(word_counts.items(),key=lambda x:(-x[1],x[0]))
for word,count in sorted_words[:5]:
    print(f"{word}:{count}")

