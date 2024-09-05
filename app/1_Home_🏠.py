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
        Fahmi Zainal is a highly skilled and results-driven Senior Data Scientist with over two years of comprehensive experience in Data Science, Analytics, Digital Marketing, and Software Development. He possesses expertise in Python, SQL, PowerBI, and machine learning, with a strong emphasis on designing and implementing data-driven solutions that optimize business processes and drive substantial revenue growth.

        Throughout his career, Fahmi has successfully led and executed projects that have significantly enhanced data processing efficiency and contributed to revenue increases ranging from 5 to 6 figures (RM) through predictive modeling, digital marketing, and market research. His skill set extends to building interactive dashboards, engineering robust ETL pipelines, and deploying RESTful APIs, all while maintaining high standards in data integrity and security on platforms like Azure and AWS.

        At INVOKE Solutions, Fahmi leads initiatives in survey automation, where he designs and implements innovative tools that drastically reduce manual processing time. His role involves architecting and managing complex data warehouse infrastructures, developing predictive models, and deploying web applications that provide actionable insights to stakeholders. In addition to his technical contributions, he mentors aspiring data professionals and guides projects to successful completion, fostering a collaborative environment that encourages growth and excellence.

        Fahmi's leadership experience is complemented by a strong foundation in business analytics, where he integrates data science principles with strategic business objectives to drive meaningful outcomes. He is dedicated to continuous learning and development, consistently staying ahead of the curve in the fast-evolving landscape of data science and technology.

        You can connect with Fahmi on [LinkedIn](https://www.linkedin.com/in/fahmizainal17) and explore his work on [GitHub](https://github.com/fahmizainal17). He is always open to collaborations that leverage the power of data science to achieve exceptional business results.
        """)

    with c2:
        # Video Player
        st.markdown("## Video")
        url =  "https://youtu.be/vC7m-u0-qXg?si=yII1DzWfcf9qB8-9"
        st_player(url)

# Call the show function if this script is executed directly
if __name__ == "__main__":
    show()
