# 숫자 맞추기 게임(횟수 제한 버전)

# guess_game_limit.py

import random

answer = random.randint(1, 100)
tries = 0
max_tries = 5  # 최대 시도 횟수 제한

print("🎮 숫자 맞추기 게임을 시작합니다! (1~100)")
print(f"최대 {max_tries}번의 기회가 있어요!")

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
        print(f"🎉 정답입니다! 시도 횟수: {tries}번")
        break
else:
    print(f"💥 아쉽지만 실패! 정답은 {answer}였습니다.")
