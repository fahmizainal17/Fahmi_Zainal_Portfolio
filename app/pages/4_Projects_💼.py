import streamlit as st
from component import page_style

def show():
    # Apply page style
    page_style()

    st.title("Projects 💼")

    # Project 1: VBA Macro Generator for Charts Handling (Aug 2024)
    st.markdown("### August 2024")
    st.subheader("**VBA Macro Generator for Charts Handling**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a VBA Macro Generator to automate the process of chart handling and arrangement within presentations. This project utilized Python, VBA, and Streamlit to enable users to map chart templates easily, reducing manual effort and improving workflow efficiency.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="VBA Macro Generator", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/VBA_Macro_Generator_for_Charts)")

    st.markdown("---")

    # Project 2: Machine Learning Project to Predict Income Group (July - Aug 2024)
    st.markdown("### July - August 2024")
    st.subheader("**Machine Learning Project to Predict Income Group**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        A machine learning project focused on predicting income groups based on survey data. The project involved extensive data preprocessing, feature engineering, and the development of classification models to achieve accurate predictions. Key tools used included Python, Pandas, and Scikit-learn.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Predicting Income Group", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Machine_Learning_Income_Group_Prediction)")

    st.markdown("---")

    # Project 3: ROAS Dashboard API Endpoints (May - Aug 2024)
    st.markdown("### May - August 2024")
    st.subheader("**Creating Endpoints for ROAS Dashboard**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Designed and implemented API endpoints directly within the Databricks framework for the Return on Ad Spend (ROAS) Dashboard. The project aimed to streamline data processing for digital marketing campaigns, enhancing backend functionality for integration with frontend services.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="ROAS Dashboard", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/ROAS_Dashboard_API_Endpoints)")

    st.markdown("---")

    # Project 4: Digital Marketing Ad Scoring (June - Aug 2024)
    st.markdown("### June - August 2024")
    st.subheader("**Digital Marketing Campaign Ad Set EDA and Ad Scoring**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a model to analyze and score digital marketing ad sets based on extensive data analysis and machine learning algorithms. This project involved collaboration with other data scientists and backend developers to integrate the scoring system into a digital marketing platform.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Ad Set EDA and Scoring", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Digital_Marketing_Ad_Scoring)")

    st.markdown("---")

    # Project 5: Deployment Endpoints to AWS ECS and EC2 (June - July 2024)
    st.markdown("### June - July 2024")
    st.subheader("**Deployment Endpoints to AWS ECS and EC2**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Utilized DevOps practices to deploy API endpoints to AWS ECS and EC2, ensuring continuous operation and availability. The deployment process included setting up IAM roles, configuring ECR, and managing CI/CD pipelines using GitHub Actions.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="AWS ECS and EC2 Deployment", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/AWS_Endpoints_Deployment)")

    st.markdown("---")

    # Project 6: Unified Web Application Ecosystem (Feb - June 2024)
    st.markdown("### February - June 2024")
    st.subheader("**Unified Web Application Ecosystem with FastAPI and AWS**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a unified web application ecosystem that bridges Streamlit and Shiny frontends using FastAPI and AWS services. The project involved extensive backend development, containerization with Docker, and deployment using AWS ECS and API Gateway.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Unified Web Application", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Unified_Web_Application_Ecosystem)")

    st.markdown("---")

    # Project 7: IVR Data Automation (Nov 2023 - Aug 2024)
    st.markdown("### November 2023 - August 2024")
    st.subheader("**Interactive Voice Response (IVR) Data Automation Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        This project automated the processing of Interactive Voice Response (IVR) data using Streamlit. The project included data cleaning, analysis, and the creation of automated reports, significantly improving data processing efficiency.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="IVR Data Automation", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/IVR_Data_Automation_Project)")

    st.markdown("---")

    # Project 8: Kaggle Binary Prediction Competition (Oct - Nov 2023)
    st.markdown("### October - November 2023")
    st.subheader("**Kaggle Playground Competition: Binary Prediction of Smoker Status**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Participated in a Kaggle Playground Competition where the task was to predict smoker status based on bio-signals. The project involved advanced machine learning techniques, hyperparameter tuning with Optuna, and achieving a top 28% finish among 1908 teams.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Kaggle Binary Prediction", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Kaggle_Binary_Prediction)")

    st.markdown("---")

    # Project 9: HR Analytics Project (Sep - Oct 2023)
    st.markdown("### September - October 2023")
    st.subheader("**HR Analytics Project: Determine High Attrition Factors**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Conducted an HR analytics project focused on identifying factors contributing to high employee attrition. The project utilized data collection through PostgreSQL, data cleaning and wrangling with Excel, and interactive visualization using Tableau to present findings to stakeholders.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="HR Analytics", use_column_width=True)
        st.markdown("[View on Tableau](https://github.com/fahmizainal17/HR_Analytics_Project)")

    st.markdown("---")

    # Project 10: Neutron Flux Profiling Project (Jul - Sep 2022)
    st.markdown("### July - September 2022")
    st.subheader("**Neutron Flux Profiling at the End of Cycle (EOC) RTP Core Configuration**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        During my industrial training at the Malaysian Nuclear Agency, I was involved in the Neutron Flux Profiling Project, where I conducted measurements and analyses to ensure reactor safety. The project provided hands-on experience in nuclear technology and reactor safety protocols.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Neutron Flux Profiling", use_column_width=True)
        st.markdown("[View Project Documentation](https://github.com/fahmizainal17/Neutron_Flux_Profiling)")

# Call the show function if this script is executed directly
if __name__ == "__main__":
    show()
