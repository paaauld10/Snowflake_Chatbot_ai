
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
# import streamlit as st

# # Streamlit UI
# def main():
#     st.title('Chat Bot')

#     # Chat history
#     chat_history = []

#     # User input field
#     user_input = st.text_input('You:', '')

#     # Send button
#     if st.button('Send'):
#         if user_input:
#             chat_history.append(('You', user_input))

#             # Generate bot response (you can replace this with your actual chatbot logic)
#             bot_response = "I'm just a simple bot, but I'm learning!"
#             chat_history.append(('Bot', bot_response))

#     # Display chat history
#     for sender, message in chat_history:
#         if sender == 'You':
#             st.text_input(sender + ':', message, disabled=True)
#         else:
#             st.text_area(sender + ':', message, disabled=True)

# if __name__ == "__main__":
#     main()

#########################################


from openai import OpenAI
import re
import streamlit as st
from prompts import get_system_prompt

st.title("☃️ Frosty")

# Initialize the chat messages history
client = OpenAI(api_key=st.secrets.OPENAI_API_KEY)
if "messages" not in st.session_state:
    # system prompt includes table information, rules, and prompts the LLM to produce
    # a welcome message to the user.
    st.session_state.messages = [{"role": "system", "content": get_system_prompt()}]

# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

# display the existing chat messages
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "results" in message:
            st.dataframe(message["results"])

# If last message is not from assistant, we need to generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response = ""
        resp_container = st.empty()
        for delta in client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        ):
            response += (delta.choices[0].delta.content or "")
            resp_container.markdown(response)

        message = {"role": "assistant", "content": response}
        # Parse the response for a SQL query and execute if available
        sql_match = re.search(r"```sql\n(.*)\n```", response, re.DOTALL)
        if sql_match:
            sql = sql_match.group(1)
            conn = st.connection("snowflake")
            message["results"] = conn.query(sql)
            st.dataframe(message["results"])
        st.session_state.messages.append(message)



















