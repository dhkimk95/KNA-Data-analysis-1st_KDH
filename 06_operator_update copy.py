# 두정수로 사칙연산 6종과 거듭제곱까지 결과를 모두 출력
a = 17
b = 5
print(a + b)  # 22
print(a - b)  # 12
print(a * b)  # 85
print(a / b)  # 3.4
print(a // b)  # 3
print(a % b)  # 2
print(a**b)  # 1419857

# 여러 수로 평균·정사각형 넓이·직육면체 부피를 계산
x = 80
y = 91
z = 90
print((x + y + z) / 3)
side = 7
print(side**2)
print(3 * 4 * 5)

# 비교 연산자 6종을 활용하여 임의의 값으로 비교하고 결과(True/False)를 출력
print(9 == 9)
print(9 != 9)
print(9 > 9)
print(9 < 9)
print(9 >= 9)
print(9 <= 9)

temp = 85
temp_ok = 60 <= temp and temp <= 90
print(temp_ok)
pressure = 5
press_ok = 3 <= pressure and pressure <= 7
print(press_ok)
print(temp_ok and press_ok)

stock = 100
print(stock)
stock += 50
print(stock)
stock -= 30
print(stock)
stock += 5
print(stock)

total = 500
defect = 23
print(defect / total * 100)
run_h = 21
toth = 24
print(run_h / toth * 100)

miniute = 500
print(miniute // 60)
print(miniute % 60)
