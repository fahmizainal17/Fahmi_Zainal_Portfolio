import streamlit as st
from component import page_style

def show_achievements():
    # Apply page style
    page_style()

    st.title("Achievements 🏆")

    # Achievement 1: Development of In-House Data Processing and Reporting Automation Tool
    st.markdown("### Development of In-House Data Processing and Reporting Automation Tool")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Led the development of a comprehensive in-house tool that streamlined the entire data processing and reporting workflow for survey data. This tool integrated a full suite of functionalities, including IVR Data Cleaning, Questionnaire Definition, Keypress Decoding, Survey Weighting, Cross-Tabulation, Survey Chart Generation, VBA Macro Automation for chart customization, and Report Summary Metrics Generation. By automating these processes, the tool reduced data preparation and reporting time from 8 hours to just 30 minutes, significantly enhancing operational efficiency and data quality.

        The tool automated key steps in the data management workflow, from initial data cleaning and weighting to the generation of cross-tabulations and visualizations. The Survey VBA Macro Generator provided accurate chart options and streamlined the arrangement process, ensuring consistent and professional visual outputs. Additionally, the report summary metrics generator enabled quick creation of comprehensive reports, facilitating fast, data-driven decision-making and freeing up valuable resources.

        This in-house solution has become a cornerstone of the organization's data management capabilities, greatly improving the efficiency of survey processing and reporting. By reducing manual work and minimizing errors, the tool ensures high-quality data outputs and quicker turnaround times for client deliverables.
        """)
    with c2:
        st.image("photos/Achievements/Survey_Tools.png", caption="In-House Data Processing Tool", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Streamlit_IVR_Data_Cleaning_Automation_Project)")

    st.markdown("---")

    # Achievement 2: Model Development for ROAS and Campaign Benchmarking
    st.markdown("### Model Development for ROAS and Campaign Benchmarking")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Model Development for ROAS (Return on Ad Spend) and Campaign Benchmarking project was a high-impact, strategic initiative that redefined the organization’s approach to digital marketing analytics. This project developed a suite of predictive models that analyzed consumer behaviors, market trends, and campaign performance, directly contributing to a 10% increase in overall revenue. By converting complex datasets into actionable insights, the project empowered the company to make smarter, data-driven decisions, enhancing client engagement and optimizing marketing spend.

        Central to the project was the creation of advanced ETL pipelines and the use of state-of-the-art data storage and processing technologies, such as MongoDB, Databricks, and Azure Blob Storage. These tools enabled efficient management of large marketing datasets, while sophisticated machine learning algorithms identified critical patterns and trends that drive successful campaigns. The models offered unprecedented clarity into customer behavior, enabling the organization to strategically allocate resources and anticipate market shifts.

        This project underscored the critical role of data science in improving core business functions. It demonstrated the organization’s ability to seamlessly integrate advanced technology with business processes, fostering a robust, adaptable framework for continuous growth and competitive advantage in a dynamic market landscape.
        """)
    with c2:
        st.image("photos/Achievements/Roas_Dashboard.png", caption="ROAS and Campaign Benchmarking", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/FastAPI_ROAS_Dashboard_Project)")

    st.markdown("---")

    # Achievement 3: Top 28% in Binary Prediction Competition on Smoker Status
    st.markdown("### Top 28% in Binary Prediction Competition on Smoker Status")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        Secured a top 28% ranking among 1908 global teams in the highly competitive Binary Prediction Competition on Smoker Status, showcasing the team’s advanced proficiency in machine learning and data science. The competition required participants to develop models that could accurately predict smoker status using complex bio-signal data, a challenge that demanded innovative solutions and the deployment of a variety of advanced algorithms, including logistic regression, random forest, and ensemble tree-based models like Gradient Boosting, LightGBM, XGBoost, and CatBoost.

        A pivotal factor in the team’s success was the implementation of a Weighted Ensemble method, which combined predictions from multiple models to maximize accuracy. This approach was meticulously optimized using Optuna, a cutting-edge hyperparameter optimization framework, allowing for the fine-tuning of model parameters to achieve a remarkable ROC-AUC score of 0.8718 (87% accuracy). This strategic combination of diverse machine learning techniques and innovative optimization underscored the team's capability to solve complex classification problems effectively.

        This accomplishment demonstrated the organization’s expertise in competing on an international level, applying advanced data science techniques to real-world healthcare challenges. The project provided valuable experience in model optimization and further solidified the team's reputation as leaders in the application of machine learning to critical health data problems.
        """)
    with c2:
        st.image("photos/Achievements/Binary_Prediction.png", caption="Binary Prediction Competition", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Binary_Classification_Weighted_Ensemble_and_Optuna_Top_28)")

    st.markdown("---")

    # Achievement 4: Flood Prediction Project Using Deep Learning
    st.markdown("### Flood Prediction Project Using Deep Learning")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        The Flood Prediction Project was an innovative effort that leveraged deep learning to address one of the most pressing environmental challenges: accurate flood forecasting. Using the TensorFlow Keras framework, the team developed a robust neural network model capable of analyzing vast datasets of historical weather data—such as rainfall, river levels, and temperature—to predict flood occurrences with high precision. This model became a crucial tool for disaster management agencies, providing timely and reliable forecasts that helped mitigate the impacts of floods on at-risk communities.

        The model achieved an impressive accuracy rate of up to 84%, demonstrating its ability to identify complex patterns in environmental data. The development process involved rigorous experimentation, testing multiple neural network architectures and fine-tuning hyperparameters to optimize predictive performance. The model’s deployment in real-world scenarios validated its utility in informing emergency response strategies and resource allocation, offering actionable insights for flood preparedness.

        By applying deep learning to environmental data, this project highlighted the transformative potential of artificial intelligence in public safety and disaster management. It established the organization as a leader in innovative AI applications, reinforcing its commitment to leveraging technology to solve critical societal challenges.
        """)
    with c2:
        st.image("photos/Achievements/Tensorflow_Flood_Prediction.png", caption="Flood Prediction Project", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Tensorflow_Flood_Prediction_Project)")

    st.markdown("---")

    # Placeholder for Future Achievements
    st.markdown("### Future Achievements")
    st.write("Stay tuned for upcoming achievements and projects. I am continuously working on innovative solutions and new initiatives to drive growth and excellence across various domains.")
    st.image("photos/Achievements/Future_Project.jpeg", caption="Future Achievements", use_column_width=True)

    st.markdown("---")

# Call the show_certifications function if this script is executed directly
if __name__ == "__main__":
    show_achievements()