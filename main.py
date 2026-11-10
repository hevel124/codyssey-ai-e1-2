# 나만의 퀴즈 게임

#list, dict를 json 글자로 바꿔 파일에 쓰는 표준 라이브러리
import json 
#파일 경로를 다루는 표준 라이브러리
from pathlib import Path


MENU_LINE = "=" * 40

#Path(__file__).parent: __file__은 지금 실행 중인 main.py의 경로이고, .parent는 그 폴더다. 어느 폴더에서 실행하든 main.py 옆(프로젝트 루트)을 가리킨다.
#/ "state.json": 폴더 경로 뒤에 파일 이름을 붙인다. Path에서 /는 나눗셈이 아니라 경로 연결이다.
STATE_FILE = Path(__file__).parent / "state.json"


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
    
    def to_dict(self):
        """state.json에 쓸 수 있게 dict로 바꿔 돌려준다."""
        return {"question": self.question, "choices": self.choices, "answer": self.answer}


def make_default_quizzes():
    """기본 퀴즈 6개(주제: 개발 환경 기초 - 터미널·Docker·Git)를 Quiz 객체 리스트로 만든다."""
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

def read_text(prompt):
    """빈 입력이 아닐 때까지 다시 묻고, 앞뒤 공백을 지운 글자를 돌려준다."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("⚠️ 빈 입력입니다. 내용을 입력하세요.")

def play_quiz(quizzes):
    """저장된 퀴즈를 차례로 출제하고, 맞힌 개수와 점수를 출력한다."""
    if not quizzes: #리스트가 비어있으면
        print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.\n")
        return
    print(f"\n📝 퀴즈를 시작합니다! (총 {len(quizzes)}문제)\n")
    correct_count = 0
    # 리스트를 숫자, 퀴즈 형태의 쌍으로 꺼내 주는 객체로 감싸고, 꺼낸 쌍을 언패킹(number, quiz)해서 대입
    for number, quiz in enumerate(quizzes, start=1):
        print("-" * 40)
        quiz.display(number)        
        user_answer = read_number("정답 입력: ", 1, 4) # 1~4 까지만 받음
        #정,오답 체크
        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!\n")
            correct_count += 1
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.\n")
    score = correct_count * 100 // len(quizzes) # 맞은 문제수 * 100 // 총 문제 수 -> // 몫만 남기는 나눗셈
    print(MENU_LINE)
    print(f"🏆 결과: {len(quizzes)}문제 중 {correct_count}문제 정답! ({score}점)")
    print(MENU_LINE)
    print()
    return score

def add_quiz(quizzes, best_score):
    """문제·선택지 4개·정답 번호를 입력받아 퀴즈를 추가하고 파일에 저장한다."""
    print("\n📌 새로운 퀴즈를 추가합니다.\n")
    question = read_text("문제를 입력하세요: ")
    choices = []
    for number in range(1, 5):
        choices.append(read_text(f"선택지 {number}: "))
    answer = read_number("정답 번호 (1-4): ", 1, 4)
    quizzes.append(Quiz(question, choices, answer))
    save_state(quizzes, best_score)
    print("\n✅ 퀴즈가 추가되었습니다!\n")

def save_state(quizzes, best_score):
    """퀴즈 목록과 최고 점수를 state.json에 UTF-8로 저장한다."""
    data = {"quizzes": [quiz.to_dict() for quiz in quizzes], "best_score": best_score}
    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def show_quizzes(quizzes):
    """저장된 퀴즈의 번호와 문제를 목록으로 출력한다."""
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.\n")
        return
    print(f"\n📋 등록된 퀴즈 목록 (총 {len(quizzes)}개)\n")
    print("-" * 40)
    for number, quiz in enumerate(quizzes, start=1):
        print(f"[{number}] {quiz.question}")
    print("-" * 40)
    print()

def update_best_score(score, best_score):
    """이번 점수와 최고 점수를 비교해, 더 높은 쪽을 최고 점수로 돌려준다."""
    if score is None:
        return best_score
    if best_score is None or score > best_score:
        print(f"🎉 최고 점수를 갱신했습니다! ({score}점)\n")
        return score
    print(f"최고 점수는 그대로 {best_score}점입니다.\n")
    return best_score

def show_score(best_score):
    """최고 점수를 출력한다. 아직 푼 기록이 없으면 안내한다."""
    if best_score is None:
        print("\n⚠️ 아직 퀴즈를 푼 기록이 없습니다. 먼저 퀴즈를 풀어 보세요.\n")
        return
    print(f"\n🏆 최고 점수: {best_score}점\n")

def main():
    """메뉴를 보여 주고, 고른 번호에 맞는 화면을 실행한다."""
    quizzes = make_default_quizzes()
    best_score = None
    while True:
        show_menu()
        choice = read_number("선택: ", 1, 5)
        if choice == 1:
            score = play_quiz(quizzes)
            best_score = update_best_score(score, best_score)
            save_state(quizzes, best_score)
        elif choice == 2:
            add_quiz(quizzes, best_score)
        elif choice == 3:
            show_quizzes(quizzes)
        elif choice == 4:
            show_score(best_score)

# python3.13 main.py처럼 이 파일을 직접 실행 시 main() 호출
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 입력이 중단되어 게임을 종료합니다.")