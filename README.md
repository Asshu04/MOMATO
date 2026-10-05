MOMATO 🍔

Food Delivery Backend API

MOMATO is a backend API for a food-delivery platform, built with Python and FastAPI. The project focuses on REST API development, database design, authentication, CRUD operations, and secure user management.

«Project Status: 🚧 In Development»

---

🚀 Overview

MOMATO is being developed as a database-driven food-delivery backend.

The current implementation provides APIs for:

- User registration and authentication
- JWT-based authorization
- Restaurant management
- Food item management
- User profiles
- Shopping cart management
- Request and response validation
- SQL Server database integration
- Interactive API documentation with Swagger/OpenAPI

The project is being developed with a modular backend architecture so additional features can be added as development continues.

---

🛠️ Tech Stack

Backend

- Python
- FastAPI
- Uvicorn
- REST APIs

Database

- Microsoft SQL Server
- SQLAlchemy
- PyODBC

Authentication & Security

- JWT Authentication
- HTTP Bearer Authentication
- bcrypt Password Hashing

Validation & Documentation

- Pydantic
- Swagger UI
- OpenAPI

Development Tools

- Git
- GitHub
- Postman
- Visual Studio Code

---

✨ Current Features

👤 User Authentication

- User registration
- Secure password hashing using bcrypt
- User login
- JWT token generation
- Protected API endpoints
- Authenticated user profile access

🏪 Restaurant Management

Restaurant APIs currently support CRUD operations:

- Create restaurant
- Retrieve restaurants
- Retrieve restaurant details
- Update restaurant
- Delete restaurant

🍕 Food Management

Food item APIs provide functionality for managing food associated with restaurants.

- Create food item
- Retrieve food items
- Update food item
- Delete food item

🛒 Shopping Cart

Authenticated users can manage their shopping cart through backend APIs.

Current functionality includes:

- Add items to cart
- View cart
- Update cart items
- Remove cart items

🗄️ Database

The application uses Microsoft SQL Server with SQLAlchemy ORM.

The backend uses SQLAlchemy models and relationships to manage application data.

📖 API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

After starting the application, open:

http://127.0.0.1:8000/docs

You can use Swagger UI to inspect and test available endpoints.

---

🔐 Authentication Flow

MOMATO uses JWT-based authentication.

User Registration
       ↓
Password Hashing
       ↓
SQL Server
       ↓
User Login
       ↓
Password Verification
       ↓
JWT Token Generated
       ↓
Bearer Token
       ↓
Protected API Endpoint
       ↓
JWT Validation
       ↓
Authorized Request

Passwords are not stored as plain text. bcrypt is used for password hashing.

---

📁 Project Structure

MOMATO/
│
├── backend/
│   ├── auth.py
│   ├── create_table.py
│   ├── database.py
│   ├── model.py
│   ├── schemas.py
│   ├── security.py
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt

---

⚙️ Installation

1. Clone the repository

git clone https://github.com/Asshu04/MOMATO.git

2. Navigate to the project

cd MOMATO

3. Create a virtual environment

python -m venv .venv

4. Activate the virtual environment

Windows PowerShell

.\.venv\Scripts\Activate.ps1

Windows CMD

.venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

---

🗄️ Database Configuration

MOMATO currently uses Microsoft SQL Server.

Before running the application, configure your SQL Server connection in the backend database configuration.

Example configuration:

SQL Server
Database Name
Server / Instance
Username
Password
Driver

«Do not commit database passwords, JWT secrets, or other sensitive credentials to GitHub.»

For production, these values should be stored using environment variables.

---

▶️ Running the Application

From the project directory:

uvicorn backend.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

ReDoc documentation:

http://127.0.0.1:8000/redoc

---

🧪 API Testing

API endpoints can be tested using:

- Swagger UI
- Postman

Recommended testing flow:

Register User
      ↓
Login
      ↓
Copy JWT Token
      ↓
Authorize
      ↓
Access Protected APIs
      ↓
Test Restaurant / Food / Cart APIs

---

📌 Project Roadmap

The following features are planned for future development:

- [ ] Order management
- [ ] Address management
- [ ] Food categories
- [ ] Search and filtering
- [ ] Reviews and ratings
- [ ] Admin APIs
- [ ] Role-based authorization
- [ ] Automated API testing
- [ ] React frontend
- [ ] Frontend/backend integration
- [ ] Production deployment
- [ ] Improved production security
- [ ] API performance optimization

---

🎯 Learning Objectives

This project is being developed to gain practical experience with:

- REST API architecture
- FastAPI
- Python backend development
- SQLAlchemy ORM
- Microsoft SQL Server
- Database relationships
- JWT authentication
- Password hashing
- Pydantic validation
- API testing
- Swagger/OpenAPI
- Git and GitHub
- Backend application architecture

---

👨‍💻 Author

Ashish Kumar Behera

Python Full Stack Developer | Backend Developer

- GitHub: https://github.com/Asshu04
- LinkedIn: https://linkedin.com/in/ashishkumarbehera04

---

📄 License

This project is currently intended for learning and development purposes.