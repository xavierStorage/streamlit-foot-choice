import streamlit as st
import random

def main():
    st.title("Food Decision Maker")
    st.write("Can't decide what to eat? Let us help you choose!")

    options = ["Chinese food", "Korean food", "American food", "Japanese food", "Thai food", "Cook at home"]
    choice = st.button("Choose for Me")

    if choice:
        random_option = random.choice(options)
        st.write(f"You should have: {random_option}!")

if __name__ == "__main__":
    main()