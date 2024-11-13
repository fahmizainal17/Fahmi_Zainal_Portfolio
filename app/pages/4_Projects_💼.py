import streamlit as st
from component import page_style

def show_projects():
    # Apply page style
    page_style()

    st.title("Projects 💼")

    # Project 1: Car Price Prediction Model (Aug 2024 - Sep 2024)
    st.markdown("### August 2024 - September 2024")
    st.subheader("**Car Price Prediction Model**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Car Price Prediction Model project aimed to create a robust machine learning model for predicting car prices using various features such as make, model, year, and mileage. The project involved extensive data preprocessing, including cleaning and feature engineering, to prepare the dataset for model training. Multiple machine learning algorithms were explored, and hyperparameter tuning was employed to achieve optimal model performance.

        The resulting model demonstrated high accuracy and was designed to be integrated seamlessly into car dealership websites and applications. It provides real-time price estimates based on current market trends, enhancing the buying and selling experience for users.

        The project highlights the effective use of machine learning techniques to solve practical problems in the automotive industry, providing valuable insights for stakeholders looking to understand market dynamics and price variations.
        """)
    with c2:
        st.image("photos/Projects/Car_Price_Prediction.jpg", caption="Car Price Prediction Model", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Car_Price_Prediction_Project)")

    st.markdown("---")

    # Project 2: Creating Endpoints for ROAS Dashboard (May 2024 - Aug 2024)
    st.markdown("### May 2024 - August 2024")
    st.subheader("**Creating Endpoints for ROAS Dashboard**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        This project focused on developing API endpoints to support a Return on Ad Spend (ROAS) Dashboard within the Databricks framework. The endpoints were designed to handle data retrieval and complex calculations necessary for digital marketing analytics. The project involved backend development, data manipulation, and integration with frontend services using NEXT.js.

        By leveraging Databricks, the project ensured efficient processing of large datasets, enabling marketers to access real-time insights and optimize their advertising strategies. The endpoints provide essential data to calculate key performance indicators (KPIs) for various digital marketing campaigns.

        Overall, the project successfully delivered a scalable solution for managing and analyzing digital marketing data, allowing businesses to make data-driven decisions and maximize their ROI.
        """)
    with c2:
        st.image("photos/Projects/Roas_Dashboard_Endpoints.png", caption="ROAS Dashboard Endpoints", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/FastAPI_ROAS_Dashboard_Project)")

    st.markdown("---")

    # Project 3: Digital Marketing Campaign Ad Set EDA and Ad Scoring (Jun 2024 - Aug 2024)
    st.markdown("### June 2024 - August 2024")
    st.subheader("**Digital Marketing Campaign Ad Set EDA and Ad Scoring**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Digital Marketing Campaign Ad Set EDA and Ad Scoring project aimed to analyze and score digital marketing ad sets through a combination of exploratory data analysis (EDA) and machine learning. This initiative involved examining ad performance data to develop a scoring mechanism that ranks ad sets based on their effectiveness.

        Collaborating with data scientists and backend developers, the project integrated the scoring system into a digital marketing platform, allowing users to evaluate and optimize their campaigns. The scoring model used various data points to predict campaign success and provided actionable insights for improving future ad strategies.

        The project contributed to a more data-driven approach to digital marketing, helping businesses understand what drives performance and how to allocate resources effectively.
        """)
    with c2:
        st.image("photos/Projects/Ad_Metrics.png", caption="Ad Set EDA and Scoring", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Digital_Marketing_Campaign_Ad_Set_EDA_and_Ad_Scoring)")

    st.markdown("---")

    # Project 4: Interactive Voice Response (IVR) Data Analysis Project (Nov 2023 - Aug 2024)
    st.markdown("### November 2023 - August 2024")
    st.subheader("**Interactive Voice Response (IVR) Data Analysis Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Interactive Voice Response (IVR) Data Analysis Project focused on enhancing customer experience and operational efficiency by analyzing IVR data. Utilizing Python, SQL, and Azure Databricks, the project involved cleaning and analyzing large datasets to extract meaningful insights.

        Key deliverables included detailed reports and visualizations that helped organizations understand customer interactions and improve their IVR systems. By identifying patterns and trends in the data, the project contributed to optimizing call flows and reducing handling times.

        The project played a vital role in transforming raw IVR data into actionable intelligence, supporting better decision-making for businesses relying on automated voice systems.
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
        This project involved analyzing data from the Google Ads Keyword Planner to identify cities with the highest search frequency for specific keywords. Using Python, a machine learning model based on K-Means clustering was developed to group cities by search behaviors, enabling more targeted digital marketing strategies.

        The project provided marketers with valuable insights into geographic patterns of consumer interest, allowing them to allocate their advertising resources more effectively. The clustering approach helped identify potential markets and tailor campaigns to specific regional audiences.

        By combining data science and digital marketing, the project demonstrated how machine learning can enhance strategic decision-making and optimize advertising efforts.
        """)
    with c2:
        st.image("photos/Projects/Keyword_Planner.png", caption="Search Frequency Clustering", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Machine_Learning_K-Means_Clustering_for_Search_Frequency_Project)")

    st.markdown("---")

    # Project 6: VBA Macro Generator for Charts Handling (Aug 2024)
    st.markdown("### August 2024")
    st.subheader("**VBA Macro Generator for Charts Handling**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The VBA Macro Generator for Charts Handling project aimed to automate the process of managing and arranging charts within presentations. Using a combination of Python, VBA, and Streamlit, the tool was developed to allow users to map chart templates easily, reducing the manual effort involved in chart customization and formatting.

        The project improved workflow efficiency by standardizing chart handling practices, ensuring consistency across presentations. It catered to users who frequently deal with data visualization, providing a streamlined solution to manage charts effectively.

        This automation tool has been widely adopted to save time and maintain high standards in data presentation.
        """)
    with c2:
        st.image("photos/Projects/VBA_Macro_Generator.png", caption="VBA Macro Generator", use_column_width=True)
        st.markdown("[View on Streamlit](https://vba-macro-generator.streamlit.app/)")

    st.markdown("---")

    # Project 7: Deployment Endpoints to AWS ECS and EC2 (Jun 2024 - Jul 2024)
    st.markdown("### June 2024 - July 2024")
    st.subheader("**Deployment Endpoints to AWS ECS and EC2**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        This project focused on deploying API endpoints to AWS Elastic Container Service (ECS) and Elastic Compute Cloud (EC2) to ensure the continuous operation of web applications. The deployment utilized AWS services for high availability and fault tolerance, critical for maintaining uninterrupted access to backend services.

        The project employed DevOps practices, such as infrastructure as code, CI/CD pipelines, and automated deployments, to create a robust and scalable environment. It enabled the seamless integration of APIs with front-end applications, supporting dynamic and interactive user experiences.

        This deployment strategy provided a reliable backend infrastructure, essential for modern web applications requiring high performance and resilience.
        """)
    with c2:
        st.image("photos/Projects/EC2_ECS.jpeg", caption="AWS Deployment", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/FastAPI_ROAS_Dashboard_Project)")

    st.markdown("---")

    # Project 8: Flood Prediction Project using TensorFlow and Keras (Jul 2024)
    st.markdown("### July 2024")
    st.subheader("**Flood Prediction Project using TensorFlow and Keras**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Flood Prediction Project utilized TensorFlow and Keras to create a model that predicts flood occurrences based on historical weather data. By analyzing large datasets, the model aimed to provide accurate and timely predictions, making it a valuable tool for disaster management and community preparedness.

        The project involved training the model on various features such as rainfall, temperature, and river levels to identify patterns that precede flooding events. It was designed to assist authorities in making informed decisions about emergency responses and resource allocation.

        This project demonstrated the application of machine learning to real-world problems, contributing to public safety and disaster resilience.
        """)
    with c2:
        st.image("photos/Projects/Tensorflow_Flood_Prediction.png", caption="Flood Prediction Model", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Tensorflow_Flood_Prediction_Project)")

    st.markdown("---")

    # Project 9: Unified Web Application Ecosystem with FastAPI and AWS (Feb 2024 - Jun 2024)
    st.markdown("### February 2024 - June 2024")
    st.subheader("**Unified Web Application Ecosystem with FastAPI and AWS**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Unified Web Application Ecosystem project developed a comprehensive solution to integrate Streamlit and Shiny frontends using FastAPI and AWS services. It involved creating a robust backend that handles data flow between different user interfaces, ensuring smooth interaction and performance.

        By leveraging containerization with Docker and deploying on AWS, the project provided a scalable and secure environment for web applications. It utilized modern development practices, including continuous integration and deployment (CI/CD), to streamline the workflow and reduce downtime.

        This project enabled seamless integration of diverse tools and frameworks, enhancing the flexibility and functionality of web applications.
        """)
    with c2:
        st.image("photos/Projects/Unified_Web_App.png", caption="Unified Web Application", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Streamlit_IVR_Data_Cleaning_Automation_Project)")

    st.markdown("---")

    # Project 10: Computer Vision Project (Mar 2024)
    st.markdown("### March 2024")
    st.subheader("**Computer Vision Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Computer Vision Project aimed to develop an API for detecting Metisa plana pupae in images, using the YOLOv5 model. It featured a FastAPI backend for making predictions and a Streamlit-based UI for visual demonstrations, creating an accessible interface for users to test the model.

        The project utilized Docker for deployment and incorporated tools such as Weights & Biases for performance tracking and Roboflow for dataset preparation. It provided an innovative solution for agricultural pest management by automating the identification process.

        By applying computer vision techniques, the project contributed to more efficient and accurate pest detection, supporting sustainable farming practices.
        """)
    with c2:
        st.image("photos/Projects/Metisa_plana_Bagworm.png", caption="Computer Vision Project", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Computer_Vision_Project)")

    st.markdown("---")

    # Project 11: Web Application Creation for Automating IVR Data Cleaning (Jan 2024 - Feb 2024)
    st.markdown("### January 2024 - February 2024")
    st.subheader("**Web Application for Automating IVR Data Cleaning**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Web Application for Automating IVR Data Cleaning was designed to simplify and streamline the data cleaning process for Interactive Voice Response (IVR) systems. Using Python and Streamlit, the application allowed users to upload, process, and download data files efficiently, reducing manual effort and error rates.

        The project provided an intuitive interface for users, ensuring that data cleaning tasks could be completed quickly and accurately. It significantly enhanced the overall efficiency of handling large volumes of IVR data, leading to better data quality and faster processing times.

        This tool has become a valuable asset for organizations managing large-scale IVR operations, ensuring smooth and accurate data handling.
        """)
    with c2:
        st.image("photos/Projects/IVR_Cleaner.png", caption="IVR Data Cleaning App", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Streamlit_IVR_Data_Cleaning_Automation_Project)")

    st.markdown("---")

    # Project 12: Containerization Using Docker Project (May 2024)
    st.markdown("### May 2024")
    st.subheader("**Containerization Using Docker Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Containerization Using Docker Project focused on deploying a FastAPI application using Docker, an open-source platform that packages applications into portable containers. The project enabled the application to run consistently across different environments, enhancing its scalability and flexibility.

        Development was carried out using a Linux environment set up with WSL, Ubuntu, and VS Code, providing a robust platform for building and testing the application. The project successfully demonstrated the benefits of containerization for managing dependencies and simplifying deployment processes.

        By adopting Docker, the project ensured a streamlined workflow and improved application portability, making it easier to manage and deploy across various environments.
        """)
    with c2:
        st.image("photos/Projects/Docker_Container.png", caption="Containerization Using Docker", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/FastAPI_ROAS_Dashboard_Project)")

    st.markdown("---")

    # Project 13: Creating Endpoints Using FastAPI Framework (Mar 2024 - May 2024)
    st.markdown("### March 2024 - May 2024")
    st.subheader("**Creating Endpoints Using FastAPI Framework**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        This project focused on developing RESTful API endpoints using the FastAPI framework to support a unified web application for survey automation. The endpoints were optimized for handling large volumes of data and were designed to provide fast, reliable access to survey data.

        The project involved building a robust backend that could efficiently process and serve data to front-end applications, enhancing the overall user experience. The use of FastAPI ensured a modern, high-performance architecture suitable for dynamic web applications.

        These endpoints are now integral to the survey automation platform, providing critical functionality for data access and manipulation.
        """)
    with c2:
        st.image("photos/Projects/FastAPI_Design.png", caption="FastAPI Endpoints", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/FastAPI_ROAS_Dashboard_Project)")

    st.markdown("---")

    # Project 14: Geocoding and Data Processing Projects (May 2024)
    st.markdown("### May 2024")
    st.subheader("**Geocoding and Data Processing Projects**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Geocoding and Data Processing Project involved using the Google Maps Geocoding API to convert geographic data, such as postcodes and localities, into precise latitude and longitude coordinates. This project was crucial for data analysis tasks that required accurate geographic information.

        Custom functions were developed to handle different levels of geographic data, enabling businesses and researchers to gain deeper insights into location-based trends and patterns. The processed data has been used in market research, demographic studies, and various other applications.

        The project showcased the effective integration of geocoding technology with data processing techniques, providing valuable tools for location-based analysis.
        """)
    with c2:
        st.image("photos/Projects/Geocoding_API.jpeg", caption="Geocoding and Data Processing", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Geocoding_API_and_Data_Modelling_Project)")

    st.markdown("---")

    # Project 15: Web Scraping (May 2024)
    st.markdown("### May 2024")
    st.subheader("**Web Scraping Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Web Scraping Project aimed to automate data extraction from various websites for market analysis and business insights. By utilizing Python libraries like BeautifulSoup and Scrapy, the project enabled efficient and systematic data collection from multiple online sources.

        The data was cleaned and structured for further analysis, supporting decision-making processes across different industries. This project provided a foundation for developing customized scraping tools tailored to specific data needs.

        The successful implementation of the project demonstrated the power of automation in gathering and processing large datasets for analytical purposes.
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
        This project utilized cloud-based tools like Azure Databricks and Google Colab to automate the process of phone number sanitization and sampling for survey data. By combining large-scale data processing capabilities with flexible scripting environments, the project enabled efficient preparation of survey datasets.

        The integration of Databricks and Colab allowed for streamlined workflows, reducing manual errors and enhancing data quality. This project played a crucial role in optimizing survey operations by automating repetitive tasks and ensuring consistent data handling practices.

        The project exemplified the use of cloud computing and data science techniques to solve practical problems in survey management.
        """)
    with c2:
        st.image("photos/Projects/Call_Sampling.png", caption="Call Sampling Techniques", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17)")

    st.markdown("---")

    # Project 17: The Live Calls Data Analysis Project (Dec 2023 - Jan 2024)
    st.markdown("### December 2023 - January 2024")
    st.subheader("**The Live Calls Data Analysis Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Live Calls Data Analysis Project aimed to enhance customer service and operational efficiency by analyzing data from live call sessions. The project involved data cleaning, sampling, weighting, cross-tabulation, and visualization to extract meaningful insights from call data.

        Tools such as Google Sheets, Excel, and Python were used to process and analyze the data, providing actionable insights into customer behavior and call center performance. The project helped identify trends and optimize call handling processes, leading to improved customer satisfaction and reduced operational costs.

        This project demonstrated the value of data analytics in transforming raw call data into strategic business insights.
        """)
    with c2:
        st.image("photos/Projects/Analytics_Live_Call.jpg", caption="Live Calls Data Analysis", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17)")

    st.markdown("---")

    # Project 18: Weighting Strata Project (Nov 2023 - Dec 2023)
    st.markdown("### November 2023 - December 2023")
    st.subheader("**Weighting Strata Project**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Weighting Strata Project utilized statistical methods to conduct weighting analysis on survey data using the R programming language in Databricks. The goal was to improve the representativeness of survey results by adjusting for various demographic factors.

        By applying advanced statistical techniques, the project ensured accurate and meaningful outcomes, enhancing the validity of survey-based studies. This project was critical for organizations relying on survey data for decision-making and policy development.

        The successful execution of the project demonstrated the importance of robust data analysis methods in ensuring the reliability of survey results.
        """)
    with c2:
        st.image("photos/Projects/Sample_Weighting.png", caption="Weighting Strata Project", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17])")

    st.markdown("---")

    # Project 19: Achieving Top 28% in Kaggle Playground Competition (Oct 2023 - Nov 2023)
    st.markdown("### October 2023 - November 2023")
    st.subheader("**Achieving Top 28% in Kaggle Playground Competition**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        This project involved competing in a Kaggle Playground Competition to predict smoker status from bio-signals, where the team achieved a top 28% ranking among 1908 teams. The competition provided an opportunity to apply various machine learning algorithms and refine model-building techniques.

        The project included extensive data preprocessing, feature engineering, and model tuning to achieve optimal results. It was a valuable experience in using data science for health-related applications, demonstrating the potential of machine learning in predicting health outcomes.

        Participation in the competition helped sharpen skills and gain insights into competitive data science challenges.
        """)
    with c2:
        st.image("photos/Projects/Binary_Prediction.png", caption="Kaggle Playground Competition", use_column_width=True)
        st.markdown("[View on Kaggle](https://github.com/fahmizainal17/Binary_Classification_Weighted_Ensemble_and_Optuna_Top_28)")

    st.markdown("---")

    # Project 20: Machine Learning Project to Predict Income Group (Nov 2023)
    st.markdown("### November 2023")
    st.subheader("**Machine Learning Project to Predict Income Group**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Machine Learning Project focused on developing a model to predict income groups based on survey data. The project covered the full lifecycle of model development, from data preprocessing and feature selection to training and evaluation.

        The model aimed to classify individuals into different income brackets, providing valuable insights for businesses and policymakers interested in socioeconomic analysis. The project utilized various machine learning techniques to achieve high predictive accuracy.

        This initiative demonstrated the application of data science to social and economic research, offering a tool for targeted interventions and informed decision-making.
        """)
    with c2:
        st.image("photos/Projects/Predict_IncomeGroup.png", caption="Income Group Prediction", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Machine_Learning_To_Predict_Salary_Project)")

    st.markdown("---")

    # Project 21: HR Analytics Project: Determining Factors of High Attrition (Sep 2023 - Oct 2023)
    st.markdown("### September 2023 - October 2023")
    st.subheader("**HR Analytics Project: Determining Factors of High Attrition**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The HR Analytics Project aimed to identify key factors contributing to high employee attrition rates. Data was collected and analyzed using PostgreSQL, Excel, and Tableau, allowing for a comprehensive examination of the various elements affecting employee turnover.

        By presenting the findings through interactive visualizations, the project provided HR teams with actionable insights into workforce management. It helped organizations understand the drivers of attrition and develop targeted retention strategies.

        This project highlighted the power of data analytics in human resource management, providing a foundation for data-driven decision-making in organizational development.
        """)
    with c2:
        st.image("photos/Projects/HR_Analytics.png", caption="HR Analytics Project", use_column_width=True)
        st.markdown("[View on Github & Tableau](https://github.com/fahmizainal17/HR_Analytics_Identifying_Key_Factors_Contributing_to_High_Employee_Attrition_Rates_Project)")

    st.markdown("---")

    # Project 22: Neutron Flux Profiling at the End of Cycle (Jul 2022 - Sep 2022)
    st.markdown("### July 2022 - September 2022")
    st.subheader("**Neutron Flux Profiling at the End of Cycle**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Neutron Flux Profiling project conducted detailed neutron flux measurements for the RTP core configuration at the Malaysian Nuclear Agency. The project included neutron activation analysis, radiation measurement, and data interpretation to contribute to reactor safety and operational efficiency.

        The profiling provided critical data for understanding the distribution of neutrons within the reactor, informing decisions on reactor management and safety protocols. The project played a significant role in optimizing reactor performance and ensuring compliance with safety standards.

        This work underscored the importance of accurate neutron flux measurements in maintaining nuclear reactor safety and efficiency.
        """)
    with c2:
        st.image("photos/Projects/Neutron_Flux_Profiling.png", caption="Neutron Flux Profiling", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Neutron_Flux_Profiling_at_the_End_of_Cycle_Project)")
    st.markdown("---")

    # Project 23: Effect of Neutron Irradiation on Borosilicate Glass Slide (Jan 2021 - Jun 2022)
    st.markdown("### January 2021 - June 2022")
    st.subheader("**Effect of Neutron Irradiation on Borosilicate Glass Slide**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The study focused on examining the effects of neutron irradiation on borosilicate glass slides used in radiation dosimetry. Advanced techniques like FTIR and Raman spectroscopy were employed to analyze changes in the glass's thermoluminescence properties.

        The research provided insights into the structural changes that occur in glass materials when exposed to neutron radiation, contributing to the development of improved radiation detection methods. The findings have applications in medical physics, nuclear safety, and materials science.

        This project highlighted the intersection of physics and materials science in understanding the behavior of materials under radiation exposure.
        """)
    with c2:
        st.image("photos/Projects/neutron_irradiation.jpg", caption="Neutron Irradiation Study", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Effect_of_Neutron_Irradiation_on_Borosilicate_Glass_Slide_Project)")

    st.markdown("---")

    # Project 24: Optical Characterization of Gamma Irradiated Microscope Glass Slide (Jun 2021 - Jun 2022)
    st.markdown("### June 2021 - June 2022")
    st.subheader("**Optical Characterization of Gamma Irradiated Microscope Glass Slide**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        This project involved the optical characterization of microscope glass slides exposed to gamma radiation from a 60Co source. The study utilized Raman, FTIR, and photoluminescence spectroscopies to investigate changes in the slides' structural and luminescent properties.

        The research provided valuable data on how gamma radiation affects glass materials, which is crucial for applications in radiation shielding, imaging, and therapy. The project contributed to a better understanding of material responses to radiation at a molecular level.

        This work demonstrated the use of advanced spectroscopic techniques to explore the effects of radiation on materials.
        """)
    with c2:
        st.image("photos/Projects/Photoluminescence.png", caption="Gamma Irradiated Glass Study", use_column_width=True)
        st.markdown("[View Study](https://github.com/fahmizainal17/Optical_Characterization_of_Gamma_Irradiated_Microscope_Glass_Slide_Project)")

    st.markdown("---")

    # Project 25: Other Contributions (Various Dates)
    
    st.subheader("**Other Contributions**")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        In addition to the major projects listed, there have been numerous other contributions across different domains, including maintaining legacy handover projects, participating in collaborative initiatives, and supporting data science and machine learning efforts. These projects have covered a wide range of topics, from digital marketing to scientific research, showcasing a diverse set of skills and interests.

        Through these contributions, a consistent focus on innovation, process improvement, and the application of data-driven approaches has been maintained. The work has consistently aimed to push the boundaries of what is possible, leveraging the latest technologies and methodologies.

        These contributions reflect a commitment to continuous learning, growth, and making meaningful impacts across various fields.
        """)
    with c2:
        st.image("photos/Projects/Future_Project.jpeg", caption="Other Contributions", use_column_width=True)
        st.markdown("[View All Projects](https://github.com/fahmizainal17)")


    # Call the show function if this script is executed directly
if __name__ == "__main__":
    show_projects()
