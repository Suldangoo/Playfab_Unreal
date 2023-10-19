from datetime import datetime

def calculate_age(birth_date, base_date):
    # 생년월일을 연, 월, 일로 분리합니다.
    birth_year, birth_month, birth_day = map(int, birth_date.split('-'))
    base_year, base_month, base_day = map(int, base_date.split('-'))

    # 만 나이를 계산합니다.
    age = base_year - birth_year
    if (base_month, base_day) < (birth_month, birth_day):
        age -= 1

    return age

def main():
    # 사용자로부터 생년월일과 기준 생년월일을 입력받습니다.
    birth_date = input("당신의 생년월일을 yyyy-mm-dd 형식으로 입력하세요: ")
    base_date = input("만 나이를 알고 싶은 기준 생년월일을 yyyy-mm-dd 형식으로 입력하세요: ")

    # 만 나이를 계산하고 출력합니다.
    age = calculate_age(birth_date, base_date)
    print(f"기준 날짜 {base_date}에서 당신의 만 나이는 {age}세입니다.")

if __name__ == "__main__":
    main()
