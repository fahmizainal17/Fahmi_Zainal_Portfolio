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
        Meet Fahmi Zainal, a visionary in the world of data science, where numbers transform into strategies and insights become growth. As a Senior Data Scientist, Fahmi brings nearly two years of specialized experience in turning raw data into game-changing business outcomes, with a unique blend of skills in Python, SQL, machine learning, and PowerBI.

        Fahmi's passion lies in crafting intelligent solutions that make data not just powerful, but irresistible. He has led high-impact projects that didn't just improve data efficiency—they revolutionized it, driving revenue leaps from thousands to six-figure success stories through predictive analytics, digital marketing, and market research.

        At INVOKE Solutions, Fahmi doesn't just build tools; he redefines possibilities. His work in survey automation slashes manual efforts to a fraction, architecting sophisticated data ecosystems that fuel faster, smarter decisions. With a flair for guiding teams and mentoring the next generation of data wizards, Fahmi thrives on collaboration, innovation, and the relentless pursuit of excellence.

        Fahmi's approach is simple: leverage data as the ultimate catalyst for business growth. He marries deep technical prowess with strategic thinking, driving forward outcomes that matter. Constantly on the frontier of new technologies, Fahmi is always learning, always evolving, and always ready to take on the next challenge.

        Ready to harness the power of data science for extraordinary impact? Connect with Fahmi on [LinkedIn](https://www.linkedin.com/in/fahmizainal17) or explore his innovative projects on [GitHub](https://github.com/fahmizainal17). Let's turn insights into incredible results—together.
        """)

    with c2:
        # Video Player
        st.markdown("## Video")
        url =  "https://youtu.be/vC7m-u0-qXg?si=yII1DzWfcf9qB8-9"
        st_player(url)

if __name__ == "__main__":
    show()

# Future fb