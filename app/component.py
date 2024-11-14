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
        **Data Scientist | Transforming Data into Insights | ML & AI Solutions Architect | Scalable ETL and API Deployment | Survey & Digital Strategy Innovator | Army Reserved Officer 🎖**
        """)

        st.markdown("""
        <style>
            .skill {
                position: relative;
                display: inline-block;
                font-weight: bold;
                color: #ffffff;
            }

            .skill .tooltip {
                visibility: hidden;
                width: 250px;
                background-color: #333;
                color: #fff;
                text-align: center;
                padding: 8px;
                border-radius: 5px;
                position: absolute;
                z-index: 1;
                bottom: 125%; /* Position above the skill */
                left: 50%;
                margin-left: -125px;
                opacity: 0;
                transition: opacity 0.3s;
            }

            .skill:hover .tooltip {
                visibility: visible;
                opacity: 1;
            }
        </style>

        ### Top Skills
        <div>
            <p class="skill">Data Analytics, EDA and Modelling
                <span class="tooltip">Extracting insights and building predictive models to drive data-driven decisions.</span>
            </p>
            <p class="skill">Power BI and Tableau Dashboarding
                <span class="tooltip">Creating interactive dashboards to make data accessible and actionable.</span>
            </p>
            <p class="skill">Python (Programming Language)
                <span class="tooltip">Advanced programming for data processing, automation, and machine learning.</span>
            </p>
            <p class="skill">SQL Querying and Modelling
                <span class="tooltip">Data transformation and efficient querying for analytics and reporting.</span>
            </p>
            <p class="skill">Machine Learning (ML)
                <span class="tooltip">Developing ML models for predictive analysis and impactful solutions.</span>
            </p>
            <p class="skill">RESTful APIs Designing
                <span class="tooltip">Designing scalable APIs for data-driven applications.</span>
            </p>
            <p class="skill">Databricks
                <span class="tooltip">Big data processing and collaborative analytics in the cloud.</span>
            </p>
            <p class="skill">AWS (S3, ECS, EC2)
                <span class="tooltip">Cloud solutions for scalable storage, computing, and model deployment.</span>
            </p>
            <p class="skill">Google Cloud Platform (GCP) APIs
                <span class="tooltip">Managing data pipelines and deploying analytics on GCP.</span>
            </p>
            <p class="skill">TensorFlow and PyTorch Framework
                <span class="tooltip">Building and fine-tuning deep learning models for complex tasks.</span>
            </p>
        </div>
        """, unsafe_allow_html=True)


        # HTML and JavaScript to open YouTube in a new tab
        new_tab_button = """
        <a href="https://www.youtube.com/watch?v=VeUiVCb7ZmQ?si=GzSBUP3zs1hEkigI" target="_blank">
            <button style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;">
                🎵 Play Music while Reading
            </button>
        </a>
        """
        st.markdown(new_tab_button, unsafe_allow_html=True)

