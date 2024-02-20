import streamlit as st

def main():
    st.title("Prettified Form Example")

    # Add some padding and center the form
    st.markdown("<h3 style='padding: 10px; text-align: center;'>Please fill out the form:</h3>", unsafe_allow_html=True)
    
    # Create input fields
    name = st.text_input("Name:", key='name_input')
    email = st.text_input("Email:", key='email_input')
    age = st.number_input("Age:", min_value=0, max_value=150, key='age_input')

    # Add a submit button
    if st.button("Submit", key='submit_button'):
        if name and email and age:
            st.success(f"Form submitted successfully!\nName: {name}\nEmail: {email}\nAge: {age}")
            print(name, email, age)
        else:
            st.error("Please fill out all fields.")

if __name__ == "__main__":
    main()
