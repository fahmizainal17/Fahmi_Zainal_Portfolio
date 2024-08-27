import streamlit as st
from component import page_style

def show():
    # Apply page style
    page_style()

    st.title("Achievements 🏆")
    
    st.markdown("---")
    
    # Project 1: Car Price Prediction Model
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("""
        **Car Price Prediction Model**

        Developed a machine learning model to predict car prices based on various features like make, model, year, and mileage. The project involved data cleaning, feature engineering, model selection, and hyperparameter tuning. The model achieved high accuracy and is available for integration into car dealership websites or applications for price estimation.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Car Price Prediction Model", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Car_Price_Prediction_Model)")

    st.markdown("---")

    # Project 2: Flood Prediction Project
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        **Flood Prediction Project using TensorFlow and Keras**

        This project utilizes the TensorFlow and Keras frameworks to predict flood occurrences based on historical weather data. The model was trained on large datasets and optimized for real-time predictions, making it a valuable tool for disaster management agencies and communities prone to flooding.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Flood Prediction Project", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Flood_Prediction_Project_utilizing_Tensorflow_Keras_Framework)")
    
    st.markdown("---")

    # Project 3: FastAPI ROAS Dashboard
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        **FastAPI ROAS Dashboard**

        Developed a Return on Ad Spend (ROAS) dashboard using FastAPI. The dashboard allows digital marketers to monitor and optimize their advertising spend by providing insights into the performance of various ad campaigns. The API backend was built with FastAPI, and the frontend was developed using a modern web framework.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="FastAPI ROAS Dashboard", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/FastAPI_ROAS_Dashboard)")
    
    st.markdown("---")

    # Project 4: Machine Learning to Predict Salary
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        **Machine Learning to Predict Salary**

        This project focuses on predicting employee salaries based on job titles, experience, education, and location. The machine learning model was trained on a large dataset and provides accurate salary predictions, helping HR professionals and job seekers make informed decisions.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Machine Learning to Predict Salary", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Machine_Learning_To_Predict_Salary_Project)")

    st.markdown("---")

    # Project 5: Streamlit IVR Data Automation Project
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        **Streamlit IVR Data Automation Project**

        This project automates the processing of Interactive Voice Response (IVR) data using Streamlit. It provides a user-friendly interface for uploading IVR data, performing data cleaning, and generating detailed reports. The project is designed to streamline data processing workflows and improve efficiency.
        """)
    with c2:
        st.image("photos/Round_Profile_Photo.jpg", caption="Streamlit IVR Data Automation Project", use_column_width=True)
        st.markdown("[View on GitHub](https://github.com/fahmizainal17/Streamlit_IVR_Data_Automation_Project)")

# Call the show function if this script is executed directly
if __name__ == "__main__":
    show()
