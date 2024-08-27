import streamlit as st
from PIL import Image

# Set the page layout to wide
st.set_page_config(layout="wide")

def show_feedback_and_discussion():
    st.title("Feedback & Discussion 💬")
    
    st.markdown("---")

    # Center the Google Form in wide mode
    st.markdown("""
    <div style="display: flex; justify-content: center;">
        <iframe src="https://forms.gle/5oUAVTU7pYfXAMUu5" 
        width="800" height="900" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div>
    """, unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    # Profile Picture
    st.image("photos/Round_Profile_Photo.jpg", width=150)  # Adjust the image path and size as needed
    
    st.header("Let's Connect! 🌐")
    st.write("Tell me about your experience with this app! 🎉")

    # LinkedIn button
    linkedin_url = "https://www.linkedin.com/in/fahmizainal17"
    if st.button("Connect on LinkedIn"):
        st.write(f"[Visit my LinkedIn]({linkedin_url})")

    # GitHub button
    github_url = "https://github.com/fahmizainal17"
    if st.button("Check out my GitHub"):
        st.write(f"[Visit my GitHub]({github_url})")

    st.markdown("---")
    st.write("Thank you for taking the time to provide feedback and connect with me. Your insights are highly valued! 💌")

# Call the function if this script is executed directly
if __name__ == "__main__":
    show_feedback_and_discussion()
