import streamlit as st
from component import page_style

page_style()

# Title for the Materials section
st.title("Materials 📚")

# Create tabs for different categories
tab1, tab2, tab3, tab4 = st.tabs(["Documentation & Reports", "Presentations & Slides", "Code Repositories", "Datasets & Tools"])

# Tab 1: Documentation & Reports
with tab1:
    st.subheader("Documentation & Reports")
    st.markdown("""
    - **[Project Report: XYZ Analysis](https://link-to-your-report.com)**: A detailed analysis report on XYZ.
    - **[API Documentation](https://link-to-your-docs.com)**: Comprehensive API documentation for the XYZ system.
    - **[White Paper: Data Science Best Practices](https://link-to-whitepaper.com)**: An in-depth white paper on data science best practices.
    """)

# Tab 2: Presentations & Slides
with tab2:
    st.subheader("Presentations & Slides")
    st.markdown("""
    - **[Conference Talk: Data Science in Practice](https://link-to-slides.com)**: Slides from my talk on data science in practice.
    - **[Workshop: Advanced Machine Learning](https://link-to-workshop.com)**: Materials from a workshop on advanced machine learning techniques.
    - **[Webinar: Building APIs with FastAPI](https://link-to-webinar.com)**: Webinar slides and recording on building APIs.
    """)

# Tab 3: Code Repositories
with tab3:
    st.subheader("Code Repositories & Scripts")
    st.markdown("""
    - **[GitHub Repository: MyProject](https://github.com/yourusername/myproject)**: Source code and documentation for MyProject.
    - **[Python Script: Data Cleaning Utility](https://link-to-script.com)**: A utility script for data cleaning.
    - **[Jupyter Notebooks: EDA & Modeling](https://link-to-notebook.com)**: Jupyter notebooks used for exploratory data analysis and modeling.
    """)

# Tab 4: Datasets & Tools
with tab4:
    st.subheader("Datasets & Tools")
    st.markdown("""
    - **[Public Dataset: ABC Data](https://link-to-dataset.com)**: A cleaned and processed dataset used for ABC analysis.
    - **[Custom Tool: Data Pipeline Automation](https://link-to-tool.com)**: A custom tool for automating data pipelines.
    - **[Cheat Sheet: Python for Data Science](https://link-to-cheatsheet.com)**: A quick-reference guide for Python in data science.
    """)

# You can add more tabs and categories as needed.
