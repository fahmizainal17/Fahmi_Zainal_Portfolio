import streamlit as st
from PIL import Image

def page_style():
    custom_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            body {
                background-color: #f0f0f0;
            }
            .stButton>button {background-color: #4CAF50; color: white !important;}
            .stDownloadButton>button {background-color: #4CAF50; color: white !important;}

            /* Certification Card Styles */
            .cert-card {
                background-color: #333333;
                color: white;
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .cert-card:hover {
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            }
            .cert-icon {
                width: 60px;
                height: 60px;
                margin-right: 15px;
                border-radius: 50%;
            }
            .cert-content {
                display: flex;
                align-items: center;
            }
            .cert-title {
                font-weight: bold;
                font-size: 18px;
            }
            .cert-date {
                font-size: 14px;
                color: #ccc;
            }

            /* Experience Card Styles */
            .experience-card {
                background-color: #444444;
                color: white;
                padding: 20px;
                margin: 15px 0;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .experience-card:hover {
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            }
            .experience-content {
                display: flex;
                align-items: center;
                margin-bottom: 15px;
            }
            .experience-title {
                font-weight: bold;
                font-size: 22px;
                margin-bottom: 5px;
            }
            .experience-date-location {
                font-size: 14px;
                color: #ccc;
            }
            .experience-skills {
                font-size: 14px;
                color: #aaa;
                margin-top: 10px;
            }
            .experience-description {
                margin-top: 15px;
                line-height: 1.5;
            }
        </style>
    """
    icon = Image.open('photos/Round_Profile_Photo.jpg')
    st.set_page_config(page_title="Report Metrics Generator", page_icon=icon, layout="wide")
    st.markdown(custom_style, unsafe_allow_html=True)
    image = Image.open('photos/Background_Photo.png')
    st.image(image)

    # Sidebar content
    with st.sidebar:
        st.image("photos/Round_Profile_Photo.jpg", width=150)  # Adjust the image path and size as needed

        st.markdown("""
            ## Fahmi Zainal
            **Data Scientist | Analytics Engineer | Survey | Digital Marketing | Software Development | ML & AI | ETL | Databricks | API Deployment | Azure & AWS DevOps Practitioner | Army Reserved Officer 🎖**
        """)

        st.markdown("""
        ### Top Skills
        - **Python (Programming Language)**
        - **Google Cloud Platform (GCP)**
        - **TensorFlow**
        - **REST APIs**
        - **Azure Databricks**
        """)
