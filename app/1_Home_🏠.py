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
        I am Muhammad Fahmi Bin Mohd Zainal, a dynamic Data Scientist with over 2 years of experience in IT, data analytics, and data science. I have a strong proficiency in Python, SQL, PowerBI, Tableau, and machine learning, with a proven track record of leading projects that significantly enhance data processing efficiency and drive revenue growth ranging from 5 to 6 figures (RM) through predictive modeling, Digital Marketing, and Market Research Survey Projects. My expertise extends to developing interactive dashboards, designing ETL pipelines, creating and deploying RESTful APIs, and maintaining data warehouses on platforms like Azure and AWS. Additionally, I specialize in applying machine learning to Return on Ad Spend (ROAS) and digital marketing strategies and have a solid background in AWS DevOps.

        At INVOKE Solutions, I spearhead survey automation projects and lead the design of innovative data processing tools that cut down manual work time drastically. My role involves architecting data for various initiatives, developing predictive models, deploying web applications, and creating interactive ROAS dashboards that provide clear, actionable insights. My experience also includes maintaining complex data warehouse infrastructures, designing and deploying RESTful APIs, and hosting tech bootcamps to educate and inspire the next generation of data scientists. Connect with me on [LinkedIn](https://www.linkedin.com/in/fahmizainal17) and [GitHub](https://github.com/fahmizainal17) to explore how we can leverage data science and AI to drive impactful business outcomes.
        """)

    with c2:
        # Video Player
        st.markdown("## Video")
        url =  "https://youtu.be/xqoMugFukUI?si=-gl0J7FjverrD6Xy"
        st_player(url)

# Call the show function if this script is executed directly
if __name__ == "__main__":
    show()
