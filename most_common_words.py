import sys
from collections import Counter

try:
    num_words = int(sys.argv[1])
except:
    print("usage: most_common_words.py num_words")
    sys.exit(1)

counter = Counter(word.lower() for line in sys.stdin
                                for word in line.strip().split()#맨앞 맨뒤 whitespace 제거 -> 중간중간 whitespace로 나누기
                                if word())

for word,count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")


def get_domain(email_address: str)-> str:
    return email_address.lower().split("@")[-1]

with open('email_addresses.txt','r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)