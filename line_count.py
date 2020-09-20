import sys

count = 0
for line in sys.stdin:
    count+=1

print(count)



# cat SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
# 이게 실행 방법 -> "|" 파이프 기호는 좌측 출력값을 우측 입력값으로 넣어줘라