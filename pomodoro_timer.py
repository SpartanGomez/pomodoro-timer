import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.master.geometry("300x150")

        self.time_left = 25 * 60  # 25 minutes in seconds
        self.is_break = False
        self.is_running = False

        self.label = tk.Label(master, text="25:00", font=("Arial", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.countdown()

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def countdown(self):
        if self.is_running:
            if self.time_left <= 0:
                if self.is_break:
                    messagebox.showinfo("Pomodoro Timer", "Break time is over. Time to work!")
                    self.time_left = 25 * 60
                    self.is_break = False
                else:
                    messagebox.showinfo("Pomodoro Timer", "Work session completed. Take a break!")
                    self.time_left = 5 * 60
                    self.is_break = True
            
            minutes, seconds = divmod(self.time_left, 60)
            time_string = f"{minutes:02d}:{seconds:02d}"
            self.label.config(text=time_string)
            self.time_left -= 1
            self.master.after(1000, self.countdown)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()