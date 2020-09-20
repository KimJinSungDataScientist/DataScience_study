#egrep.py
import sys, re

# sys.argv는 커맨드 라인에서 사용할 수 있는 몯느 인자에 대한 리스트다.
# sys.argv[0]는 프로그램의 이름을 나타낸다.
# sys.argv[1]는 커맨드 라인에서 주어지는 정규표현식이다.
regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex,line):
        sys.stdout.write(line)
