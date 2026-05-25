![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Machine Learning](https://img.shields.io/badge/AI-Scikit--Learn-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

# 🌱 Smart Agriculture System

A full-stack **Smart Agriculture platform** integrating **FastAPI, PostgreSQL, AI (Machine Learning), and Streamlit Dashboard**. This project is production-ready, deployable via Docker, and GitHub-ready for developers, startups, and research purposes.

---

## Features

- **JWT Authentication** – Secure login & role-based access
- **Sensor Data Management** – CRUD operations for temperature, humidity, soil moisture
- **AI Crop Recommendation** – ML model predicts the best crop based on environmental conditions
- **Streamlit Dashboard** – Interactive UI for data visualization and AI recommendations
- **Docker Deployment** – One-command deployment for backend + database

---

## Technology Stack

- **Backend:** FastAPI, Python 3.11
- **Database:** PostgreSQL
- **Machine Learning:** scikit-learn, pandas, numpy
- **Frontend / Dashboard:** Streamlit
- **Deployment:** Docker & Docker Compose
- **Authentication:** JWT + passlib bcrypt

---

## Project Structure

```
smart-agriculture-system/
│── backend/          # FastAPI backend
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes/
│       ├── auth_routes.py
│       ├── sensor_routes.py
│       └── ai_routes.py
│
├── ai_models/        # AI datasets & models
│   ├── dataset.csv
│   ├── train_model.py
│   └── crop_model.pkl
│
├── dashboard/        # Streamlit dashboard
│   └── app.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
cd smart-agriculture-system
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Set up PostgreSQL:

```sql
CREATE DATABASE smart_agriculture;
CREATE USER smart_user WITH PASSWORD 'smartpass';
GRANT ALL PRIVILEGES ON DATABASE smart_agriculture TO smart_user;
```

Update `backend/config.py` if necessary.

### 5. Run Backend

```bash
uvicorn backend.main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6. Run Dashboard

```bash
streamlit run dashboard/app.py
```

### 7. Docker Deployment (Optional)

```bash
docker-compose up --build
```

---

## Usage

1. **Register / Login** via `/auth` endpoints
2. **Send Sensor Data** via `/sensors` endpoints
3. **Get AI Crop Recommendation** via `/ai/recommend`
4. **View data and AI suggestions** in Streamlit Dashboard

---

## License

This project is licensed under the MIT License.

---

## Future Enhancements

- Real-time IoT sensor integration (ESP32/Arduino)
- Mobile app interface (Flutter or Kivy)
- Advanced AI for disease and pest detection
- Cloud deployment (AWS, Azure, Railway)
