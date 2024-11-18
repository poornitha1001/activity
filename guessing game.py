import streamlit as st
import random

def main():
    st.title("Guess the Number Game")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 10
        st.session_state.guesses = []

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Attempts left: {st.session_state.attempts}")
    with col2:
        if st.session_state.guesses:
            st.write("Previous guesses:", st.session_state.guesses)

    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        handle_guess(guess)

def handle_guess(guess):
    st.session_state.guesses.append(guess)
    st.session_state.attempts -= 1

    if guess < st.session_state.secret_number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try again.")
    else:
        st.success("Congratulations! You've guessed the number!")
        reset_game()

    if st.session_state.attempts == 0:
        st.error(f"Game Over! The secret number was {st.session_state.secret_number}.")
        reset_game()

def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 10
    st.session_state.guesses = []

if _name_ == "_main_":
    main()