import streamlit as st
from PIL import Image
import base64

def get_base64_of_bin_file(bin_file):
    """
    Function to encode local file (image or gif) to base64 string
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def page_style():
    # Encode the local GIF to base64
    sidebar_gif_base64 = get_base64_of_bin_file('assets/background_sidebar.jpg')

    # Apply custom styles, including the sidebar background GIF
    custom_style = f"""
        <style>
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}

            /* Sidebar background with a dark overlay */
            [data-testid="stSidebar"] > div:first-child {{
                background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                                  url("data:image/gif;base64,{sidebar_gif_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: local;
            }}

            [data-testid="stHeader"] {{
                background: rgba(0,0,0,0);
            }}

            [data-testid="stToolbar"] {{
                right: 2rem;
            }}

            .stButton>button {{background-color: #4CAF50; color: white !important;}}
            .stDownloadButton>button {{background-color: #4CAF50; color: white !important;}}

            /* Certification Card Styles */
            .cert-card {{
                background-color: #333333;
                color: white;
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .cert-card:hover {{
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            }}
        </style>
    """
    
    # Set the page configuration
    icon = Image.open('photos/My_Photo/Round_Profile_Photo.jpg')
    st.set_page_config(page_title="Fahmi Zainal", page_icon=icon, layout="wide")

    # Apply custom styles to the page
    st.markdown(custom_style, unsafe_allow_html=True)

    # Display the main background image
    image = Image.open('photos/My_Photo/Background_Photo.png')
    st.image(image)

    # Sidebar content
    with st.sidebar:
        # Profile Picture
        st.image("photos/My_Photo/Round_Profile_Photo.jpg", width=80)
        st.markdown("<h1 style='font-size: 1.5em;'><strong>Fahmi Zainal</strong>, <em>Data Scientist</em></h1>", unsafe_allow_html=True)

        st.markdown("""
        **Data Scientist | Analytics Engineer | Survey | Digital Marketing | Software Development | ML & AI | ETL | Databricks | API Deployment | Azure & AWS DevOps Practitioner | Army Reserved Officer 🎖**
        """)

        st.markdown("""
        ### Top Skills
        - **Data Analytics, EDA and Modelling**
        - **Power BI and Tableau Dashboarding**
        - **Python (Programming Language)**
        - **SQL Querying and Modelling**
        - **Machine Learning (ML)**
        - **RESTful APIs Designing**
        - **Databricks**
        - **AWS(S3, ECS, EC2)**
        - **Google Cloud Platform (GCP) APIs**
        - **TensorFlow and Pytorch Framework**
        """)

        # HTML and JavaScript to open YouTube in a new tab
        new_tab_button = """
        <a href="https://www.youtube.com/watch?v=VeUiVCb7ZmQ?si=GzSBUP3zs1hEkigI" target="_blank">
            <button style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;">
                🎵 Play Music while Reading
            </button>
        </a>
        """
        st.markdown(new_tab_button, unsafe_allow_html=True)

