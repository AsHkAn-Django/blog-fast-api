# Blog FastAPI

A simple yet powerful blog application built with **FastAPI**, **SQLAlchemy**, and **Pydantic**.  
This project demonstrates modern backend development practices including authentication, CRUD operations, and database management.

---

## 🚀 Features

- User registration & authentication (JWT-based)
- Create, read, update, and delete (CRUD) blog posts
- Comment system for posts
- Role-based access (users & admins)
- Database integration with SQLAlchemy
- Automatic API documentation with Swagger & ReDoc
- Environment-based configuration

---

## 🛠️ Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)  
- **Database ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)  
- **Data Validation**: [Pydantic](https://docs.pydantic.dev/)  
- **Authentication**: OAuth2 + JWT  
- **Server**: [Uvicorn](https://www.uvicorn.org/)

---

## 📂 Project Structure

blog-fast-api/
│── app/
│ ├── main.py # Entry point
│ ├── models/ # SQLAlchemy models
│ ├── schemas/ # Pydantic schemas
│ ├── crud/ # CRUD operations
│ ├── api/ # API routers
│ ├── core/ # Security, config, etc.
│ └── db/ # Database session & base
│
│── tests/ # Test cases
│── requirements.txt # Dependencies
│── README.md # Project documentation

