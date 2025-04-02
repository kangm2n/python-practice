# guess_game_final.py

import random

def choose_difficulty():
    print("난이도를 선택하세요:")
    print("1. 쉬움 (1~50)")
    print("2. 보통 (1~100)")
    print("3. 어려움 (1~200)")

    while True:
        choice = input("선택 (1/2/3): ")
        if choice == '1':
            return 1, 50
        elif choice == '2':
            return 1, 100
        elif choice == '3':
            return 1, 200
        else:
            print("❗ 올바른 숫자를 입력해주세요 (1, 2, 3)")

def play_game():
    low, high = choose_difficulty()
    answer = random.randint(low, high)
    max_tries = 5
    tries = 0

    print(f"\n🎮 {low}부터 {high}까지의 숫자 중에서 맞춰보세요!")
    print(f"총 기회는 {max_tries}번입니다.")

    while tries < max_tries:
        guess = input("숫자를 입력하세요: ")

        if not guess.isdigit():
            print("❗ 숫자만 입력해주세요!")
            continue

        guess = int(guess)
        tries += 1

        if guess < answer:
            print(f"UP! 남은 기회: {max_tries - tries}")
        elif guess > answer:
            print(f"DOWN! 남은 기회: {max_tries - tries}")
        else:
            print(f"🎉 정답입니다! 시도 횟수: {tries}번\n")
            break
    else:
        print(f"💥 실패! 정답은 {answer}였습니다.\n")

def main():
    while True:
        play_game()
        again = input("다시 하시겠습니까? (Y/N): ").lower()
        if again != 'y':
            print("게임을 종료합니다. 감사합니다!")
            break

if __name__ == "__main__":
    main()
