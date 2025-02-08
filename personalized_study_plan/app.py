from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# ✅ Corrected Database Initialization Function
def init_db():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS study_plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                study_hours INTEGER,
                subject TEXT,
                recommended_topic TEXT
            )
        ''')
        conn.commit()

init_db()  # Ensure database is initialized when app starts

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_plan", methods=["POST"])
def generate_plan():
    try:
        data = request.get_json()
        study_hours = data.get("study_hours")

        if not study_hours or not isinstance(study_hours, int):
            return jsonify({"error": "Invalid study hours"}), 400

        # ✅ Simple ML Logic for Study Plan
        subjects = ["Math", "Science", "Programming", "History", "AI/ML"]
        topics = ["Algebra", "Physics Laws", "Python Basics", "World War II", "Neural Networks"]

        recommendations = []
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            for i in range(min(study_hours, len(subjects))):
                subject = subjects[i % len(subjects)]
                topic = topics[i % len(topics)]

                # Insert into database
                cursor.execute("INSERT INTO study_plans (study_hours, subject, recommended_topic) VALUES (?, ?, ?)",
                               (study_hours, subject, topic))
                conn.commit()

                recommendations.append({"subject": subject, "topic": topic})

        return jsonify({"study_plan": recommendations})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
