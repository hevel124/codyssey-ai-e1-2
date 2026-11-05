# 나만의 퀴즈 게임

MENU_LINE = "=" * 40

class Quiz:
    """퀴즈 1개(문제, 선택지 4개, 정답 번호)를 표현한다."""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, number):
        """[문제 N] 형식으로 문제와 선택지를 출력한다."""
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")
        print()

    def is_correct(self, user_answer):
        """입력한 번호가 정답 번호와 같으면 True를 돌려준다."""
        return user_answer == self.answer


def make_default_quizzes():
    """기본 퀴즈 6개(주제: e1-1 개발 환경 미션)를 Quiz 객체 리스트로 만든다."""
    return [
        Quiz("현재 위치가 /home/test/practice일 때 ../note.txt가 가리키는 절대 경로는?",
             ["/home/test/practice/note.txt", "/home/test/note.txt", "/home/note.txt", "/note.txt"], 2),
        Quiz("파일 권한 755를 문자로 바꾸면?",
             ["rw-r--r--", "rwx------", "rwxr-xr-x", "rwxrwxrwx"], 3),
        Quiz("docker build -t e1-1-web:1.0 . 에서 -t의 역할은?",
             ["포트를 연결한다", "백그라운드로 실행한다", "볼륨을 연결한다", "이미지 이름과 태그를 지정한다"], 4),
        Quiz("docker run -p 8090:80 에서 8090은 무엇의 포트인가?",
             ["내 컴퓨터(호스트)", "컨테이너", "Docker 볼륨", "GitHub 서버"], 1),
        Quiz("컨테이너를 삭제해도 데이터가 남도록 Docker가 컨테이너 바깥에 관리하는 저장 공간은?",
             ["이미지 태그", "포트 매핑", "볼륨", "네트워크 네임스페이스"], 3),
        Quiz("내 컴퓨터에서 만든 커밋을 GitHub에 올리는 명령은?",
             ["git commit", "git init", "git clone", "git push"], 4),
    ]



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
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 입력이 중단되어 게임을 종료합니다.")