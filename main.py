# 나만의 퀴즈 게임

MENU_LINE = "=" * 40

def show_menu():
    """메뉴 화면을 출력한다."""
    print(MENU_LINE)
    print("        🎯 나만의 퀴즈 게임 🎯")
    print(MENU_LINE)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print(MENU_LINE)

def read_number(prompt, min_value, max_value):
    """min_value~max_value 사이의 숫자를 받을 때까지 다시 묻는다."""
    error_message = f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요."
    while True:
        text = input(prompt).strip()
        if text == "":
            print(error_message)
            continue
        try:
            number = int(text)
        except ValueError:
            print(error_message)
            continue
        if min_value <= number <= max_value:
            return number
        print(error_message)

def main():
    """메뉴를 보여 주고, 고른 번호에 맞는 화면을 실행한다."""
    while True:
        show_menu()
        choice = read_number("선택: ", 1, 5)
        if choice == 1:
            print("\n📝 퀴즈 풀기 화면입니다. (준비 중)\n")
        elif choice == 2:
            print("\n📌 퀴즈 추가 화면입니다. (준비 중)\n")
        elif choice == 3:
            print("\n📋 퀴즈 목록 화면입니다. (준비 중)\n")
        elif choice == 4:
            print("\n🏆 점수 확인 화면입니다. (준비 중)\n")
        else:
            print("\n👋 게임을 종료합니다.")
            break

# python3.13 main.py처럼 이 파일을 직접 실행 시 main() 호출
if __name__ == "__main__":
    main()