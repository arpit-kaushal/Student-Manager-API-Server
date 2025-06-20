# 🧠 Student Manager API (Flask + MySQL)

This project is built as part of the **Keploy API Fellowship**. It is a fully functional backend API (with optional frontend) to manage student data using Python Flask and MySQL.

---

## ✅ Features

- RESTful API built with Flask
- Database integration using MySQL
- CRUD operations on student data
- Simple frontend UI to interact with APIs
- Tested via `curl` commands

---

## ⚙️ Technologies Used

- Python
- Flask
- MySQL
- HTML, JavaScript (for frontend)
- curl (for API testing)

---

## 📁 Folder Structure
```
student-api/
├── app.py
├── db_config.py
├── templates/
│ └── index.html 
├── static/
│ └── script.js
├── requirements.txt
├── README.md 
```

---

## 🔧 How to Run the Project

### 🛠️ Prerequisites
- Python 3
- MySQL installed and running

### 📦 Install Python packages
```bash
pip install flask flask-mysqldb flask-cors

```

## ▶️ Run the Flask App
```
python app.py
```
App will run at: http://localhost:5000

## 🔗 API Endpoints

| Method | Endpoint             | Description          |
| ------ | -------------------- | -------------------- |
| GET    | `/api/students`      | Fetch all students   |
| POST   | `/api/students`      | Add new student      |
| PUT    | `/api/students/<id>` | Update student by ID |
| DELETE | `/api/students/<id>` | Delete student by ID |

## 🔁 API Testing with curl

### 📥 Add Student
```
curl -X POST http://localhost:5000/api/students -H "Content-Type: application/json" -d "{\"name\":\"Arpit Kaushal\", \"email\":\"arpit@keploy.com\", \"course\":\"Flask + MySQL\"}"
```

### 📤 Get All Students
```
curl http://localhost:5000/api/students
```
### 📝 Update Student

```
curl -X PUT http://localhost:5000/api/students/2 -H "Content-Type: application/json" -d "{\"name\":\"Updated Arpit\", \"email\":\"updated@x.com\", \"course\":\"AI/ML\"}"
```

### ❌ Delete Student

```
curl -X DELETE http://localhost:5000/api/students/2
```

## 🌐 Frontend

You can access the simple UI via:
```
http://localhost:5000/
```
- ✅ Form inputs to add a student
- 📋 Dynamic list of all students
- ❌ Delete student button

## 📌 Notes

- The API is fully functional locally.
- You can deploy it using Render, Heroku, or locally via ngrok if required for demos.
- curl commands tested and verified.
