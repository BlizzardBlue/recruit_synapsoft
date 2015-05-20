# -*- coding: utf-8 -*-
## 디버깅의 용이성을 위해 불필요한 print 문이 추가된 버전입니다.


## "합이 최소가 되는 쌍"을 만들기 위한 조건을 아래와 같이 생각해보았다.
# 1) 조합 하나를 이루는 정수들은 오름차순 정렬로 되어야 함
# 2) 단, 첫 번째 숫자는 0을 제외한 가장 낮은 수여야 함
# 3) 입력값에 0이 들어있다면 첫 번째 수 바로 다음부터 0이 들어가고, 0이 끝난 후엔 오름차순이 재개되어야 함
# 4) 만들어진 두 조합의 자릿수는 서로 같거나, 1개 차이여야 함
# 4-1) 한 조합에 낮은 숫자만 넣더라도 자릿수가 높다면 낮은 숫자는 그 역할을 하지 못하므로

# raw_input을 통해 계산에 사용될 숫자를 입력받고, 입력값에서 쉼표와 공백을 제거한다.
in_value = raw_input("input> ")
in_value = in_value.translate(None, ", ")

# 입력받은 숫자 개수가 조건을 충족하는지 확인.
count = len(in_value)
if not 1 < count < 19:
    print "error: 입력받는 숫자의 개수는 2개 이상, 18개 이하입니다. 진행을 중단합니다."
    exit()

# 입력값을 다루기 편하도록 빈 리스트를 생성하여 append(list.append)한다.
input_list = []
index = 0
while index < len(in_value):
    input_list.append(int(in_value[index:index+1]))
    index += 1

# 오름차순 정렬을 시행하여 리스트를 더욱 다루기 편하도록 만든다.
input_list.sort()

# 결과값 계산을 위한 쌍이 될 두 조합을 빈 리스트로 생성한다.
table1 = []
table2 = []


## 두 조합을 만들기 위한 흐름은 아래와 같다.
# 1) 입력값 리스트에서 '0'을 제외한 가장 낮은 숫자를 추출(list.pop)하여 '0'을 제외한 숫자가 남지 않을 때 까지 두 조합 리스트에 번갈아 append한다
# 2) 입력값 리스트에 '0'이 있을경우 이를 추출하여 '0'이 남지 않을 때 까지 두 조합 리스트 중 자릿수가 더 낮은 쪽 부터 '0'을 추출 후 번갈아 append한다
# 2-1) 두 조합 리스트의 자릿수가 같을 경우 'table1'부터 시작한다

# 입력값 리스트에 들어있는 '0'의 개수를 카운트하여 추후 처리에 용이하도록 한다.
zero = input_list.count(0)
print "zero count:", zero #[debug] 카운트된 '0' 개수 표시

# 상기한 흐름에 따라 입력값을 두 리스트로 분배하려면 총 몇 번의 분배가 이루어져야 하는지 알아둘 필요가 있다.
# n개의 숫자를 입력받고, 한 번에 하나씩 분배하려면 총 n번의 분배가 이루어져야 하므로 이 n값을 'index2'라는 변수로 생성한다.
index2 = len(in_value)
print "분배 횟수:", index2 #[debug] 분배 횟수 표시

# '0'을 제외한 정수들을 먼저 두 리스트에 append한 후, 남은 '0'값들을 조합의 두 번째 자리에 삽입(list.insert)하는 방식으로 진행된다.
# 앞서 편의를 위해 생성한 변수인 zero와 index2값의 비교를 통해 '0'값의 처리 여부를 결정할 수 있도록 하였다.
while index2 > 0:
    if index2 <= zero and zero % 2 == 1:
        table1.insert(1, 0)
        zero -= 1
        index2 -= 1
    elif index2 <= zero and zero % 2 == 0:
        table2.insert(1, 0)
        zero -= 1
        index2 -= 1
    elif index2 % 2 == 1:
        table1.append(input_list.pop(int(zero)))
        index2 -= 1
    elif index2 % 2 == 0:
        table2.append(input_list.pop(int(zero)))
        index2 -= 1
    print "-- %s번 남음 --" %(index2) #[debug] 진행 과정 표시
    print "table1:", table1 #[debug] 진행 과정 표시
    print "table2:", table2 #[debug] 진행 과정 표시


# 아래는 조합이 '0'으로만 이루어져 있을 경우 '-1'이라는 결과값을 도출하기 위한 코드이다.
# 계산에 사용되는 입력값의 개수가 2 ~ 18개로 비교적 적어 계산 프로세스가 끝난 뒤에 가용성 체크를 해도 성능 최적화의 관점에서 큰 문제가 되지 않는다고 판단하였다.
try:
    check1 = table1.index(0)
    if check1 == 0:
        print "error: 쌍을 만들 수 없습니다. 진행을 중단합니다."
        print "total: %d" % (-1)
        exit()
except ValueError:
    pass
try:
    check2 = table2.index(0)
    if check2 == 0:
        print "error: 쌍을 만들 수 없습니다. 진행을 중단합니다."
        print "total: %d" % (-1)
        exit()
except ValueError:
    pass

#결과값 계산을 위해 리스트 요소들을 순서대로 문자열로 재생성 한다.
table1_result = ''.join(str(item) for item in table1)
table2_result = ''.join(str(item) for item in table2)


## 결과값 출력
total_sum = int(table1_result) + int(table2_result)
print total_sum
