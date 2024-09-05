import streamlit as st
from component import page_style

def show():
    # Apply page style
    page_style()

    st.title("Projects 💼")

    # Project 1: Car Price Prediction Model (Aug 2024 - Sep 2024)
    st.markdown("### August 2024 - September 2024")
    st.subheader("**Car Price Prediction Model**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a machine learning model to predict car prices based on various features like make, model, year, and mileage. The project involved data cleaning, feature engineering, model selection, and hyperparameter tuning. The model achieved high accuracy and is available for integration into car dealership websites or applications for price estimation.
        """)
    with c2:
        st.image("photos/Projects/Car_Price_Prediction.jpg", caption="Car Price Prediction Model", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Car_Price_Prediction_Model)")

    st.markdown("---")

    # Project 2: Creating Endpoints for ROAS Dashboard (May 2024 - Aug 2024)
    st.markdown("### May 2024 - August 2024")
    st.subheader("**Creating Endpoints for ROAS Dashboard**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed API endpoints within the Databricks framework to power a Return on Ad Spend (ROAS) Dashboard. The project aimed at enabling data retrieval and calculations for digital marketing analytics. The project involved backend processing, data manipulation, and integration with frontend services using NEXT.js.
        """)
    with c2:
        st.image("photos/Projects/Roas_Dashboard_Endpoints.png", caption="ROAS Dashboard Endpoints", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/ROAS_Dashboard_API_Endpoints)")

    st.markdown("---")

    # Project 3: Digital Marketing Campaign Ad Set EDA and Ad Scoring (Jun 2024 - Aug 2024)
    st.markdown("### June 2024 - August 2024")
    st.subheader("**Digital Marketing Campaign Ad Set EDA and Ad Scoring**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a model to analyze and score digital marketing ad sets based on extensive data analysis and machine learning algorithms. This project involved collaboration with other data scientists and backend developers to integrate the scoring system into a digital marketing platform.
        """)
    with c2:
        st.image("photos/Projects/Ad_Metrics.png", caption="Ad Set EDA and Scoring", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Digital_Marketing_Ad_Scoring)")

    st.markdown("---")

    # Project 4: Interactive Voice Response (IVR) Data Analysis Project (Nov 2023 - Aug 2024)
    st.markdown("### November 2023 - August 2024")
    st.subheader("**Interactive Voice Response (IVR) Data Analysis Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Interactive Voice Response (IVR) Data Analysis Project aims to improve customer experience and operational efficiency by analyzing IVR data. It includes data cleaning, analysis, visualization, and reporting, utilizing Python, SQL, and Azure Databricks for scalable analytics.
        """)
    with c2:
        st.image("photos/Projects/IVR_Analytics.jpg", caption="IVR Data Analysis", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/IVR_Data_Analysis_Project)")

    st.markdown("---")

    # Project 5: Machine Learning Project by Implementing K-Means Clustering (Jul 2024 - Aug 2024)
    st.markdown("### July 2024 - August 2024")
    st.subheader("**Machine Learning Project: K-Means Clustering for Search Frequency**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Extracted data from Google Ads Keyword Planner and analyzed it using Python to identify cities with the highest search frequency. Developed a machine learning model using K-Means clustering to provide recommendations for digital marketing strategies.
        """)
    with c2:
        st.image("photos/Projects/Keyword_Planner.png", caption="Search Frequency Clustering", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Search_Frequency_Clustering)")

    st.markdown("---")

    # Project 6: VBA Macro Generator for Charts Handling (Aug 2024)
    st.markdown("### August 2024")
    st.subheader("**VBA Macro Generator for Charts Handling**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a VBA Macro Generator to automate chart handling and arrangement within presentations. Utilized Python, VBA, and Streamlit to enable users to map chart templates easily, reducing manual effort and improving workflow efficiency.
        """)
    with c2:
        st.image("photos/Projects/VBA_Macro_Generator.png", caption="VBA Macro Generator", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/VBA_Macro_Generator_for_Charts)")

    st.markdown("---")

    # Project 7: Deployment Endpoints to AWS ECS and EC2 (Jun 2024 - Jul 2024)
    st.markdown("### June 2024 - July 2024")
    st.subheader("**Deployment Endpoints to AWS ECS and EC2**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Deployed API endpoints to AWS ECS and EC2, ensuring continuous operation and availability. This project utilized DevOps practices, including IAM roles, ECR, ECS, EC2, load balancing, and CI/CD pipelines with GitHub Actions.
        """)
    with c2:
        st.image("photos/Projects/EC2_ECS.jpeg", caption="AWS Deployment", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/AWS_Endpoints_Deployment)")

    st.markdown("---")

    # Project 8: Flood Prediction Project using TensorFlow and Keras (Jul 2024)
    st.markdown("### July 2024")
    st.subheader("**Flood Prediction Project using TensorFlow and Keras**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Utilized TensorFlow and Keras frameworks to predict flood occurrences based on historical weather data. The model was trained on large datasets and optimized for real-time predictions, making it a valuable tool for disaster management agencies and communities prone to flooding.
        """)
    with c2:
        st.image("photos/Projects/Tensorflow_Flood_Prediction.png", caption="Flood Prediction Model", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Flood_Prediction_Project)")

    st.markdown("---")

    # Project 9: Unified Web Application Ecosystem with FastAPI and AWS (Feb 2024 - Jun 2024)
    st.markdown("### February 2024 - June 2024")
    st.subheader("**Unified Web Application Ecosystem with FastAPI and AWS**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a unified web application ecosystem that bridges Streamlit and Shiny frontends using FastAPI and AWS services. The project involved extensive backend development, containerization with Docker, and deployment using AWS ECS and API Gateway.
        """)
    with c2:
        st.image("photos/Projects/Unified_Web_App.png", caption="Unified Web Application", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Unified_Web_Application_Ecosystem)")

    st.markdown("---")

    # Project 10: Computer Vision Project (Mar 2024)
    st.markdown("### March 2024")
    st.subheader("**Computer Vision Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The FGV-Metisa Plana API project aims to develop an API using YOLOv5 for detecting Metisa plana pupae in images, featuring a FastAPI backend for predictions and a Streamlit-based UI for demonstrations. The project involves training and deploying the model using Docker, with plans for cloud deployment on AWS ECS and ECR. It also utilizes tools like Weights & Biases for performance tracking and Roboflow for dataset preparation. Currently, the project is on hold pending client feedback after the proof of concept.
        """)
    with c2:
        st.image("photos/Projects/Computer_Vision.png", caption="Computer Vision Project", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Computer_Vision_Project)")

    st.markdown("---")

    # Project 11: Web Application Creation for Automating IVR Data Cleaning (Jan 2024 - Feb 2024)
    st.markdown("### January 2024 - February 2024")
    st.subheader("**Web Application for Automating IVR Data Cleaning**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a web application to automate the IVR data cleaning process using Python and Streamlit. The application includes data upload, processing, and download functionalities, significantly improving data cleaning efficiency.
        """)
    with c2:
        st.image("photos/Projects/IVR_Cleaner.png", caption="IVR Data Cleaning App", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/IVR_Data_Cleaning_App)")

    st.markdown("---")

    # Project 12: Containerization Using Docker Project (May 2024)
    st.markdown("### May 2024")
    st.subheader("**Containerization Using Docker Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        For deploying a FastAPI app to AWS, utilized Docker, an open-source platform for containerization. This project involved setting up a Linux environment using WSL, Ubuntu (GUI), and VS Code for development and deployment.
        """)
    with c2:
        st.image("photos/Projects/Docker_Container.png", caption="Containerization Using Docker", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Containerization_Docker_Project)")

    st.markdown("---")

    # Project 13: Creating Endpoints Using FastAPI Framework (Mar 2024 - May 2024)
    st.markdown("### March 2024 - May 2024")
    st.subheader("**Creating Endpoints Using FastAPI Framework**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed and implemented several RESTful API endpoints using the FastAPI framework to support a unified web application for survey automation. This project improved backend efficiency and enhanced data processing speed.
        """)
    with c2:
        st.image("photos/Projects/FastAPI_Design.png", caption="FastAPI Endpoints", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/FastAPI_Endpoints_Project)")

    st.markdown("---")

    # Project 14: Geocoding and Data Processing Projects (May 2024)
    st.markdown("### May 2024")
    st.subheader("**Geocoding and Data Processing Projects**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Utilized the Google Maps Geocoding API to map and geocode postcodes, districts, localities, and points of interest for data analysis and processing. Developed custom data processing functions to handle different geographic levels.
        """)
    with c2:
        st.image("photos/Projects/Geocoding_API.jpeg", caption="Geocoding and Data Processing", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Geocoding_Data_Processing_Project)")

    st.markdown("---")

    # Project 15: Web Scraping (May 2024)
    st.markdown("### May 2024")
    st.subheader("**Web Scraping Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed and deployed a web scraping tool to extract data from multiple sources for market analysis and insights. The project involved using Python libraries like BeautifulSoup and Scrapy to automate data extraction and processing.
        """)
    with c2:
        st.image("photos/Projects/Web_Scraper.jpeg", caption="Web Scraping", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Web_Scraping_Project)")

    st.markdown("---")

    # Project 15: Call Sampling Techniques by Azure Databricks and Google Colab (Dec 2023 - Jan 2024)
    st.markdown("### December 2023 - January 2024")
    st.subheader("**Call Sampling Techniques by Azure Databricks and Google Colab**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Leveraged cloud computing and data processing to automate phone number sanitization and sampling from survey data. Combined Azure Databricks for large-scale processing with Google Colab for flexible, script-based data manipulation.
        """)
    with c2:
        st.image("photos/Projects/Call_Sampling.png", caption="Call Sampling Techniques", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Call_Sampling_Techniques)")

    st.markdown("---")

    # Project 17: The Live Calls Data Analysis Project (Dec 2023 - Jan 2024)
    st.markdown("### December 2023 - January 2024")
    st.subheader("**The Live Calls Data Analysis Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Focused on enhancing customer service and operational efficiency by analyzing live call data. The project involved data cleaning, sampling, weighting, cross-tabulation, and visualization using tools like Google Sheets, Excel, and Python.
        """)
    with c2:
        st.image("photos/Projects/Analytics_Live_Call.jpg", caption="Live Calls Data Analysis", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Live_Calls_Data_Analysis_Project)")

    st.markdown("---")

    # Project 18: Weighting Strata Project (Nov 2023 - Dec 2023)
    st.markdown("### November 2023 - December 2023")
    st.subheader("**Weighting Strata Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Conducted weighting analysis using the R programming language in Databricks. This project aimed to optimize data representation for survey results by applying statistical techniques to ensure accurate and meaningful outcomes.
        """)
    with c2:
        st.image("photos/Projects/Sample_Weighting.png", caption="Weighting Strata Project", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Weighting_Strata_Project)")

    st.markdown("---")

    # Project 19: Achieving Top 28% in Kaggle Playground Competition (Oct 2023 - Nov 2023)
    st.markdown("### October 2023 - November 2023")
    st.subheader("**Achieving Top 28% in Kaggle Playground Competition**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Collaborated in a Kaggle Playground Competition to predict smoker status from bio-signals, achieving top 28% among 1908 teams. Utilized multiple machine learning algorithms and hyperparameter tuning to optimize model performance.
        """)
    with c2:
        st.image("photos/Projects/Binary_Prediction.png", caption="Kaggle Playground Competition", use_column_width=True)
        st.markdown("[View on Kaggle](https://www.kaggle.com/fahmizainal17/competition-entry)")

    st.markdown("---")

    # Project 20: Machine Learning Project to Predict Income Group (Nov 2023)
    st.markdown("### November 2023")
    st.subheader("**Machine Learning Project to Predict Income Group**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Developed a machine learning model to predict income groups based on survey data. The project covered data preprocessing, model development, performance evaluation, and future deployment strategies for real-time predictions.
        """)
    with c2:
        st.image("photos/Projects/Predict_IncomeGroup.png", caption="Income Group Prediction", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Income_Prediction_Model)")

    st.markdown("---")

    # Project 21: HR Analytics Project: Determining Factors of High Attrition (Sep 2023 - Oct 2023)
    st.markdown("### September 2023 - October 2023")
    st.subheader("**HR Analytics Project: Determining Factors of High Attrition**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Conducted data analysis to identify key factors contributing to high employee attrition rates. Data was collected using PostgreSQL, cleaned and wrangled with Excel, and presented using interactive visualizations in Tableau.
        """)
    with c2:
        st.image("photos/Projects/HR_Analytics.png", caption="HR Analytics Project", use_column_width=True)
        st.markdown("[View on Tableau](https://public.tableau.com/fahmizainal17/HR_Analytics)")

    st.markdown("---")

    # Project 22: Neutron Flux Profiling at the End of Cycle (Jul 2022 - Sep 2022)
    st.markdown("### July 2022 - September 2022")
    st.subheader("**Neutron Flux Profiling at the End of Cycle**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Conducted neutron flux profiling for the RTP core configuration at the Malaysian Nuclear Agency. This involved neutron activation analysis, sample preparation, radiation measurement, and contributing to reactor safety and efficiency.
        """)
    with c2:
        st.image("photos/Projects/Neutron_Flux_Profiling.png", caption="Neutron Flux Profiling", use_column_width=True)
        st.markdown("[View Report](https://drive.google.com/fahmizainal17/Neutron_Flux_Profiling_Report)")

    st.markdown("---")

    # Project 23: Effect of Neutron Irradiation on Borosilicate Glass Slide (Jan 2021 - Jun 2022)
    st.markdown("### January 2021 - June 2022")
    st.subheader("**Effect of Neutron Irradiation on Borosilicate Glass Slide**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Explored the effects of neutron irradiation on borosilicate glass slides for radiation dosimetry. The study involved utilizing advanced techniques like FTIR and Raman spectroscopy to analyze thermoluminescence properties.
        """)
    with c2:
        st.image("photos/Projects/neutron_irradiation.jpg", caption="Neutron Irradiation Study", use_column_width=True)
        st.markdown("[View on ResearchGate](https://www.researchgate.net/fahmizainal17/Borosilicate_Glass_Study)")

    st.markdown("---")

    # Project 24: Optical Characterization of Gamma Irradiated Microscope Glass Slide (Jun 2021 - Jun 2022)
    st.markdown("### June 2021 - June 2022")
    st.subheader("**Optical Characterization of Gamma Irradiated Microscope Glass Slide**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Conducted a detailed study on the structural interaction changes and luminescence characteristics in microscope glass slides exposed to 60Co gamma-ray sources, leveraging Raman, FTIR, and PL spectroscopies.
        """)
    with c2:
        st.image("photos/Projects/GammaCell.jpeg", caption="Gamma Irradiated Glass Study", use_column_width=True)
        st.markdown("[View Study](https://arxiv.org/fahmizainal17/Optical_Characterization_Glass)")

    st.markdown("---")

    # Project 25: Other Contributions (Various Dates)
    st.markdown("### Various Dates")
    st.subheader("**Other Contributions**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Contributed to various other projects, including maintaining legacy handover projects, participating in collaborative initiatives, and supporting multiple data science and machine learning endeavors across different domains.
        """)
    with c2:
        st.image("Fahmi_Zainal_Portfolio/photos/Projects/future_project.jpg.jpg", caption="Other Contributions", use_column_width=True)
        st.markdown("[View All Projects](https://github.com/fahmizainal17)")


    # Call the show function if this script is executed directly
if __name__ == "__main__":
    show()
