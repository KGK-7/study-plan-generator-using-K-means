# 📚 Personalized Study Plan Generator

## 🔹 Project Overview
The **Personalized Study Plan Generator** is an AI-powered web application that creates a **customized study schedule** based on the number of hours a user wants to study. It dynamically suggests **subjects and topics** using a simple **machine learning algorithm** to ensure an optimized study experience.

## 🔹 Features
✅ Generate a study plan based on user input  
✅ AI-powered **subject & topic recommendations**  
✅ SQLite3 database for storing study plans  
✅ REST API with Flask for backend processing  
✅ Simple **HTML & CSS** frontend for user interaction  

---

## 🛠️ Technologies Used
- **Frontend**: HTML, CSS  
- **Backend**: Flask (Python)  
- **Database**: SQLite3  
- **API Handling**: REST API (Flask + JSON)  
- **ML Logic**: Python-based AI for study recommendations  

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/Personalized-Study-Plan-Generator.git
cd Personalized-Study-Plan-Generator
```

### **2️⃣ Install Dependencies**
Make sure you have **Python 3.7+** installed. Then, install the required dependencies:
```bash
pip install flask flask-cors sqlite3
```

### **3️⃣ Run the Flask Server**
```bash
python app.py
```
The server will start at **http://127.0.0.1:5000** 🚀  

---

## 🖥️ API Endpoints

### **📌 1. Generate Study Plan**
**Endpoint:** `POST /generate_plan`  
**Description:** Generates a personalized study plan based on input study hours.  

#### 🔹 **Request (JSON format)**
```json
{
  "study_hours": 3
}
```

#### 🔹 **Response (Example JSON Output)**
```json
{
  "study_plan": [
    {"subject": "Math", "topic": "Algebra"},
    {"subject": "Science", "topic": "Physics Laws"},
    {"subject": "Programming", "topic": "Python Basics"}
  ]
}
```

---

## 🎨 Frontend Usage
- Open `index.html` in a browser.  
- Enter study hours and click **Generate Plan**.  
- The study plan will be displayed on the screen.  

---

## 🔥 Future Improvements
✅ **User authentication** for tracking progress  
✅ **Integration with external learning APIs**  
✅ **Advanced ML algorithms** for more personalized recommendations  

---

## 📌 Contributing
Contributions are welcome! If you’d like to improve this project, feel free to submit a pull request or open an issue.  

## 📝 License
This project is open-source and available under the **MIT License**.
