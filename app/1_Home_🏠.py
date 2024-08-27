import streamlit as st
from streamlit_player import st_player
from component import page_style

page_style()

def show():
    # Main content with two columns: About section on the left and video on the right
    c1, c2 = st.columns([2, 1])  # Adjust column widths as necessary
    with c1:
        st.markdown("""
        ## About
        I am Muhammad Fahmi Bin Mohd Zainal, a passionate and results-driven Data Scientist with over two years of overall comprehensive experience in Data Science,Business Analytics, and Software Engineering. My expertise spans across Python, SQL, PowerBI, and machine learning, with a particular focus on designing and implementing data-driven solutions that optimize business processes and drive substantial revenue growth.

        Throughout my career, I have led and executed projects that significantly enhanced data processing efficiency and contributed to revenue increases ranging from 5 to 6 figures (RM) through predictive modeling, digital marketing, and market research. My capabilities extend to building interactive dashboards, engineering robust ETL pipelines, and deploying RESTful APIs, all while maintaining high standards in data integrity and security on platforms like Azure and AWS.

        At INVOKE Solutions, I lead initiatives in survey automation, where I design and implement innovative tools that drastically reduce manual processing time. My role also involves architecting and managing complex data warehouse infrastructures, developing predictive models, and deploying web applications that provide actionable insights to stakeholders. Additionally, I mentor aspiring data professionals and guide projects to successful completion, fostering a collaborative environment that encourages growth and excellence.

        My leadership experience is complemented by a strong foundation in business analytics, where I integrate data science principles with strategic business objectives to drive meaningful outcomes. I am dedicated to continuous learning and development, consistently staying ahead of the curve in the fast-evolving landscape of data science and technology.

        I invite you to connect with me on [LinkedIn](https://www.linkedin.com/in/fahmizainal17) and explore my work on [GitHub](https://github.com/fahmizainal17). Let's collaborate to leverage the power of data science in achieving exceptional business results.
        """)

    with c2:
        # Video Player
        st.markdown("## Video")
        url =  "https://youtu.be/xqoMugFukUI?si=-gl0J7FjverrD6Xy"
        st_player(url)

# Call the show function if this script is executed directly
if __name__ == "__main__":
    show()
