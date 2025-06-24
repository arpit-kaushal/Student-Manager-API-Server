# 🧠 Student Manager API (Flask + MySQL)

This project was developed as part of the **Keploy API Fellowship**. It is a full-stack API project built with **Flask** and **MySQL**, including a frontend interface and robust testing with **Pytest** and **mocking**.
---

## ✅ Features

- RESTful API with Python Flask
- MySQL database integration
- CRUD operations on student records
- HTML + JS frontend for user interaction
- ✅ Unit & API tests using `pytest`
- ✅ Mocked DB tests for safe, fast coverage

---

## ⚙️ Technologies Used

- Python + Flask
- MySQL
- HTML + JavaScript (Frontend)
- Pytest + pytest-cov (Testing + Coverage)
- Flask-CORS, Flask-MySQLdb

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
├── tests/
│ └── test_api.py
├── requirements.txt
├── README.md 
```

---
## 🗄️ MySQL Setup
```
CREATE DATABASE studentdb;

USE studentdb;

CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  course VARCHAR(100)
);
```
Update your MySQL username/password in db_config.py if needed.

## 🔧 How to Run the Project

### 🛠️ Prerequisites
- Python 3
- MySQL installed and running

### 📦 Install Python packages
```bash
pip install flask flask-mysqldb flask-cors

pip install flask flask-mysqldb flask-cors pytest pytest-cov


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



## 🌐 Frontend

You can access the simple UI via:
```
http://localhost:5000/
```
- ✅ Form inputs to add a student
- 📋 Dynamic list of all students
- ❌ Delete student button

## 🧪 Running Tests
### ✅ Run Unit + API Tests (Mocked DB)
```
python -m pytest tests/ --cov=app --cov-report=term-missing

```

### ✅ What is Tested:
- API response structure
- Request handling
- CRUD logic via mocked MySQL

## 📸 Test Coverage Screenshot
![Test Coverage](api_test.png)

  
## 📌 Notes

- API works fully with MySQL (studentdb) when running Flask app
- Tests run independently without database (mocked)
- Tested using Pytest and coverage
- Can be deployed using Render, Railway, Heroku, etc.
