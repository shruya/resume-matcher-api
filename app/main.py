from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
from app.resume_parser import extract_resume_text
from app.skill_matcher import match_skills

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Resume Matcher API is running 🚀"}

@app.post("/match_resume/")
async def match_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    skills: str = Form(...)
):
    file_path = os.path.join(UPLOAD_DIR, resume.filename)

    # Save uploaded resume file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    # Extract resume text
    resume_text = extract_resume_text(file_path)
    if not resume_text:
        return {"error": "Unsupported file format. Use PDF or DOCX."}

    # Convert skills string to list
    skills_list = [s.strip() for s in skills.split(",")]

    # Perform matching
    result = match_skills(resume_text, job_description, skills_list)

    return {
        "filename": resume.filename,
        "job_description": job_description,
        "skills": skills_list,
        "result": result
    }