from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/api/result", methods=["POST"])
def result():
    data = request.get_json()
    reg_no = data.get("reg_no")
    sem = data.get("sem")
    session = data.get("session")

    if not reg_no or not sem or not session:
        return jsonify({"success": False, "error": "reg_no, sem, session required"})

    roman = {
        "1": "I",
        "2": "II",
        "3": "III",
        "4": "IV",
        "5": "V",
        "6": "VI",
        "7": "VII",
        "8": "VIII"
    }
    sem_roman = roman.get(str(sem))

    exam_held = "November/" + session if int(sem) % 2 == 0 else "April/" + session

    url = (
        "https://beu-bih.ac.in/result-three?"
        f"name=B.Tech.%20{sem}%20Semester%20Examination,%20{session}"
        f"&semester={sem_roman}"
        f"&session={session}"
        f"&regNo={reg_no}"
        f"&exam_held={exam_held.replace('/', '%2F')}"
    )

    return jsonify({"success": True, "url": url})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
