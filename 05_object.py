# int - 정수형
# 소수점 없이 딱 떨어지는 수
# 0와 음수도 정수에 포함됨
count = 3
age = 32
tall = 173
zero = 0
temp = -30

# ============================

# float - 실수
# 소수점이 붙은 숫자
# 5.0처럼 딱 떨어지는 수이지만 소수점이 있다면 무조건 float
tired = 99.999999
height = 17.2

# ============================

# str - 문자열
# 따옴표에 감싸져있는 모든 값
hello = "안녕하세요~!"
emoji = ""
empty = ""
fake_num = "12345"
fake_num2 = "5.0"
# 따옴표가 ""와'' 둘 다 사용할수 있는 이유는
# 문자열 안에 따옴표가 필요한 경우가 있기 떄문
# 이럴 경우 사용하지 않는 따옴표로 쌍을 맞춰 가장 바깥에 감싸줘야 함'
illit = "it's me"

# ============================

# bool - 불리언형
# True 또는 False만
# 첫 글자는 대문자, 따옴표 없이 작성

ok = True
no = False

# 비교할 경우 bool로 출력
print(100 < 5)  # False
print(5 == 5)  # True

# ============================

# type() 자료형 확인
# type (확인하고자 하는 것) > 입력한 것의 자료형을 알려줌

type(5)  # 터미널에서 확인 불가 > print 하지 않았기 떄문

print(type(5))
print(type("센서A"))
print(type(True))
print(type(3 > 2))
# 1. print 함수의 내부를 확인
# 2. print 함수에 또 함수가 있는 것을 확인하고 type 함수의 내부를 확인
# 3. type 함수의 내부에 연산자가 있는 것을 확인하고 연산 진행
# 4. 3 > 2의 연산 결과는 True이기 떄문에 type(True)로 바뀜
# 5. type(True)의 결과인 <class 'bool'>이 print로 인해 터미널에 출력

print(3, type(3))

num = 123
fake_num = "123"
str = "문자열"
ok = True

print(num, type(num))

# 내가 터미널에서 출력된 결과 중에서
# type()을 사용해서 출력된 자료형을 쉽게 확인 할 수 있는 방ㅂ법
print(num, ">>>>", type(num))
print("num :", type(num))
