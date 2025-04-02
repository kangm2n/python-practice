# guess_game.py

import random

answer = random.randint(1, 100)  # 1부터 100 사이 숫자 중 정답 설정
tries = 0  # 시도 횟수

print("숫자 맞추기 게임을 시작합니다! (1~100 사이)")

while True:
    guess = input("숫자를 입력하세요: ")

    # 입력값이 숫자인지 확인
    if not guess.isdigit():
        print("숫자만 입력해주세요!")
        continue

    guess = int(guess)
    tries += 1

    if guess < answer:
        print("UP!")
    elif guess > answer:
        print("DOWN!")
    else:
        print(f"정답입니다! 시도 횟수: {tries}번")
        break
