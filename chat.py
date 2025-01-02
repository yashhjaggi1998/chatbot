"""
# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            'message': 'Hello Serial, how can I help you?'
        }
    ]

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.

if prompt := st.chat_input("What is up?"):

    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response using the OpenAI API.
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True,
    )

    # Stream the response to the chat using `st.write_stream`, then store it in 
    # session state.
    with st.chat_message("assistant"):
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
"""

"""
# Status code
with st.status('Trying to answer you query...', expanded = True) as status:
    try:
        st.write('Fetching top k results pertaining to the query...');
        time.sleep(2)

        st.write('Fetched top k results...');
        time.sleep(2)

        st.write('Generating a response...')
        time.sleep(2)

        status.update(label = 'Here is your answer', state = 'complete', expanded = False)
    except: 
        status.update(label = 'Failed to answer your query due to internal server error', state = 'error', expanded = False)
"""