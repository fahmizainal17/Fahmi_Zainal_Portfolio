import streamlit as st
from PIL import Image
from component import page_style

def show_experience():
    # Apply page style
    page_style()

    st.title("Experience 💼")
    
    # Experience list
    experiences = [
        {
            "company": "INVOKE Solutions",
            "logo": "photos/Experience_Company_Logo/Invoke_Logo.png",
            "position": "**Senior Data Scientist**",  # Using Markdown for bold
            "duration": "Jul 2024 - Present · 2 mos",
            "location": "Federal Territory of Kuala Lumpur, Malaysia",
            "description": """
                - Led the design and implementation of the Data Cleaner, Questionnaire Definer, and Keypress Decoder, utilizing Streamlit Web App, reducing data processing time by 80%.
                - Directed survey projects ranging from Sampling, Data Processing, Weighting, and Visualization utilizing Google Colab, Azure Databricks, and Custom Web Applications, increasing data accuracy by 20%.
                - Developed and integrated Unified Web Applications using Streamlit and Shiny Apps, enhancing team collaboration utilizing Python and R Programming.
                - Engineered data solutions for clients, improving geographical and demographic data accuracy by 95% utilizing Geocoding API.
            """,
            "skills": "Airflow · Linux Architecture · GitHub Actions · Amazon EC2 · Data Integrity · CI/CD · AWS ECR"
        },
        {
            "company": "Kaggle",
            "logo": "photos/Experience_Company_Logo/Kaggle_Logo.png",  
            "position": "**Data Scientist**",  # Using Markdown for bold
            "duration": "Mar 2023 - Present · 1 yr 6 mos",
            "location": "Kuala Lumpur, Malaysia · Remote",
            "description": """
                - Participated and contributed actively in the Real World Data Machine Learning Project Competition.
                - Achieved top 28% ranking out of 1908 teams in a Binary Prediction Competition on Smoker Status Using Bio-Signals, leveraging logistic regression, random forest, and tree-boosted algorithms such as Gradient Boosting, LightGBM, XGBoost, and CatBoost.
                - Planned the work meticulously, conducting nightly meetings to discuss strategies and optimize models using Optuna for hyperparameter tuning.
            """,
            "skills": "Linux Architecture · Linux · Coaching · Shell Scripting · Git · Microsoft Azure Databricks · Data Management"
        },
        # Add more experiences as needed
    ]

    for exp in experiences:
        c1, c2 = st.columns([1, 7], gap="small")
        with c1:
            st.image(exp["logo"], use_column_width=True)
        with c2:
            st.subheader(exp['position'])  # Using subheader for position title
            st.markdown(f"""
                <div class="exp-card">
                    <div class="exp-content" style="display: flex; align-items: center;">
                        <div>
                            <div class="exp-date-location">{exp['duration']} · {exp['location']}</div>
                        </div>
                    </div>
                    <div class="exp-description">
                        {exp['description']}
                    </div>
                    <div class="exp-skills">
                        Skills: {exp['skills']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Add horizontal line after each experience
        st.markdown("---")

# Call the show_experience function if this script is executed directly
if __name__ == "__main__":
    show_experience()
