def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "0으로 나눌 수 없습니다."
        else:
            return a / b
    else:
        return "지원되지 않는 연산자입니다."

def main():
    # 사용자로부터 두 정수와 연산자를 입력 받습니다.
    a = int(input("첫 번째 정수를 입력하세요: "))
    b = int(input("두 번째 정수를 입력하세요: "))
    operator = input("연산자(+, -, *, /)를 입력하세요: ")

    # 결과를 계산하고 출력합니다.
    result = calculate(a, b, operator)
    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()
