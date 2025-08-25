import re
from typing import List, Dict

def match_skills(resume_text: str, job_description: str, skills: List[str]) -> Dict:
    """Match skills between resume and job description"""
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched = []
    missing = []

    for skill in skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, resume_text):
            matched.append(skill)
        else:
            missing.append(skill)

    score = round((len(matched) / len(skills)) * 100, 2) if skills else 0

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }