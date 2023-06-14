import random
import tkinter as tk

def initialize_game():
    word_list = ['python', 'javascript', 'html', 'css', 'programming']
    word = random.choice(word_list)
    guessed_letters = set()
    attempts = 6

    return word, guessed_letters, attempts

def guess_letter():
    letter = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if letter in guessed_letters:
        message_label.configure(text="You already guessed that letter. Try again.")
    else:
        guessed_letters.add(letter)
        if letter in word:
            update_word_label()
            if all(letter in guessed_letters for letter in word):
                message_label.configure(text="Congratulations! You guessed the word correctly!")
                disable_input()
        else:
            attempts_left = attempts - len(guessed_letters.difference(word))
            message_label.configure(text=f"Wrong guess! Attempts left: {attempts_left}")
            draw_hangman(len(guessed_letters))

            if attempts_left == 0:
                message_label.configure(text=f"You ran out of attempts. The word was: {word}")
                disable_input()

def update_word_label():
    guessed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    word_label.configure(text=f"Word: {guessed_word}")

def disable_input():
    letter_entry.configure(state=tk.DISABLED)
    guess_button.configure(state=tk.DISABLED)

def draw_hangman(incorrect_guesses):
    # Aquí puedes implementar la lógica para dibujar el ahorcado en la interfaz gráfica
    pass

# Configuración de la ventana
window = tk.Tk()
window.title("Hangman Game")

# Inicialización del juego
word, guessed_letters, attempts = initialize_game()

# Etiquetas
word_label = tk.Label(window, text="Word: _" * len(word))
word_label.pack()

message_label = tk.Label(window, text="Enter a letter:")
message_label.pack()

# Entrada de texto
letter_entry = tk.Entry(window)
letter_entry.pack()

# Botón de adivinanza
guess_button = tk.Button(window, text="Guess", command=guess_letter)
guess_button.pack()

# Ejecución de la ventana
window.mainloop()
