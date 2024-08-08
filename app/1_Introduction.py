import streamlit as st
import replicate
import os
from module.Introduction.resume_text import resume_text
from streamlit_chat import message

# Set up the page configuration 
st.set_page_config(page_title="🦙💬 Fahmi Zainal Llama 2 Chatbot", page_icon=":robot:", layout="wide")

# Define the app title and sidebar for API token input
with st.sidebar:
    st.title('🦙💬 Llama 2 Chatbot')
    
    replicate_api = st.text_input('Enter Replicate API token:', type='password')
    if replicate_api:
        st.success('Proceed to entering your prompt message!', icon='👉')
        os.environ['REPLICATE_API_TOKEN'] = replicate_api
    else:
        st.warning('Please enter your credentials!', icon='⚠️')

    st.subheader('Models and parameters')
    selected_model = st.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Llama2-13B'], key='selected_model')
    if selected_model == 'Llama2-7B':
        llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
    elif selected_model == 'Llama2-13B':
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    temperature = st.slider('Temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.slider('Top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.slider('Max length', min_value=32, max_value=128, value=120, step=8)
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')

# Initialize the session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Function to clear chat history
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response with resume context
def generate_llama2_response(prompt_input):
    context = resume_text + "\n\nUser: " + prompt_input + "\nAssistant:"
    output = replicate.run(
        llm,
        input={"prompt": context, "temperature": temperature, "top_p": top_p, "max_length": max_length, "repetition_penalty": 1}
    )
    output_list = list(output)  # Convert generator to list
    return output_list[0]  # Assuming output is a list of strings

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
