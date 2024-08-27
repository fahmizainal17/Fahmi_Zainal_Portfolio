import streamlit as st
from PIL import Image
from component import page_style

def show_education():
    # Apply page style
    page_style()

    st.title("Education 🎓")
    
    # Education list
    education_list = [
        {
            "institution": "University of Malaya",
            "logo": "photos/UM_Logo.png",
            "degree": "**Bachelor of Science in Physics**",  # Using Markdown for bold
            "duration": "2017 - 2021",
            "location": "Kuala Lumpur, Malaysia",
            "description": """
                - Graduated with Honors in Physics.
                - Completed a thesis on "Quantum Computing and Its Applications in Cryptography".
                - Active member of the Physics Society and Student Council.
            """
        },
        {
            "institution": "University of Malaya",
            "logo": "photos/UM_Logo.png",
            "degree": "**Foundation in Physical Sciences**",  # Using Markdown for bold
            "duration": "2013 - 2017",
            "location": "Kuala Lumpur, Malaysia",
            "description": """
                - Graduated as Valedictorian.
                - Participated in national-level science fairs and debates.
                - Captained the school’s robotics team to win the state championship.
            """
        },
        # Add more education items as needed
    ]

    for edu in education_list:
        c1, c2 = st.columns([1, 7], gap="small")
        with c1:
            st.image(edu["logo"], use_column_width=True)
        with c2:
            st.subheader(edu['degree'])  # Using subheader for degree title
            st.markdown(f"""
                <div class="education-card">
                    <div class="education-content">
                        <div class="education-date-location">{edu['duration']} · {edu['location']}</div>
                    </div>
                    <div class="education-description">
                        {edu['description']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Add horizontal line after each education item
        st.markdown("---")

# Call the show_education function if this script is executed directly
if __name__ == "__main__":
    show_education()
