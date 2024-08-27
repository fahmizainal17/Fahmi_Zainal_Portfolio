import streamlit as st
from PIL import Image
from component import page_style

def show_certifications():
    # Apply page style
    page_style()

    st.title("Certifications 📊")
    
    # Certifications list
    certifications = [
        {
            "title": "Certified Kubernetes Administrator (CKA)",
            "date": "August 2023",
            "image": "photos/Round_Profile_Photo.jpg",
            "organization": "The Linux Foundation",
            "details_link": "https://www.credly.com/badges/cka-badge"
        },
        {
            "title": "Certified DevOps Foundation",
            "date": "July 2023",
            "image": "photos/Round_Profile_Photo.jpg",
            "organization": "CCSD Europe",
            "details_link": "https://www.credly.com/badges/devops-badge"
        },
        {
            "title": "IBM Data Analytics Essentials",
            "date": "June 2023",
            "image": "photos/Round_Profile_Photo.jpg",
            "organization": "IBM",
            "details_link": "https://www.credly.com/badges/ibm-analytics-badge"
        },
        # Add more certifications as needed
    ]

    for cert in certifications:
        c1, c2 = st.columns([1, 4])
        with c1:
            st.image(cert["image"], use_column_width=True)
        with c2:
            st.markdown(f"""
                <div class="cert-card">
                    <div class="cert-content">
                        <div>
                            <div class="cert-title">{cert['title']}</div>
                            <div class="cert-date">{cert['date']}</div>
                            <div>{cert['organization']}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"[View Certification]({cert['details_link']})", unsafe_allow_html=True)

        # Add horizontal line after each certification
        st.markdown("---")

# Call the show_certifications function if this script is executed directly
if __name__ == "__main__":
    show_certifications()
