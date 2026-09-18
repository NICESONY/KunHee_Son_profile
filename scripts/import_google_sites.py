"""Import the saved, public Google Sites snapshot; never infer missing links."""
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
soup = BeautifulSoup((ROOT.parent / "source_material/google-sites-home.html").read_text(encoding="utf-8"), "html.parser")

def clean(text):
    return re.sub(r"\s+", " ", text).strip()

def records(heading):
    section = next(s for s in soup.select("section") if s.find("h2") and clean(s.find("h2").get_text(" ", strip=True)) == heading)
    result = []
    for paragraph in section.select("p"):
        text = clean(re.sub(r"\[\s*link\s*\]", "", paragraph.get_text(" ", strip=True)))
        if text:
            urls = list(dict.fromkeys(a["href"] for a in paragraph.select('a[href^="http"]')))
            result.append({"text": text, "links": urls})
    return result

profile = {
    "name": "Kun-Hee Son",
    "department": "School of Artificial Intelligence",
    "affiliation": "Kongju National University",
    "email": "songunhee5426@gmail.com",
    "github": "https://github.com/NICESONY",
    "source_url": "https://sites.google.com/view/khson-profile-record",
    "source_date": "2026-09-19",
    "about": clean(next(p.get_text(" ", strip=True) for p in soup.select("p") if p.get_text(strip=True).startswith("Hello!"))),
    "research": {
        "interests": ["Robotic Manipulation", "Data Collection Systems", "Sim-to-Real"],
        "recent": "Robotics, Self supervised learning, Data generation",
        "previous": "Curriculum Learning and Image Classification, Reinforcement Learning",
        "paper_label": "KIICE 2023",
        "paper_url": "https://github.com/NICESONY/KIICE_2024_paper/"
    },
    "education": [
        {"institution": "Kongju National University", "program": "Department of Artificial Intelligence", "location": "Republic of Korea", "dates": "2020. 3. 2. – Current", "detail": "GPA: 4.15"},
        {"institution": "University of Nevada, Las Vegas", "program": "Experiential and Cultural Program", "location": "USA", "dates": "2024. 1. 1. – 2024. 1. 26.", "detail": ""}
    ],
    "publications": records("Paper"),
    "robotics_projects": records("ROS Project"),
    "web_projects": records("Web P roject"),
    "awards": records("Award"),
    "activities": records("External Activities"),
    "programming_skills": records("Professional Programming Skills"),
    "english_skills": records("English Skills"),
    "navigation": [{"id": key, "label": label} for key, label in [
        ("about", "About"), ("research", "Research"), ("education", "Education"),
        ("publications", "Publications"), ("projects", "Projects"), ("awards", "Awards"),
        ("activities", "Activities"), ("skills", "Skills")]]
}
link_checks = ROOT.parent / "source_material/link-checks.json"
profile["unavailable_links"] = [item["url"] for item in json.loads(link_checks.read_text(encoding="utf-8")) if item.get("status") == 404] if link_checks.is_file() else []
existing_path = ROOT / "_data/profile.json"
if existing_path.is_file():
    existing = json.loads(existing_path.read_text(encoding="utf-8"))
    for key in ["cv", "google_scholar"]:
        profile[key] = existing.get(key, "")
(ROOT / "_data/profile.json").write_text(json.dumps(profile, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Imported profile and all source records.")
