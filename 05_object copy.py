# 정수 (int) count 변수 만들기
count = 5  # int
# 실수 (float) temp 변수 만들기
temp = 55.5  # float
# 문자열 (str) name 변수 만들기
name = "사과"  # str
# 불린(bool) is_ok 변수 만들기
is_ok = True  # bool

print(count, temp, name, is_ok)

# ================================

# count 의 자료형 확인
print(type(count))
# temp 의 자료형 확인
print(type(temp))
# name 의 자료형 확인
print(type(name))
# is_ok 의 자료형 확인
print(type(is_ok))

# ================================

# 100의 자료형 예측하여 주석으로 작성하기
# 100의 자료형은 # int
print(type(100))

# 100.0의 자료형 예측하여 주석으로 작성하기
# 100.0의 자료형은 # float
print(type(100.0))

# "100"의 자료형 예측하여 주석으로 작성하기
# "100"의 자료형은 # str
print(type("100"))

# type()으로 셋 다 채점하기
# 셋다 예측한 결과 값 확인

# ================================

# 진짜 숫자끼리 더하기
print(3 + 5)  # 8
# 글자 숫자끼리 더하기
print("3" + "5")  # 35
# 두자리 글자 숫자끼리 더하기
print("10" + "20")  # 1020

# 두 결과의 차이 확인하기
# 숫자끼리 더하기는 계산이고, 글자 더하기는 이어붙어짐

# ================================

# 3이 2보다 큰지 주석으로 작성 후 결과 출력해보기
print(3 > 2)  # true
# 5 와 5가 같은지 결과 출력해보기
print(5 == 5)  # true
# 값을 비교하는 type의 자료형 출력하기
print(type(3 > 2))  # bool

# ================================

# 정수 변수를 선언하고, 자료형 출력하기
count = 3
print(count, type(count))
# 정수를 실수로 값을 재할당하여 자료형 출력하기
count = 3.0
print(count, type(count))
# 숫자를 글자로 값을 재할당하여 자료형 출력하기
count = "3.0"
print(count, type(count))

# ================================

# device_temp 변수 선언하기
device_temp = 50
print(device_temp, type(device_temp))
# check_count 변수 선언하기
check_count = 58.0
print(check_count, type(check_count))
# device_name 변수 선언하기
device_name = "센서A"
print(device_name, type(device_name))
# is_normal 변수 선언하기
is_normal = True
print(is_normal, type(is_normal))
