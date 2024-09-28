import tkinter as tk
from tkinter import messagebox
import random

words=['python', 'cobra', 'earth', 'universe', 'happy','sad', 'plastic','eraser','India']

word_to_guess = random.choice(words)
guessed_letters=[]
attempts=6

window=tk.Tk()
window.title("Hangman Challenge")

def is_game_over():
    return check_win() or check_loss()

def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)

def check_loss():
    return attempts == 0

def guess_letter():
    global attempts
    letter= letter_entry.get().lower()
    if letter.isalpha() and len(letter)==1:
        if letter in guessed_letters:
            messagebox.showinfo("Hangman", f"You've already guessed '{letter}'")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                messagebox.showinfo("Hangman", "Congratulations! You Win!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -=1
            update_attempts_display()
            draw_hangman()
            if check_loss():
                messagebox.showinfo("Hangman", "You lose! The Word was:" + word_to_guess)
                reset_game()
        letter_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Please enter a single letter.")


def reset_game():
    global word_to_guess, guessed_letters, attempts
    word_to_guess= random.choice(words)
    guessed_letters=[]
    attempts = 6
    update_word_display()
    update_attempts_display()
    draw_hangman()

def update_word_display():
    display_word= ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
        display_word += " "
    word_label.config(text = display_word)

def update_attempts_display():
    attempts_label.config(text = f"Attempts left:{attempts}")

def draw_hangman():
    canvas.delete("hangman")
    if attempts < 6:
        canvas.create_oval(125,125,175,175, width=4, tags="hangman")
    if attempts < 5:
        canvas.create_line(150,175,150,225, width=4, tags="hangman")
    if attempts < 4:
        canvas.create_line(150,200,125,175, width=4, tags="hangman")
    if attempts < 3:
        canvas.create_line(150,200,175,175, width=4, tags="hangman")    
    if attempts < 2:
        canvas.create_line(150,225,125,250, width=4, tags="hangman")
    if attempts < 1:
        canvas.create_line(150,225,175,250, width=4, tags="hangman")

            
word_label = tk.Label(window, text="", font=("Arial", 24))
attempts_label = tk.Label(window, text="", font=("Arial", 16))
letter_entry = tk.Entry(window, width=5, font=("Arial", 16))
guess_button = tk.Button(window, text="Guess", command=guess_letter)
reset_button = tk.Button(window, text="Reset", command=reset_game)
canvas = tk.Canvas(window, width=300, height=300)
canvas.create_line(50,250,250,250, width=4)
canvas.create_line(200,250,200,100, width=4)
canvas.create_line(100,100,200,100, width=4)
canvas.create_line(150,100,150,120, width=4)
canvas.pack()

word_label.pack()
attempts_label.pack()
letter_entry.pack()
guess_button.pack()
reset_button.pack()

update_word_display()
update_attempts_display()
draw_hangman()

window.mainloop()