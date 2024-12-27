import requests
import tkinter as tk
from tkinter import ttk, messagebox
import random
import html

# Function to fetch trivia questions from the API
def fetch_trivia_questions():
    url = "https://opentdb.com/api.php?amount=50&category=15&difficulty=medium&type=multiple"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['response_code'] == 0:
            return data['results']
        else:
            messagebox.showerror("Error", "No trivia questions available.")
            return []
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to fetch trivia questions: {e}")
        return []

# Function to display the next question
def next_question():
    global current_question_index, selected_correct, next_button

    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        question_label["text"] = html.unescape(question_data["question"])

        # Shuffle answers
        answers = question_data["incorrect_answers"] + [question_data["correct_answer"]]
        answers = [html.unescape(ans) for ans in answers]
        random.shuffle(answers)

        # Display answers
        for i, answer in enumerate(answers):
            answer_buttons[i]["text"] = answer
            answer_buttons[i]["state"] = "normal"
            answer_buttons[i]["command"] = lambda ans=answer, correct=question_data["correct_answer"]: check_answer(ans, correct)

        feedback_label["text"] = ""
        next_button["state"] = "disabled"
        selected_correct = False

        current_question_index += 1
    else:
        messagebox.showinfo("Game Over", f"Game over! Your score: {score}/{len(questions)}")
        root.quit()

# Function to check the selected answer
def check_answer(selected, correct):
    global score, wrong_answers, selected_correct, next_button

    if selected == html.unescape(correct):
        feedback_label.configure(text="Correct!", foreground="green")
        score += 1
        score_label.configure(text=f"Correct: {score}")
        selected_correct = True
    else:
        feedback_label.configure(text=f"Wrong! The correct answer was: {html.unescape(correct)}", foreground="red")
        wrong_answers += 1
        wrong_label.configure(text=f"Wrong: {wrong_answers}")

    # Disable answer buttons after selection
    for btn in answer_buttons:
        btn["state"] = "disabled"

    next_button["state"] = "normal"

# Timer function
def update_timer():
    global elapsed_time
    elapsed_time += 1
    minutes, seconds = divmod(elapsed_time, 60)
    if minutes > 0:
        timer_label.configure(text=f"Time: {minutes:02}:{seconds:02}")
    else:
        timer_label.configure(text=f"Time: {seconds}s")
    root.after(1000, update_timer)

# Initialize game data
questions = fetch_trivia_questions()
current_question_index = 0
score = 0
wrong_answers = 0
selected_correct = False

# Timer initialization
elapsed_time = 0  # Start the timer at 0 seconds

# GUI Setup
root = tk.Tk()
root.title("Trivia Game")
root.geometry("650x420")
root.configure(bg="#131313")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Correct.TLabel", background="#131313", foreground="green", font=("Verdana", 12)
)
style.configure(
    "Wrong.TLabel", background="#131313", foreground="red", font=("Verdana", 12)
)
style.configure(
    "Question.TLabel", background="#131313", foreground="white", font=("Verdana", 14, "bold")
)
style.configure(
    "Answer.TButton", background="#131313", foreground="white", font=("Verdana", 12)
)
style.map(
    "Answer.TButton",
    background=[("active", "#444444")],  # Hover background color
    foreground=[("active", "white")],    # Hover text color
)
style.configure(
    "Feedback.TLabel", background="#131313", foreground="white", font=("Verdana", 14)
)
style.configure(
    "Timer.TLabel", background="#131313", foreground="yellow", font=("Verdana", 12)
)

# Widgets
score_frame = tk.Frame(root, bg="#131313")
score_frame.pack(side="left", fill="y", padx=10, pady=10)

# Add a container to vertically center the timer and score labels
center_frame = tk.Frame(score_frame, bg="#131313")
center_frame.pack(expand=True)

# Timer label
timer_label = ttk.Label(center_frame, text=f"Time: {elapsed_time}s", style="Timer.TLabel")
timer_label.pack(anchor="center", pady=(10, 10))

score_label = ttk.Label(center_frame, text="Correct: 0", style="Correct.TLabel")
score_label.pack(anchor="center", pady=(10, 5))

wrong_label = ttk.Label(center_frame, text="Wrong: 0", style="Wrong.TLabel")
wrong_label.pack(anchor="center", pady=(5, 10))

main_frame = tk.Frame(root, bg="#131313")
main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

question_label = ttk.Label(main_frame, text="", style="Question.TLabel", wraplength=500, justify="center")
question_label.pack(pady=20)

answer_buttons = []
for _ in range(4):
    btn = ttk.Button(main_frame, text="", style="Answer.TButton", width=50)
    btn.pack(pady=5)
    answer_buttons.append(btn)

feedback_label = ttk.Label(main_frame, text="", style="Feedback.TLabel", wraplength=500, justify="center")
feedback_label.pack(pady=10)

next_button = ttk.Button(main_frame, text="Next Question", command=lambda: next_question(), state="disabled")
next_button.pack(pady=20)

# Start the timer
update_timer()

# Start the game
if questions:
    next_question()
else:
    messagebox.showerror("Error", "Unable to load questions. Please try again later.")
    root.quit()

root.mainloop()
