# MFA Face Recognition System

A modern Multi-Factor Authentication (MFA) system that combines traditional password authentication with facial recognition and grid-based coordinate authentication for enhanced security.

## 🌟 Features

- **Multi-Factor Authentication**: Three layers of security
  - Username/Password authentication
  - Facial recognition using face-api.js
  - Grid coordinate-based authentication
- **Real-time Face Detection**: Live webcam integration for face registration and authentication
- **Secure Backend**: JWT-based authentication with Flask
- **Modern Frontend**: React-based responsive user interface
- **Dockerized**: Easy deployment with Docker Compose
- **Database**: PostgreSQL for secure data storage

## 🏗️ Architecture

```
├── MFA-Backend/           # Flask API backend
│   └── mfa_app/
│       ├── app.py         # Flask application entry point
│       ├── models.py      # Database models
│       ├── config.py      # Configuration settings
│       ├── routes/        # API endpoints
│       │   ├── auth.py    # Authentication routes
│       │   ├── face.py    # Face recognition routes
│       │   └── mfa.py     # MFA verification routes
│       └── utils/         # Utility functions
├── MFAFRONTENDCORRECT/    # React frontend
│   └── mfa-client/
│       ├── src/
│       │   ├── pages/     # Application pages
│       │   ├── components/# React components
│       │   └── api/       # API integration
└── docker-compose.yml    # Container orchestration
```

## 🛠️ Technology Stack

### Backend
- **Flask** - Python web framework
- **PostgreSQL** - Database
- **JWT** - Authentication tokens
- **OpenCV** - Computer vision for face processing
- **BCrypt** - Password hashing
- **Flask-CORS** - Cross-origin requests

### Frontend
- **React** - UI framework
- **face-api.js** - Browser-based face recognition
- **React Router** - Navigation
- **Axios** - HTTP client
- **React Webcam** - Camera integration

### Infrastructure
- **Docker & Docker Compose** - Containerization
- **Nginx** - Web server (in production)

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MFA
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Database: localhost:5432

## 📋 Usage

### User Registration
1. Navigate to the registration page
2. Enter username and password
3. Complete face registration using your webcam
4. Select grid coordinates for additional security
5. Submit registration

### User Authentication
1. Enter username and password
2. Complete face verification using webcam
3. Select the correct grid coordinates
4. Access your secured dashboard

## 🔧 Development Setup

### Backend Development

1. **Navigate to backend directory**
   ```bash
   cd MFA-Backend/mfa_app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   export FLASK_ENV=development
   export DATABASE_URL=postgresql://postgres:1234@localhost:5432/mfa_db
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

### Frontend Development

1. **Navigate to frontend directory**
   ```bash
   cd MFAFRONTENDCORRECT/mfa-client
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm start
   ```

## 🌐 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login

### Face Recognition
- `POST /face/register` - Register face data
- `POST /face/verify` - Verify face during authentication

### MFA
- `POST /mfa/verify-grid` - Verify grid coordinates
- `GET /mfa/status` - Check MFA status

## 🔐 Security Features

- **Password Hashing**: BCrypt for secure password storage
- **JWT Tokens**: Stateless authentication
- **Face Encoding**: Secure facial feature storage
- **CORS Protection**: Configured cross-origin policies
- **Input Validation**: Server-side validation for all inputs

## 📊 Database Schema

### User Table
```sql
- id (Primary Key)
- username (Unique)
- password_hash
- face_model (Binary - encoded face features)
- grid_coordinates (JSON - selected coordinates)
```

## 🐳 Docker Configuration

The application uses Docker Compose with three services:

- **backend**: Flask API server (Port 8000)
- **frontend**: React application (Port 3000)
- **postgres**: PostgreSQL database (Port 5432)

## 🔍 Testing

### Frontend Tests
```bash
cd MFAFRONTENDCORRECT/mfa-client
npm test
```

### Backend Tests
```bash
cd MFA-Backend/mfa_app
python -m pytest
```

## 🚀 Production Deployment

1. **Update environment variables** in docker-compose.yml
2. **Configure production database** settings
3. **Set up reverse proxy** (Nginx recommended)
4. **Enable HTTPS** for secure connections
5. **Configure CORS** for your domain

## 🎯 Future Enhancements

- [ ] Mobile application support
- [ ] Voice recognition integration
- [ ] Advanced facial liveness detection
- [ ] Two-factor authentication via SMS
- [ ] Admin dashboard for user management
- [ ] Multi-language support
- [ ] Audit logging and monitoring


