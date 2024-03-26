import tkinter as tk
from tkinter import messagebox
import time

class PomodoroClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Clock")
        
        self.work_time = 45 * 60  # 25 minutes in seconds
        self.break_time = 5 * 60  # 5 minutes in seconds
        
        self.time_remaining = tk.StringVar()
        self.time_remaining.set(self._format_time(self.work_time))
        
        self.clock_label = tk.Label(master, textvariable=self.time_remaining, font=("Helvetica", 48))
        self.clock_label.pack(pady=20)
        
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        self.running = False
        self.time_left = self.work_time
        self.start_time = None
        
    def _format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.run_timer()
        
    def stop_timer(self):
        if self.running:
            self.running = False
        
    def reset_timer(self):
        self.stop_timer()
        self.running = False
        self.time_left = self.work_time
        self.time_remaining.set(self._format_time(self.time_left))
        
    def run_timer(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.time_left = max(self.work_time - int(elapsed_time), 0)
            self.time_remaining.set(self._format_time(self.time_left))
            if self.time_left == 0:
                self.timer_finished()
            else:
                self.master.after(1000, self.run_timer)
        
    def timer_finished(self):
        self.running = False
        messagebox.showinfo("Pomodoro Clock", "Time's up!")
        self.reset_timer()
        
if __name__ == "__main__":
    root = tk.Tk()
    clock = PomodoroClock(root)
    root.mainloop()
