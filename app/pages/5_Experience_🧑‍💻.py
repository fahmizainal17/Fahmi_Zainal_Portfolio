import streamlit as st
from PIL import Image
from component import page_style

def show_experience():
    # Apply page style
    page_style()

    st.title("Experience 🧑‍💻")
    
    # Experience list
    experiences = [
        {
            "company": "INVOKE Solutions",
            "logo": "photos/Experience_Company_Logo/Invoke_Logo.png",
            "positions": [
                {
                    "position": "**Senior Data Scientist**",
                    "duration": "Jul 2024 - Present · 3 mos",
                    "location": "Kuala Lumpur, Malaysia · Full-time",
                    "description": """
                        - Led development of data pipelines and architecture using Airflow, Talend, and AWS, enhancing data integrity and reducing processing times by 80%.
                        - Developed predictive models and dashboards that improved user satisfaction and led to a 10% revenue increase.
                        - Managed data solutions for client projects, improving data accuracy by 95% and enhancing collaboration across teams.
                        - Supervised a team of interns and junior scientists, increasing project completion rates by 30%.
                        - Utilized a range of technologies including AWS, GitHub Actions, SQL Server Integration Services (SSIS), and Linux systems.
                    """,
                    "skills": "Airflow, Linux Architecture, GitHub Actions, Amazon EC2, Data Integrity, CI/CD, AWS ECR"
                },
                {
                    "position": "**Data Scientist**",
                    "duration": "Nov 2023 - Jul 2024 · 9 mos",
                    "location": "Selangor, Malaysia · Full-time",
                    "description": """
                        - Spearheaded the design and implementation of Data Cleaner and Keypress Decoder tools, reducing data processing time by 80%.
                        - Developed a Unified Web Application using Streamlit and Shiny Apps, optimizing team collaboration with Python and R.
                        - Directed survey projects involving sampling, data processing, weighting, and visualization, enhancing data accuracy by 20%.
                        - Engineered data solutions that improved geographical and demographic data accuracy by 95%.
                        - Designed predictive models and enhanced the ROAS Dashboard, increasing data visualization efficiency by 25%.
                    """,
                    "skills": "REST APIs, Linux Architecture, Microsoft Azure, Computer Vision, Predictive Modeling, Streamlit, Data Science, Deep Learning"
                }
            ]
        },
        {
            "company": "Excelerate Asia",
            "logo": "photos/Experience_Company_Logo/Excelerate_Asia_Logo.png",
            "position": "**Data Analyst**",
            "duration": "Mar 2023 - Nov 2023 · 9 mos",
            "location": "Kuala Lumpur, Malaysia · Full-time",
            "description": """
                - Analyzed HR data to uncover patterns in employee termination, optimizing recruitment and retention strategies.
                - Led projects in Business Analytics, improving data accuracy to above 90% and developing streamlined dashboards for insights.
                - Developed skills in SQL, Tableau, and data cleaning to enhance operational efficiency and data management.
            """,
            "skills": "Microsoft Power BI, Linux, Project Management, SQL, Tableau, Data Analytics, Streamlit"
        },
        {
            "company": "Malaysian Nuclear Agency",
            "logo": "photos/Experience_Company_Logo/Nuclear_Agency_Logo.png",
            "position": "**Research Officer Trainee**",
            "duration": "Jul 2022 - Sep 2022 · 3 mos",
            "location": "Bandar Baru Bangi, Selangor, Malaysia · Internship",
            "description": """
                - Contributed to research on neutron flux profiling at Reactor TRIGA PUSPATI (RTP), increasing research findings by 25%.
                - Managed research data and implemented a data management system, reducing discrepancies by 15%.
                - Collaborated with researchers, receiving commendations for teamwork and presentation skills.
            """,
            "skills": "Teamwork, Data Management, Research and Development (R&D), Data Science, Presentation Skills"
        },
        {
            "company": "I Synergy Group Ltd (ASX: IS3)",
            "logo": "photos/Experience_Company_Logo/ISynergy_Logo.png",
            "position": "**Affiliate Marketing Specialist**",
            "duration": "Jan 2019 - Jun 2022 · 3 yrs 6 mos",
            "location": "Kuala Lumpur, Malaysia · Full-time",
            "description": """
                - Acquired and expanded a substantial user base for the MySmartShopper app, boosting customer acquisition and revenue.
                - Recruited and mentored affiliates, building a team of 21 and achieving Regional Partner status.
                - Developed marketing strategies and partnership initiatives that increased brand visibility and customer engagement.
            """,
            "skills": "Marketing Strategy, Team Leadership, Customer Acquisition, Multi-level Marketing"
        },
        {
            "company": "Malaysian Army (Tentera Darat)",
            "logo": "photos/Experience_Company_Logo/Army_Logo.png",
            "positions": [
                {
                    "position": "**Second Lieutenant Reserved Officer**",
                    "duration": "Feb 2023 - Present · 1 yr 8 mos",
                    "location": "Kuala Lumpur, Malaysia · Part-time",
                    "description": """
                        - Commissioned by the Yang di-Pertuan Agong for outstanding leadership in the Reserve Officer Training Unit (ROTU).
                        - Led and mentored trainees, achieving top performance evaluations and enhancing training outcomes by 30%.
                        - Managed logistics and tactical operations, reducing supply losses by 15% and improving operational efficiency.
                        - Represented the Army at national events, recognized for superior leadership and communication skills.
                    """,
                    "skills": "Project Management, Coaching, Team Management, Leadership"
                },
                {
                    "position": "**Army Cadet Reserved Officer**",
                    "duration": "Sep 2019 - Feb 2023 · 3 yrs 6 mos",
                    "location": "Kuala Lumpur, Malaysia · Part-time",
                    "description": """
                        - Developed leadership skills through training exercises and simulations, earning commendations for quick decision-making.
                        - Managed logistics and recruit training, fostering a team-oriented environment.
                        - Mastered basic weapon handling and tactical operations.
                    """,
                    "skills": "Teamwork, Leadership, Problem Solving"
                }
            ]
        },
        {
            "company": "J&T EXPRESS (MALAYSIA) SDN BHD",
            "logo": "photos/Experience_Company_Logo/JTExpress_Logo.png",
            "position": "**Courier Driver Specialist**",
            "duration": "Jan 2019 - May 2022 · 3 yrs 5 mos",
            "location": "Cheras, Selangor, Malaysia · Freelance",
            "description": """
                - Achieved a 98% on-time delivery rate by optimizing delivery routes and implementing new logistics strategies.
                - Improved customer satisfaction through problem-solving and communication, receiving a 95% positive feedback rating.
                - Managed deliveries of diverse parcel sizes, ensuring efficient and secure transport across various locations.
            """,
            "skills": "Teamwork, Communication, Logistics Management"
        },
        {
            "company": "McDonald's",
            "logo": "photos/Experience_Company_Logo/McDonalds_Logo.png",
            "position": "**Food And Beverage Specialist**",
            "duration": "Jan 2018 - Sep 2018 · 9 mos",
            "location": "Putrajaya, Malaysia · Part-time",
            "description": """
                - Managed kitchen operations and inventory, ensuring seamless service and high food quality.
                - Excelled in customer service, enhancing the dining experience and promoting teamwork among colleagues.
                - Demonstrated financial management skills, handling restaurant finances and payroll with accuracy.
            """,
            "skills": "Teamwork, Leadership, Communication"
        },
    ]

    for exp in experiences:
        c1, c2 = st.columns([1, 7], gap="small")
        with c1:
            st.image(exp["logo"], use_column_width=True)
        with c2:
            if 'positions' in exp:  # Handle multiple positions in the same company
                for position in exp['positions']:
                    st.subheader(position['position'])
                    st.write(f"**{position['duration']} · {position['location']}**")
                    st.markdown(position['description'])
                    st.write(f"**Skills:** {position['skills']}")
            else:
                st.subheader(exp['position'])
                st.write(f"**{exp['duration']} · {exp['location']}**")
                st.markdown(exp['description'])
                st.write(f"**Skills:** {exp['skills']}")
        
        # Add horizontal line after each experience
        st.markdown("---")

# Call the show_experience function if this script is executed directly
if __name__ == "__main__":
    show_experience()
