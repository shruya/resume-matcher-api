from fastapi.testclient import TestClient
from app.main import app
from io import BytesIO
from docx import Document

client = TestClient(app)


def create_test_docx():
    doc = Document()
    doc.add_paragraph("This is a sample resume with Python experience")
    file_stream = BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)
    return file_stream


def test_match_resume():
    job_desc = "Looking for a backend developer skilled in Python and FastAPI"
    skills = ["Python", "FastAPI", "Docker"]

    files = {
        "resume": ("resume.docx", create_test_docx().read())
    }

    response = client.post(
        "/match_resume/",
        data={"job_description": job_desc, "skills": ",".join(skills)},
        files=files
    )

    assert response.status_code == 200
    result = response.json()
    assert "result" in result
