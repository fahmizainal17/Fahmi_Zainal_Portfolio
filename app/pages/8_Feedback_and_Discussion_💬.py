import streamlit as st
from PIL import Image
from streamlit_player import st_player

# Function to apply custom page style
def apply_page_style():
    custom_style = f"""
        <style>
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}
            
            /* Sidebar background using Unsplash image */
            [data-testid="stSidebar"] > div:first-child {{
                background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                                url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
                background-size: 180%;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: local;
            }}

            [data-testid="stHeader"] {{
                background: rgba(0,0,0,0);
            }}

            [data-testid="stToolbar"] {{
                right: 2rem;
            }}
        </style>
    """
    st.markdown(custom_style, unsafe_allow_html=True)

# Set the page layout to wide
st.set_page_config(layout="wide")

# Apply the page style to ensure the background matches the rest of the pages
apply_page_style()

def show_feedback_and_discussion():
    c1, c2 = st.columns([10,8])
    with c1:
        st.title("Feedback & Discussion 💬")
        
        # Call to action button to play YouTube song
        if st.button("🎵 Enjoy a Song While You Give Feedback"):
            st.session_state['play_song'] = True  # Store the state to control the YouTube player visibility

    with c2:
        # Check if the button was clicked to show the YouTube player
        if 'play_song' in st.session_state and st.session_state['play_song']:
            st_player("https://www.youtube.com/watch?v=VeUiVCb7ZmQ?si=GzSBUP3zs1hEkigI", height=140)

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
    st.image("photos/My_Photo/Round_Profile_Photo.jpg", width=150)  # Adjust the image path and size as needed
    
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
