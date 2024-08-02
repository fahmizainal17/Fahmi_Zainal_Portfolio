import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Instantiate the OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    message = response.choices[0].message.content.strip()
    return message

def main():
    st.title("Chat with Fahmi's Resume Bot")
    st.write("Ask anything about Fahmi Zainal's professional experience, skills, and projects!")

    # Displaying the resume information
    with st.expander("Show Resume"):
        st.write("""
        **Muhammad Fahmi Bin Mohd Zainal**
        - **Location:** Kuala Lumpur, Malaysia
        - **Email:** fahmizainal9@gmail.com
        - **Phone:** +60165507849
        - **LinkedIn Profile:** [LinkedIn](https://www.linkedin.com)
        - **GitHub Profile:** [GitHub](https://www.github.com)
        - **Tableau Profile:** [Tableau](https://www.tableau.com)
        - **Credly Profile:** [Credly](https://www.credly.com)

        **Summary:**
        Full-Stack Data Scientist with 1+ years of experience in IT, data analytics, and data science...

        **Professional Experience:**
        - **INVOKE SOLUTIONS Kuala Lumpur** (Senior Data Scientist, November 2023 – Present)
        - **EXCELERATE ASIA Kuala Lumpur** (Data Analyst Trainee, March 2023 – October 2023)
        - **MALAYSIAN NUCLEAR AGENCY Bangi, Selangor** (Research Officer Trainee, July 2022 – September 2022)
        - **MALAYSIAN ARMED FORCE Kuala Lumpur** (Second Lieutenant Reserved Army, September 2019 – February 2023)

        **Education:**
        - **UNIVERSITY OF MALAYA Kuala Lumpur** (Bachelor of Science in Physics (Hons), September 2019 – February 2023)

        **Certifications:**
        - Oil & Gas Meta HRDC Fundamentals Of Oil and Gas Softwares for Professional...
        - General Assembly Data Analytics and Data Science Bootcamp, 2023
        - Kaggle Python certification, 2023
        - Coursera Working with Big Query certification, 2023
        - IBM Data Analytics Essential Certificate recipient, 2023
        - IBM Excel Essential for Data Analysis Certificate recipient, 2023
        - IBM Data Visualization and Dashboards with Excel and Cognos Analytics Certificate recipient, 2023

        **Achievements:**
        - Achieved top 28% ranking out of 1908 teams internationally in a Binary Prediction Competition...
        - Completed Flood Prediction Project leveraging Deep Learning model...
        - Planned the work meticulously, conducting nightly meetings to discuss strategies...

        **Skills:**
        - Programming Languages: Python, Pyspark, SQL, R, HTML, CSS
        - Cloud & Databases: Azure Databricks, Azure Functions, AWS Services...
        - Data Science Packages: Pandas, Numpy, BS4, Sklearn, TensorFlow, Keras...
        - Data Processing and Analytics: PySpark, Google Colab, Streamlit Web Application...
        - Dashboarding and Reporting: Microsoft Office (Excel, PowerPoint, Word), PowerBI, Tableau...
        - Web Development: RESTful API, FastAPI, Streamlit Web App...
        - Containerization and Virtual Machine: WSL, Ubuntu, Docker...
        - Development Tools: Visual Studio Code, GitHub Actions (CI/CD)...
        """)

    # Chatbot interface
    user_input = st.text_input("You: ", "Tell me about your experience at INVOKE SOLUTIONS")

    if st.button("Send"):
        prompt = f"Muhammad Fahmi Bin Mohd Zainal's resume:\n{user_input}\nBased on the resume, answer the query."
        response = generate_response(prompt)
        st.text_area("Fahmi's Resume Bot:", value=response, height=200)

if __name__ == "__main__":
    main()
