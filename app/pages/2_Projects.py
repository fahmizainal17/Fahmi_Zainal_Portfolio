import streamlit as st
from transformers import pipeline

resume_data = {
    "name": "Fahmi Zainal",
    "email": "fahmizainal9@gmail.com",
    "phone": "+60165507849",
    "experience": [
        {
            "role": "Data Scientist",
            "company": "INVOKE Solutions",
            "duration": "November 2023 – Now",
            "details": "Working on survey automation, data analysis, and predictive modeling."
        },
        {
            "role": "Data Processing Specialist",
            "company": "NielsenIQ",
            "duration": "June 2024 – Present",
            "details": "Input validation and data processing."
        }
    ],
    "skills": ["Python", "FastAPI", "Streamlit", "AWS", "Machine Learning", "Data Analysis"]
}

# Load pre-trained model
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased", tokenizer="distilbert-base-uncased")

# Function to answer questions based on resume data
def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Combine resume data into a context string
context = f"""
My name is {resume_data['name']}. You can contact me at {resume_data['email']} or {resume_data['phone']}.
I have worked as a {resume_data['experience'][0]['role']} at {resume_data['experience'][0]['company']} from {resume_data['experience'][0]['duration']}.
My responsibilities included: {resume_data['experience'][0]['details']}.
I am skilled in {', '.join(resume_data['skills'])}.
"""

# Streamlit app
st.title("Resume Chatbot")

question = st.text_input("Ask a question about my resume:")
if question:
    answer = answer_question(question, context)
    st.write(answer)
