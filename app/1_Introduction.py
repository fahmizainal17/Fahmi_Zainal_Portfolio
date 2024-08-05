import streamlit as st
from streamlit_chat import message
import requests

st.set_page_config(
    page_title="Fahmi Zainal Chatbot",
    page_icon=":robot:"
)

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": st.secrets['api_key']}

st.header("Fahmi Zainal Chatbot")
st.markdown("[Github](https://github.com/fahmizainal17/FastAPI_ROAS_Dashboard)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text

# Resume text to be used for generating responses
resume_text = """
Hello! My name is Fahmi Zainal. I am a Full-Stack Data Scientist and AI enthusiast based in Selangor, Malaysia.
I have expertise in Azure Databricks, Visual Studio Code, FastAPI, Streamlit, Docker, AWS Services, R programming, and Next.js.
I work on developing machine learning models for analyzing human behaviors and socio-economic trends from survey data, and I manage interactive dashboards for detailed data analysis.
I lead and mentor teams at INVOKE, manage interns and new hires, and have developed a Survey Automation platform using a diverse toolkit.
Feel free to ask me about my work experience, skills, and projects!
"""

user_input = get_text()

if user_input:
    output = query({
        "inputs": {
            "past_user_inputs": st.session_state.past,
            "generated_responses": st.session_state.generated,
            "text": f"{resume_text} {user_input}",
        }, "parameters": {"repetition_penalty": 1.33},
    })

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["generated_text"])

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
