import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Saurav Chavan | Data Analyst & Software Developer",
    page_icon="📊",
    layout="wide",
)

# 1. Hero Section
st.title("SAURAV SUMERSING CHAVAN")
st.subheader("Data Analyst | Python Developer | Freelance Solutions Specialist")
st.write(
    """
Professional Data Analyst and Software Developer specializing in converting complex business 
requirements into functional web applications, custom websites, and data-driven insights. 
Experienced in utilizing modern analytics tools and programming frameworks to deliver tailored solutions.
"""
)

st.divider()

# 2. Core Competencies & Education
col1, col2 = st.columns(2)

with col1:
    st.header("🛠️ Technical Skills")
    st.markdown(
        """
    - **Programming & Databases:** Python, SQL, Advanced Excel
    - **Data Analytics & Libraries:** Pandas, NumPy, Data Visualization, Jupyter Notebook
    - **Frameworks & Tools:** Streamlit, GitHub, Vercel, Canva Design
    """
    )

with col2:
    st.header("🎓 Education & Certification")
    st.markdown(
        """
    - **Data Science & Data Analytics:** Skillected Institute
    - **Bachelor of Commerce (B.Com):** Sant Gadge Baba Amravati University (72%)
    - **Higher Secondary Certificate (12th):** Maharashtra State Board (83%)
    - **Secondary School Certificate (10th):** Maharashtra State Board (70%)
    """
    )

st.divider()

# 3. Freelance Services Offered
st.header("💼 Professional Services")
s1, s2, s3 = st.columns(3)

with s1:
    st.subheader("📱 Custom App Development")
    st.write(
        "Designing and deploying bespoke web applications using Python and Streamlit to automate workflows and optimize operations based on specific client requirements."
    )

with s2:
    st.subheader("🌐 Web Development")
    st.write(
        "Building responsive, high-performance websites for businesses, personal branding, and portfolio representation."
    )

with s3:
    st.subheader("📊 Data Analytics & Reporting")
    st.write(
        "Performing exploratory data analysis, writing structured SQL queries, and generating actionable business intelligence reports."
    )

st.divider()

# 4. Featured Project
st.header("📁 Featured Project")

st.subheader("🚀 Abhyas Bharat")
st.write(
    "An educational data platform developed to streamline learning content and insights. Source code and documentation are publicly available on GitHub."
)
st.markdown(
    "[🔗 View 'Abhyas Bharat' Project on GitHub](https://github.com)"
)  # Update with your exact GitHub link

st.divider()

# 5. Contact Information
st.header("📫 Contact & Business Location")

c1, c2 = st.columns(2)

with c1:
    st.markdown("**Full Name:** Saurav Sumersing Chavan")
    st.markdown("**Business Establishment:** Shivraj Fire")
    st.markdown("**Location:** Malkapur, Dist. Buldhana, Maharashtra, India")

with c2:
    st.markdown("**Direct Contact:** [+91 7499458809](tel:7499458809)")
    st.markdown("**Professional Email:** contact@sauravchavan.com")
    st.markdown(
        "**Instagram Profile:** [@unseenreality_in](https://instagram.com/unseenreality_in)"
    )
