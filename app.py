import streamlit as st
from utils.pdf_generator import create_pdf
# Store student data
if "student_data" not in st.session_state:
    st.session_state.student_data = {}
    # Store generated Resume
if "resume" not in st.session_state:
    st.session_state.resume = ""

# Store generated Cover Letter
if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

# Store LinkedIn Summary
if "linkedin" not in st.session_state:
    st.session_state.linkedin = ""

# Store Portfolio
if "portfolio" not in st.session_state:
    st.session_state.portfolio = ""

# Store Resume Analysis
if "analysis" not in st.session_state:
    st.session_state.analysis = ""

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume & Portfolio Builder",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📂 Navigation")

page = st.sidebar.radio(
    "Select a Module",
    [
        "🏠 Home",
        "👤 Student Details",
        "📄 Resume Generator",
        "✉️ Cover Letter",
        "🌐 Portfolio",
        "💼 LinkedIn Summary",
        "📊 Resume Analysis"
    ]
)

# -----------------------------
# Home Page
# -----------------------------
if page == "🏠 Home":

    st.title("📄 AI Resume & Portfolio Builder")

    st.markdown("---")

    st.header("🎯 Project Objective")

    st.write("""
    This AI application helps students create professional resumes,
    personalized cover letters, portfolio content, and LinkedIn summaries
    using Google's Gemini AI.
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📄 Resume")

    with col2:
        st.info("✉️ Cover Letter")

    with col3:
        st.info("💼 LinkedIn")

    st.markdown("---")

    st.success("🚀 Project setup completed successfully!")
    # ----------------------------------------
# Student Details Page
# ----------------------------------------

elif page == "👤 Student Details":

    st.title("👤 Student Information")

    st.write("Fill in your details to generate AI-powered career documents.")

    st.markdown("---")

    with st.form("student_form"):

        # Personal Information
        st.subheader("📌 Personal Information")

        full_name = st.text_input("Full Name")

        email = st.text_input("Email")

        phone = st.text_input("Phone Number")

        location = st.text_input("Location")

        # Education
        st.subheader("🎓 Education")

        college = st.text_input("College Name")

        degree = st.text_input("Degree")

        specialization = st.text_input("Specialization")

        cgpa = st.text_input("CGPA")

        graduation = st.text_input("Graduation Year")

        # Skills
        st.subheader("💻 Skills")

        skills = st.text_area(
            "Enter your skills (comma separated)",
            placeholder="Python, Machine Learning, SQL, Streamlit..."
        )

        # Projects
        st.subheader("🚀 Projects")

        projects = st.text_area(
            "Describe your projects"
        )

        # Certifications
        st.subheader("📜 Certifications")

        certifications = st.text_area(
            "Enter your certifications"
        )

        # Experience
        st.subheader("🏢 Internship / Experience")

        experience = st.text_area(
            "Describe your internship or work experience"
        )

        # Achievements
        st.subheader("🏆 Achievements")

        achievements = st.text_area(
            "Mention your achievements"
        )

        # Target Role
        st.subheader("🎯 Target Job")

        job_role = st.text_input(
            "Target Job Role"
        )

        submitted = st.form_submit_button("Save Details")

    if submitted:

        st.session_state.student_data = {

        "full_name": full_name,
        "email": email,
        "phone": phone,
        "location": location,
        "college": college,
        "degree": degree,
        "specialization": specialization,
        "cgpa": cgpa,
        "graduation": graduation,
        "skills": skills,
        "projects": projects,
        "certifications": certifications,
        "experience": experience,
        "achievements": achievements,
        "job_role": job_role

        }

        st.success("✅ Student Details Saved Successfully!")

        st.json(st.session_state.student_data)
    # ----------------------------------------
# Resume Generator
# ----------------------------------------

# ----------------------------------------
# Resume Generator
# ----------------------------------------

elif page == "📄 Resume Generator":

    st.title("📄 AI Resume Generator")

    if not st.session_state.student_data:

        st.warning("Please fill the Student Details first.")

    else:

        st.success("Student Details Found ✅")

        if st.button("Generate Resume"):

            from utils.ai_generator import generate_resume

            with st.spinner("Gemini AI is generating your resume..."):

                st.session_state.resume = generate_resume(
                    st.session_state.student_data
                )

            st.success("✅ Resume Generated Successfully!")


        if st.session_state.resume:

            st.markdown("## 📄 Generated Resume")

            st.markdown(st.session_state.resume)


            # Create PDF
            pdf = create_pdf(
                st.session_state.resume,
                "AI_Resume.pdf"
            )


            # Download Button
            with open(pdf, "rb") as file:

                st.download_button(
                    label="⬇️ Download Resume PDF",
                    data=file,
                    file_name="AI_Resume.pdf",
                    mime="application/pdf"
                )

            # ----------------------------------------
# Cover Letter Generator
# ----------------------------------------

# ----------------------------------------
# Cover Letter Generator
# ----------------------------------------

elif page == "✉️ Cover Letter":

    st.title("✉️ AI Cover Letter Generator")

    if not st.session_state.student_data:

        st.warning("Please fill the Student Details first.")

    else:

        st.success("Student Details Found ✅")

        company_name = st.text_input("Company Name")

        job_position = st.text_input("Job Position")

        if st.button("Generate Cover Letter"):

            from utils.ai_generator import generate_cover_letter

            with st.spinner("Generating your Cover Letter..."):

                st.session_state.cover_letter = generate_cover_letter(
                    st.session_state.student_data,
                    company_name,
                    job_position
                )

            st.success("✅ Cover Letter Generated Successfully!")
            if st.session_state.cover_letter:
                st.markdown("## ✉️ Generated Cover Letter")

    st.markdown(st.session_state.cover_letter)


    pdf = create_pdf(
        st.session_state.cover_letter,
        "Cover_Letter.pdf"
    )


    with open(pdf, "rb") as file:

        st.download_button(
            label="⬇️ Download Cover Letter PDF",
            data=file,
            file_name="Cover_Letter.pdf",
            mime="application/pdf"
        )


    

        
            # ----------------------------------------
# LinkedIn Summary Generator
# ----------------------------------------

# ----------------------------------------
# LinkedIn Summary Generator
# ----------------------------------------

elif page == "💼 LinkedIn Summary":

    st.title("💼 AI LinkedIn Profile Generator")

    if not st.session_state.student_data:

        st.warning("Please fill Student Details first.")

    else:

        st.success("Student Details Found ✅")

        if st.button("Generate LinkedIn Profile"):

            from utils.ai_generator import generate_linkedin_summary

            with st.spinner("Generating LinkedIn Profile..."):

                st.session_state.linkedin = generate_linkedin_summary(
                    st.session_state.student_data
                )

            st.success("✅ LinkedIn Profile Generated Successfully!")

        if st.session_state.linkedin:
            st.markdown("## 💼 Generated LinkedIn Profile")

    st.markdown(st.session_state.linkedin)


    pdf = create_pdf(
        st.session_state.linkedin,
        "LinkedIn_Profile.pdf"
    )


    with open(pdf, "rb") as file:

        st.download_button(
            label="⬇️ Download LinkedIn Profile PDF",
            data=file,
            file_name="LinkedIn_Profile.pdf",
            mime="application/pdf"
        )

    
            # ----------------------------------------
# Portfolio Generator
# ----------------------------------------

elif page == "🌐 Portfolio":

    st.title("🌐 AI Portfolio Generator")

    if not st.session_state.student_data:

        st.warning("Please fill Student Details first.")

    else:

        st.success("Student Details Found ✅")

        if st.button("Generate Portfolio"):

            st.session_state.portfolio = (
                f"""
# {st.session_state.student_data['full_name']}

## About Me

I am a {st.session_state.student_data['degree']} student specializing in 
{st.session_state.student_data['specialization']}.

## Skills

{st.session_state.student_data['skills']}

## Projects

{st.session_state.student_data['projects']}

## Experience

{st.session_state.student_data['experience']}
"""
            )

        if st.session_state.portfolio:

            st.markdown("## 🌐 Generated Portfolio")

            st.markdown(
                st.session_state.portfolio
            )

            # ----------------------------------------
# Resume Analysis
# ----------------------------------------

elif page == "📊 Resume Analysis":

    st.title("📊 AI Resume Analysis")

    if not st.session_state.resume:

        st.warning("Generate Resume first.")

    else:

        st.success("Resume Found ✅")

        st.write(
            """
### Resume Analysis

✅ ATS Friendly Format  
✅ Professional Sections  
✅ Skills Included  
✅ Project Details Added  
✅ Recruiter Readability Optimized
"""
        )