# Resume Matcher API

This project is a small backend service I built using FastAPI.
The idea is simple: upload a resume (PDF/DOCX) along with a job description, and the API will check how well the resume matches by looking for the required skills and keywords.

I wanted to make something that feels close to real-world use, because in hiring most resumes are scanned and filtered automatically.

## Features

- Upload resumes in PDF or DOCX format.

- Extract text from resumes and compare with a job description.

- Skill matching logic (checks for required skills in the resume).

- API built with FastAPI, responses in JSON.

- Basic test cases written with pytest to validate the flow.

## Tech Stack

- **Python 3.12**

- **FastAPI** – for building APIs.

- **python-docx / PyPDF2** – to read resumes.

- **pytest** – for testing.

## How to Run

1. Clone the repo

   ```bash
   git clone <resume-matcher-api >
   cd resume-matcher-api


2. Install requirements

   pip install -r requirements.txt


3. Start the server

   uvicorn app.main:app --reload


4. Open in browser: http://127.0.0.1:8000/docs

## Testing

Run the test cases:

   pytest -v


✅ Example result:

   tests/test_matcher.py::test_match_resume PASSED

## Example Response

Request: upload a resume + job description + skills list

Response:

{
  "result": {
    "skills_found": ["Python"],
    "skills_missing": ["FastAPI", "Docker"],
    "match_score": 33.3
  }
}

## Why I Built This

I wanted to practice working with **file uploads, parsing, and testing** in FastAPI.
This project gave me good hands-on experience and also helped me show how I approach **backend development in Python**.