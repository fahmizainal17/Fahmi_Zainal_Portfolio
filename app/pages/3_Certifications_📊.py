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
            "title": "HRDC Sap Fundamentals",
            "date": "September 2024",
            "image": "photos/Certifications/Sap.jpeg",
            "organization": "HRD Corp - Human Resource Development Corporation",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "HRDC Autocad Volume 1",
            "date": "August 2024",
            "image": "photos/Certifications/Autocad_Volume_1.jpeg",
            "organization": "HRD Corp - Human Resource Development Corporation",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "HRDC Autocad Volume 2",
            "date": "August 2024",
            "image": "photos/Certifications/Autocad_Volume_2.jpeg",
            "organization": "HRD Corp - Human Resource Development Corporation",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "HRDC Microsoft Project",
            "date": "August 2024",
            "image": "photos/Certifications/Microsoft_Project.jpeg",
            "organization": "HRD Corp - Human Resource Development Corporation",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "MBOT HRDC Primavera P6 Module 1",
            "date": "August 2024",
            "image": "photos/Certifications/Primavera_P6_Volume_1.jpeg",
            "organization": "Malaysia Board of Technologists",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "MBOT HRDC Primavera P6 Module 2",
            "date": "August 2024",
            "image": "photos/Certifications/Primavera_P6_Volume_2.jpeg",
            "organization": "Malaysia Board of Technologists",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "Kunkwan Mandarin Conversation Class",
            "date": "July 2024",
            "image": "photos/Certifications/Kunkwan_Basic_Mandarin.jpeg",
            "organization": "Kunkwan International Mandarin Training Centre",
            "details_link": "https://kunkwan.com.my/contact/"
        },
        {
            "title": "MBOT HRDC Advanced Excel for Oil and Gas Module 3",
            "date": "July 2024",
            "image": "photos/Certifications/Advanced_Excel_Module_3.jpeg",
            "organization": "Malaysia Board of Technologists",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "MBOT HRDC OGM Microsoft Power BI for Oil and Gas Module 1",
            "date": "July 2024",
            "image": "photos/Certifications/Power_BI_Volume_1.jpeg",
            "organization": "Malaysia Board of Technologists",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "MBOT HRDC OGM Microsoft Power BI for Oil and Gas Module 2",
            "date": "July 2024",
            "image": "photos/Certifications/Power_BI_Volume_2.jpeg",
            "organization": "Malaysia Board of Technologists",
            "details_link": "https://oilandgasmeta.com/contact/"
        },
        {
            "title": "Kaggle Python Programming",
            "date": "November 2023",
            "image": "photos/Certifications/Kaggle_Python.jpeg",
            "organization": "Kaggle",
            "details_link": "https://www.kaggle.com/learn/certification/fahmizainal/python"
        },
        {
            "title": "Coursera Project Certificate - Working With Big Query",
            "date": "November 2023",
            "image": "photos/Certifications/Big_Query.png",
            "organization": "Coursera",
            "details_link": "https://www.coursera.org/account/accomplishments/certificate/NESXX5PWWJ4W"
        },
        {
            "title": "General Assembly Data Analytics",
            "date": "October 2023",
            "image": "photos/Certifications/Data_Analytics_Bootcamp.jpeg",
            "organization": "General Assembly",
            "details_link": "https://excelerate.asia/contact-us/"
        },
        {
            "title": "IBM Data Science Essentials",
            "date": "June 2023",
            "image": "photos/Certifications/IBM_Data_Science_Essential.png",
            "organization": "Coursera",
            "details_link": "https://www.coursera.org/account/accomplishments/certificate/V6SSW27VS2QP"
        },
        {
            "title": "IBM Data Visualization and Dashboards with Excel & Cognos Analytics",
            "date": "June 2023",
            "image": "photos/Certifications/IBM_Data_Visualization_and_Dashboarding.png",
            "organization": "Coursera",
            "details_link": "https://www.coursera.org/account/accomplishments/certificate/ERMW3M5VFLQK"
        },
        {
            "title": "IBMExcel Essentials for Data Analytics",
            "date": "June 2023",
            "image": "photos/Certifications/IBM_Excel_Essential.png",
            "organization": "Coursera",
            "details_link": "https://www.coursera.org/account/accomplishments/certificate/TP3VCQBC226U"
        },
        {
            "title": "Introduction to Data Analytics",
            "date": "June 2023",
            "image": "photos/Certifications/IBM_Data_Analytics_Essential.png",
            "organization": "Coursera",
            "details_link": "https://www.coursera.org/account/accomplishments/certificate/QXZ672AWA9VX"
        },
        {
            "title": "Job Interview Tips for Project Managers",
            "date": "June 2023",
            "image": "photos/Certifications/Job_Interview_Tips_For_Project_Manager.png",
            "organization": "LinkedIn",
            "details_link": "https://www.linkedin.com/learning/certificates/a34f0ddfa55c2ac3d1a2fcc58eecef39d779fdf201a743c5c3d0062dd5c118a3"
        },
        {
            "title": "LinkedIn Premium Quick Tips",
            "date": "June 2023",
            "image": "photos/Certifications/LinkedIn_Premium_Quick_Tips.png",
            "organization": "LinkedIn",
            "details_link": "https://www.linkedin.com/learning/certificates/9671eac03a397930a9bfbffc868907f06e81729d3eb11346b662d961260412e8"
        },
    ]

    for cert in certifications:
        c1, c2 = st.columns([1, 3.5])
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
            if cert['details_link']:
                st.markdown(f"[Details Link]({cert['details_link']})", unsafe_allow_html=True)

        # Add horizontal line after each certification
        st.markdown("---")

# Call the show_certifications function if this script is executed directly
if __name__ == "__main__":
    show_certifications()
