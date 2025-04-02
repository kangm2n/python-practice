import tkinter as tk
import random

class GuessGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("숫자 맞추기 게임")

        self.low = 1
        self.high = 100
        self.max_tries = 5
        self.reset_game()

        # 위젯 구성
        self.label_info = tk.Label(root, text="1부터 100 사이의 숫자를 맞혀보세요!")
        self.label_info.pack()

        self.label_hint = tk.Label(root, text=f"남은 기회: {self.max_tries}")
        self.label_hint.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button_check = tk.Button(root, text="확인", command=self.check_guess)
        self.button_check.pack()

        self.label_result = tk.Label(root, text="")
        self.label_result.pack()

        self.button_retry = tk.Button(root, text="다시 시작", command=self.reset_game, state="disabled")
        self.button_retry.pack()

    def reset_game(self):
        self.answer = random.randint(self.low, self.high)
        self.tries = 0
        if hasattr(self, 'label_hint'):
            self.label_hint.config(text=f"남은 기회: {self.max_tries}")
        if hasattr(self, 'label_result'):
            self.label_result.config(text="")
        if hasattr(self, 'entry'):
            self.entry.delete(0, tk.END)
        if hasattr(self, 'button_retry'):
            self.button_retry.config(state="disabled")
        if hasattr(self, 'button_check'):
            self.button_check.config(state="normal")

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.label_result.config(text="숫자를 입력해주세요!")
            return

        guess = int(guess)
        self.tries += 1
        remaining = self.max_tries - self.tries

        if guess < self.answer:
            self.label_result.config(text=f"UP! 남은 기회: {remaining}")
        elif guess > self.answer:
            self.label_result.config(text=f"DOWN! 남은 기회: {remaining}")
        else:
            self.label_result.config(text=f"정답입니다! 🎉 시도 횟수: {self.tries}번")
            self.end_game()
            return

        self.label_hint.config(text=f"남은 기회: {remaining}")

        if self.tries >= self.max_tries:
            self.label_result.config(text=f"실패! 정답은 {self.answer}였습니다.")
            self.end_game()

    def end_game(self):
        self.button_check.config(state="disabled")
        self.button_retry.config(state="normal")

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessGameApp(root)
    root.mainloop()
