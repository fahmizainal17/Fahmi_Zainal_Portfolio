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
    # Encode the local background image for the sidebar
    sidebar_bg_base64 = get_base64_of_bin_file('assets/background_sidebar.jpg')

    # Apply custom styles, including the sidebar background image
    custom_style = f"""
        <style>
            /* Hide Streamlit's default menu, footer, and header */
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}

            /* Sidebar background with a dark overlay */
            [data-testid="stSidebar"] > div:first-child {{
                background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                                  url("data:image/jpg;base64,{sidebar_bg_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: local;
            }}

            /* Adjust the header and toolbar */
            [data-testid="stHeader"] {{
                background: rgba(0,0,0,0);
            }}

            [data-testid="stToolbar"] {{
                right: 2rem;
            }}

            /* Style for buttons */
            .stButton>button {{
                background-color: #4CAF50; 
                color: white !important;
                border: none;
                padding: 10px 20px;
                text-align: center;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            }}
            .stDownloadButton>button {{
                background-color: #4CAF50; 
                color: white !important;
                border: none;
                padding: 10px 20px;
                text-align: center;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            }}

            /* Skill Category Styles */
            .skill-category {{
                font-weight: bold;
                margin-bottom: 10px;
            }}

            /* Skill Description Styles */
            .skill-description {{
                margin-left: 15px;
                margin-bottom: 10px;
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
    st.image(image, use_column_width=True)

    # Sidebar content
    with st.sidebar:
        # Profile Picture
        st.image("photos/My_Photo/Round_Profile_Photo.jpg", width=80)
        st.markdown("<h1 style='font-size: 1.5em;'><strong>Fahmi Zainal</strong>, <em>Data Scientist</em></h1>", unsafe_allow_html=True)

        st.markdown("""
        **Data Scientist | Transforming Data into Insights | ML & AI Solutions Architect | Scalable ETL and API Deployment | Survey & Digital Strategy Innovator | Army Reserved Officer 🎖**
        """)

        st.markdown("""
            <h3>Top Skills</h3>
        """, unsafe_allow_html=True)

        # Data Science & Analytics
        with st.expander("📊 Data Science & Analytics", expanded=False):
            st.markdown("""
                **Statistical Analysis:**  
                Proficient in applying statistical methods to interpret complex data sets. Demonstrated expertise in the **Weighting Strata Project** using R and Databricks, which improved survey data representativeness by adjusting for demographic factors.

                **Data Mining:**  
                Expertise in extracting meaningful patterns and insights from large datasets. Showcased in the **Development of In-House Data Processing and Reporting Automation Tool**, which streamlined data workflows and reduced processing time from 8 hours to 30 minutes.

                **Data Visualization:**  
                Skilled in creating intuitive visual representations of data using tools like Tableau, Power BI, and matplotlib. Enhanced the **ROAS Dashboard** project, increasing data visualization efficiency by 25% and enabling better decision-making for marketing strategies.

                **Programming Languages:**  
                Proficient in Python, R, and SQL for data manipulation and analysis. Supported by certifications such as **IBM Data Science Essentials** and practical application in projects like the **Car Price Prediction Model** and **Flood Prediction Project**.

                **Machine Learning:**  
                Experience with developing, training, and deploying machine learning models. Demonstrated in the **Ad Scoring Model** project, which contributed to a 50% increase in revenue, and achieved a **Top 28%** ranking in the **Binary Prediction Competition on Smoker Status**.

                **Deep Learning:**  
                Knowledge of neural networks and frameworks such as TensorFlow and PyTorch. Applied in the **Flood Prediction Project** using TensorFlow Keras, achieving an 84% accuracy rate in predicting flood occurrences.
            """)

        # Machine Learning & AI Solutions Architecture
        with st.expander("🤖 Machine Learning & AI Solutions Architecture", expanded=False):
            st.markdown("""
                **AI System Design:**  
                Capable of designing scalable AI and ML architectures tailored to business needs. Implemented in the **Unified Web Application Ecosystem with FastAPI and AWS**, integrating Streamlit and Shiny frontends for seamless user interaction.

                **Model Deployment:**  
                Expertise in deploying machine learning models into production environments. Successfully deployed the **Flood Prediction Model** and **Computer Vision Project** APIs using Docker and AWS ECS, ensuring high availability and fault tolerance.

                **Algorithm Development:**  
                Skilled in developing and optimizing algorithms for various applications. Enhanced predictive performance in the **Ad Scoring Model** and **Binary Prediction Competition** through advanced techniques like Weighted Ensemble methods and hyperparameter tuning with Optuna.

                **Cloud Platforms:**  
                Proficient with cloud services like AWS, Azure, and Google Cloud for AI/ML solutions. Managed data pipelines and deployments in projects such as the **ROAS Dashboard** and **Unified Web Application Ecosystem**, leveraging AWS services like EC2 and Azure Databricks.

                **Automation:**  
                Implementing automated workflows for continuous integration and deployment of AI solutions. Automated chart customization and report generation in the **In-House Data Processing Tool** using VBA Macros and Streamlit.
            """)

        # Data Engineering & Infrastructure
        with st.expander("🛠️ Data Engineering & Infrastructure", expanded=False):
            st.markdown("""
                **ETL Processes:**  
                Designing and managing scalable Extract, Transform, Load (ETL) pipelines. Led the creation of robust ETL pipelines in the **Ad Scoring Model** and **IVR Data Analysis Project**, ensuring efficient data flow and integrity.

                **API Development:**  
                Building and deploying robust APIs for data access and integration. Developed RESTful APIs using FastAPI for the **ROAS Dashboard** and **Unified Web Application Ecosystem**, facilitating seamless data interactions.

                **Database Management:**  
                Experience with SQL and NoSQL databases such as PostgreSQL and MongoDB. Managed large marketing datasets in the **Ad Scoring Model** project using MongoDB and optimized data storage solutions for high performance.

                **Big Data Technologies:**  
                Familiarity with Hadoop, Spark, and similar big data frameworks. Utilized Databricks for processing extensive datasets in the **IVR Data Analysis Project**, enhancing data processing capabilities.

                **Scalability Solutions:**  
                Ensuring data systems are scalable and maintain high performance under load. Achieved scalable deployments in the **Flood Prediction Project** and **ROAS Dashboard**, leveraging AWS ECS and EC2 for reliable infrastructure.
            """)

        # Business Intelligence & Strategy
        with st.expander("📈 Business Intelligence & Strategy", expanded=False):
            st.markdown("""
                **Data Interpretation:**  
                Translating complex data into actionable business insights. Led survey projects and developed dashboards in the **In-House Data Processing Tool**, enabling data-driven decision-making.

                **Business Intelligence Tools:**  
                Proficient in BI tools like Tableau, Power BI, and Looker. Created comprehensive visualizations in the **HR Analytics Project** and **ROAS Dashboard**, facilitating better business insights.

                **Strategic Planning:**  
                Developing data-driven strategies to support business objectives. Contributed to digital marketing strategies through the **Ad Scoring Model** and **Digital Marketing Campaign Ad Set EDA and Ad Scoring** projects, optimizing marketing spend and increasing revenue.

                **Survey Design & Analysis:**  
                Creating and analyzing surveys to gather actionable feedback and insights. Directed survey projects in the **Data Scientist** role at INVOKE Solutions, enhancing data accuracy by 20%.

                **Digital Strategy Innovation:**  
                Innovating digital strategies to enhance business processes and customer engagement. Developed tools like the **VBA Macro Generator for Charts Handling** and the **Unified Web Application Ecosystem**, improving operational efficiency and user experience.

                **Data Storytelling:**  
                Communicating data insights effectively to stakeholders through compelling narratives. Presented findings in the **HR Analytics Project** and **Live Calls Data Analysis Project**, driving strategic initiatives and improving customer satisfaction.
            """)

        # Additional Skills
        with st.expander("🔧 Additional Skills", expanded=False):
            st.markdown("""
                **Project Management:**  
                Managing data projects from inception to completion using methodologies like Agile and Scrum. Successfully led multiple projects, including the **Unified Web Application Ecosystem** and **Deployment Endpoints to AWS ECS and EC2**, ensuring timely delivery and high-quality outcomes.

                **Collaboration & Communication:**  
                Working effectively with cross-functional teams and communicating complex technical concepts to non-technical stakeholders. Coordinated with data scientists, backend developers, and marketing teams in projects like the **Ad Scoring Model** and **IVR Data Analysis Project**.

                **Problem-Solving:**  
                Strong analytical and problem-solving abilities to address data-related challenges. Resolved data processing bottlenecks in the **In-House Data Processing Tool** and optimized model performance in various machine learning competitions.

                **Continuous Learning:**  
                Staying updated with the latest trends and advancements in data science, AI, and technology. Earned certifications such as **Advanced LLM Certificate**, **Kaggle Python Programming**, and actively participated in competitions and hackathons like the **AI Tinkerers Hackathon**.
            """)
        
        st.markdown("---")
        
        # Play Music Button
        new_tab_button = """
        <a href="https://www.youtube.com/watch?v=VeUiVCb7ZmQ&si=GzSBUP3zs1hEkigI" target="_blank">
            <button style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;">
                🎵 Play Music while Reading
            </button>
        </a>
        """
        st.markdown(new_tab_button, unsafe_allow_html=True)

        st.markdown("---")