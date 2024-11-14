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
        ### Top Skills
        <style>
            .skill-box {
                padding: 8px 15px;
                margin: 5px 0;
                border-radius: 8px;
                background-color: #333333;
                color: white;
                cursor: pointer;
                font-weight: bold;
                text-align: center;
            }
            .popup {
                display: none;
                position: fixed;
                z-index: 1;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0,0,0,0.5);
                justify-content: center;
                align-items: center;
            }
            .popup-content {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                width: 300px;
                text-align: center;
                font-size: 16px;
                color: black;
            }
        </style>

        <div class="skill-box" onclick="showPopup('Data Analytics & Insights – Extracting actionable insights to drive data-driven decisions')">Data Analytics</div>
        <div class="skill-box" onclick="showPopup('Exploratory Data Analysis & Modeling – Uncovering trends and building predictive models')">EDA & Modeling</div>
        <div class="skill-box" onclick="showPopup('Data Visualization – Creating dynamic dashboards with Power BI & Tableau')">Data Visualization</div>
        <div class="skill-box" onclick="showPopup('Python – Advanced data processing, automation, and ML pipelines')">Python</div>
        <div class="skill-box" onclick="showPopup('SQL – Data transformation and modeling for robust analytics')">SQL</div>
        <div class="skill-box" onclick="showPopup('Machine Learning – Developing predictive models for impactful solutions')">Machine Learning</div>
        <div class="skill-box" onclick="showPopup('RESTful APIs – Designing scalable data-driven APIs')">RESTful APIs</div>
        <div class="skill-box" onclick="showPopup('Cloud Solutions – Expertise in Databricks, AWS, and GCP')">Cloud Solutions</div>
        <div class="skill-box" onclick="showPopup('Deep Learning – Building models with TensorFlow and PyTorch')">Deep Learning</div>

        <div id="popup" class="popup" onclick="hidePopup()">
            <div class="popup-content" id="popup-content"></div>
        </div>

        <script>
            function showPopup(text) {
                document.getElementById('popup-content').innerText = text;
                document.getElementById('popup').style.display = 'flex';
            }

            function hidePopup() {
                document.getElementById('popup').style.display = 'none';
            }
        </script>
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

