import streamlit as st

def show_feedback_and_discussion():
    st.title("Feedback & Discussion 💬")

    # Embed the Google Form in Streamlit
    st.markdown("""
    <iframe src="https://forms.gle/5oUAVTU7pYfXAMUu5" 
    width="640" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    """, unsafe_allow_html=True)

    st.markdown("**Recent Discussions**")
    st.text("Recent discussions could be listed here if you have a database or other methods to store and display them.")

# Call the function if this script is executed directly
if __name__ == "__main__":
    show_feedback_and_discussion()
