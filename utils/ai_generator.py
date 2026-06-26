import os
from dotenv import load_dotenv
from google import genai

# Load the .env file
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"
print("Loading .env from:", env_path)
load_dotenv(dotenv_path=env_path)

# Read the API key
API_KEY = os.getenv("GEMINI_API_KEY")
print("Gemini API loaded successfully.")

# Check if API key exists
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please check your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def generate_resume(student_data):

    prompt = f"""
You are an expert ATS Resume Writer.

Create a professional ATS-friendly resume using the information below.

Name: {student_data['full_name']}
Email: {student_data['email']}
Phone: {student_data['phone']}
Location: {student_data['location']}

College: {student_data['college']}
Degree: {student_data['degree']}
Specialization: {student_data['specialization']}
CGPA: {student_data['cgpa']}
Graduation Year: {student_data['graduation']}

Skills:
{student_data['skills']}

Projects:
{student_data['projects']}

Experience:
{student_data['experience']}

Certifications:
{student_data['certifications']}

Achievements:
{student_data['achievements']}

Target Job:
{student_data['job_role']}

Generate a resume with these sections:

1. Professional Summary
2. Technical Skills
3. Education
4. Projects
5. Experience
6. Certifications
7. Achievements

Format it professionally.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
def generate_cover_letter(student_data, company_name, job_position):

    prompt = f"""
You are a professional HR Manager.

Write a professional cover letter.

Candidate Details

Name: {student_data['full_name']}
Email: {student_data['email']}
Phone: {student_data['phone']}
Location: {student_data['location']}

College:
{student_data['college']}

Degree:
{student_data['degree']}

Specialization:
{student_data['specialization']}

Skills:
{student_data['skills']}

Projects:
{student_data['projects']}

Experience:
{student_data['experience']}

Achievements:
{student_data['achievements']}

Company:
{company_name}

Job Position:
{job_position}

Target Role:
{student_data['job_role']}

Write a professional cover letter that:

• Addresses the hiring manager

• Mentions the company name

• Mentions the job position

• Highlights the candidate's projects

• Highlights technical skills

• Shows enthusiasm

• Ends professionally

Length:
300-400 words.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
def generate_linkedin_summary(student_data):

    prompt = f"""
You are an expert LinkedIn Profile Writer.

Create a complete LinkedIn profile for the following student.

Student Details

Name: {student_data['full_name']}

Degree:
{student_data['degree']}

College:
{student_data['college']}

Specialization:
{student_data['specialization']}

Skills:
{student_data['skills']}

Projects:
{student_data['projects']}

Experience:
{student_data['experience']}

Achievements:
{student_data['achievements']}

Target Role:
{student_data['job_role']}

Generate:

1. Professional LinkedIn Headline

2. About Section

3. Top Skills

4. Career Objective

5. Suggested LinkedIn Banner Quote

Use professional language suitable for recruiters.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text