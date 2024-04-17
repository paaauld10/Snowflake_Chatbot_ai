
# # Import the streamlit library
# import streamlit as st

# # Set the title of your app
# st.title('My First Streamlit App')

# # Add a welcome message
# st.write('Welcome to my Streamlit app!')

# # Create a text input widget
# user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')

# # Display the customized message
# st.write('Customized Message:', user_input)

###############################################
import streamlit as st

# Streamlit UI
def main():
    st.title('Chat Bot')

    # Chat history
    chat_history = []

    # User input field
    user_input = st.text_input('You:', '')

    # Send button
    if st.button('Send'):
        if user_input:
            chat_history.append(('You', user_input))

            # Generate bot response (you can replace this with your actual chatbot logic)
            bot_response = "I'm just a simple bot, but I'm learning!"
            chat_history.append(('Bot', bot_response))

    # Display chat history
    for sender, message in chat_history:
        if sender == 'You':
            st.text_input(sender + ':', message, disabled=True)
        else:
            st.text_area(sender + ':', message, disabled=True)

if __name__ == "__main__":
    main()
