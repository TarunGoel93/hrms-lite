<div align="center">

# 🏢 HRMS Lite

### Lightweight Human Resource Management System

<p align="center">
  <img src="https://img.shields.io/badge/Flask-2.0+-1B4332?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Python-3.8+-2D6A4F?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-Database-40916C?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/License-MIT-C2703E?style=for-the-badge" alt="License">
</p>

<p align="center">
  <strong>A beautifully designed, minimal HR management solution for small teams</strong>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-api-documentation">API</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

</div>

## ✨ Features

<table>
<tr>
<td width="50%">

### 👥 Employee Management
- **Add, view, and delete** employees effortlessly
- **Comprehensive profiles** with ID, name, email, and department
- **Real-time updates** with instant feedback
- **Elegant table view** with search and filter capabilities

</td>
<td width="50%">

### 📅 Attendance Tracking
- **Mark attendance** with Present/Absent status
- **Date-based tracking** for accurate records
- **Statistics dashboard** showing attendance rate
- **Prevent duplicates** with smart validation

</td>
</tr>
</table>

### 🎨 Beautiful Design Philosophy

Built with a carefully crafted design system featuring:

- 🌿 **Nature-inspired palette** - Calming greens and earthy tones
- ✨ **Smooth animations** - Delightful micro-interactions
- 📱 **Fully responsive** - Perfect on desktop, tablet, and mobile
- ♿ **Accessible** - WCAG compliant with thoughtful UX

---

## 🖼️ Demo

<div align="center">

### Employee Management
![Employee Management Interface](https://via.placeholder.com/800x450/1B4332/FFFFFF?text=Employee+Management+Dashboard)

### Attendance Tracking
![Attendance Tracking Interface](https://via.placeholder.com/800x450/2D6A4F/FFFFFF?text=Attendance+Management+System)

</div>

---

## 🚀 Quick Start

### Prerequisites

Make sure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/TarunGoel93/hrms-lite.git
cd hrms-lite

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The application will be available at `http://localhost:5000` 🎉

### Docker Deployment (Optional)

```bash
# Build the Docker image
docker build -t hrms-lite .

# Run the container
docker run -p 5000:5000 hrms-lite
```

---

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="60" height="60" alt="Python"/>
<br><strong>Python</strong>
<br><sub>Backend Logic</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" width="60" height="60" alt="Flask"/>
<br><strong>Flask</strong>
<br><sub>Web Framework</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg" width="60" height="60" alt="SQLite"/>
<br><strong>SQLite</strong>
<br><sub>Database</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="60" height="60" alt="HTML5"/>
<br><strong>HTML5/CSS3</strong>
<br><sub>Frontend</sub>
</td>
</tr>
</table>

### Core Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend Framework** | Flask 2.0+ | Lightweight web server and routing |
| **ORM** | SQLAlchemy | Database abstraction and queries |
| **Database** | SQLite | Persistent data storage |
| **Frontend** | Vanilla JS + CSS3 | Interactive UI without frameworks |
| **Typography** | DM Sans | Modern, readable font |

---

## 📁 Project Structure

```
hrms-lite/
├── 📄 app.py                 # Main Flask application
├── 📁 templates/             # HTML templates
│   ├── index.html           # Employee management page
│   └── attendance.html      # Attendance tracking page
├── 📁 instance/              # Database instance
│   └── hrms.db              # SQLite database
├── 📄 requirements.txt       # Python dependencies
└── 📄 README.md             # You are here!
```

---

## 🔌 API Documentation

### Employee Endpoints

#### Get All Employees
```http
GET /api/employees
```

**Response:**
```json
[
  {
    "id": 1,
    "employee_id": "EMP001",
    "full_name": "John Doe",
    "email": "john.doe@company.com",
    "department": "Engineering",
    "created_at": "2026-02-07T10:30:00"
  }
]
```

#### Create Employee
```http
POST /api/employees
Content-Type: application/json
```

**Request Body:**
```json
{
  "employee_id": "EMP001",
  "full_name": "John Doe",
  "email": "john.doe@company.com",
  "department": "Engineering"
}
```

**Response:** `201 Created`

#### Delete Employee
```http
DELETE /api/employees/{id}
```

**Response:** `200 OK`

### Attendance Endpoints

#### Mark Attendance
```http
POST /api/attendance
Content-Type: application/json
```

**Request Body:**
```json
{
  "employee_id": 1,
  "date": "2026-02-07",
  "status": "Present"
}
```

**Response:** `201 Created`

#### Get Attendance Records
```http
GET /api/attendance/{employee_id}
```

**Response:**
```json
[
  {
    "id": 1,
    "employee_id": 1,
    "date": "2026-02-07",
    "status": "Present",
    "employee_name": "John Doe"
  }
]
```

---

## 🎨 Design System

### Color Palette

```css
/* Primary Brand Colors */
--brand: #1B4332        /* Deep Forest Green */
--brand-light: #2D6A4F  /* Forest Green */
--brand-lighter: #40916C /* Emerald */

/* Accent Colors */
--accent: #C2703E       /* Warm Terracotta */
--accent-light: #D4885A /* Sandy Brown */

/* Semantic Colors */
--success: #15803D      /* Success Green */
--danger: #B91C1C       /* Alert Red */

/* Neutral Colors */
--bg: #f5f2ed          /* Warm White */
--surface: #ffffff      /* Pure White */
--text-primary: #1c1917 /* Rich Black */
```

### Typography

- **Font Family:** DM Sans
- **Weights:** 300 (Light), 400 (Regular), 500 (Medium), 600 (Semibold), 700 (Bold)

---

## 🔐 Security Features

- ✅ **Input validation** on all form fields
- ✅ **SQL injection protection** via SQLAlchemy ORM
- ✅ **Email format validation** with regex patterns
- ✅ **Duplicate prevention** with unique constraints
- ✅ **Error handling** with graceful fallbacks
- ✅ **CSRF protection** ready for production deployment



---

## 🤝 Contributing

We love contributions! Here's how you can help make HRMS Lite even better:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write descriptive commit messages
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 💖 Acknowledgments

- Design inspiration from modern HR platforms
- Icons from [Heroicons](https://heroicons.com/)
- Font from [Google Fonts](https://fonts.google.com/specimen/DM+Sans)
- Built with ❤️ by [Tarun Goel](https://github.com/TarunGoel93)

---

<div align="center">

### 🌟 Star this repo if you find it helpful!

Made with 💚 and ☕ by the HRMS Lite team

[Report Bug](https://github.com/TarunGoel93/hrms-lite/issues) · [Request Feature](https://github.com/TarunGoel93/hrms-lite/issues) · [Discussions](https://github.com/TarunGoel93/hrms-lite/discussions)

</div>
