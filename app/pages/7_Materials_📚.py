import streamlit as st
import hmac
from component import page_style

# Apply the page style
page_style()

# Title for the Materials section
st.title("Materials 📚")

# Password check function
def check_password():
    """Returns `True` if the user has the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        # Access the secret password from the secrets.toml file
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
            st.balloons()  # Show snow effect on successful login
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password with a hint
    st.text_input("Password (Hint: Frozen peep 🐧)", type="password", on_change=password_entered, key="password")
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 Password incorrect.")
    return False

# Create tabs for different categories
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Documentation & Reports", "Presentations & Slides", "Code Repositories", "Datasets & Tools", "Certificate Videos"]
)

# Tab 1: Documentation & Reports
with tab1:
    st.subheader("Documentation & Reports")
    st.markdown("""
    - **[Project Report: Data Analysis Documentation](https://databox.com/data-analysis-report)**: A general project report guidance on data analysis practices and methodologies.
    - **[API Documentation: FastAPI Integration](https://swagger.io/tools/swaggerhub/)**: Comprehensive API documentation for integrating FastAPI with existing systems.
    - **[White Paper: Data Science Best Practices](https://medium.com/bitgrit-data-science-publication/10-best-practices-for-data-science-21a748a410e4)**: An in-depth white paper on data science best practices.
    """)

# Tab 2: Presentations & Slides
with tab2:
    st.subheader("Presentations & Slides")
    st.markdown("""
    - **[Conference Talk: Data Science in Practice](https://www.slideshare.net/)**: Slides from my talk on data science in practice.
    - **[Workshop: Advanced Machine Learning](https://www.coursera.org/learn/advanced-machine-learning)**: Materials from a workshop on advanced machine learning techniques.
    - **[Webinar: Building APIs with FastAPI](https://fastapi.tiangolo.com/tutorial/)**: Webinar slides and recording on building APIs.
    """)

# Tab 3: Code Repositories
with tab3:
    st.subheader("Code Repositories & Scripts")
    st.markdown("""
    - **[GitHub Repository: MyProject](https://github.com/fahmizainal17)**: Source code and documentation for MyProject.
    - **[Python Script: Data Cleaning Utility](https://realpython.com/python-data-cleaning-numpy-pandas/)**: A utility script for data cleaning following best practices.
    - **[Jupyter Notebooks: EDA & Modeling](https://nbviewer.jupyter.org/)**: Jupyter notebooks used for exploratory data analysis and modeling.
    """)

# Tab 4: Datasets & Tools
with tab4:
    st.subheader("Datasets & Tools")
    st.markdown("""
    - **[Public Dataset](https://www.kaggle.com/datasets)**: Raw, cleaned, and processed dataset from Kaggle.
    - **[Custom Tool: Data Pipeline Automation](https://airflow.apache.org/)**: A custom tool for automating data pipelines.
    - **[Cheat Sheet: Python for Data Science](https://www.datacamp.com/community/data-science-cheatsheets)**: A quick-reference guide for Python in data science.
    """)

# Tab 5: Certificate Videos (Password Protected)
with tab5:
    st.subheader("Certificate Videos (Password Protected)")

    # Check if the user has entered the correct password
    if check_password():
        # Display all the confidential content from secrets.toml
        st.markdown(st.secrets["confidential_content"])
    else:
        st.write("🔒 Enter the correct password to access this content.")
