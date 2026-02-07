from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import re

app = Flask(__name__)

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///hrms.db')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==================== MODELS ====================

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    attendances = db.relationship('Attendance', backref='employee', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'full_name': self.full_name,
            'email': self.email,
            'department': self.department,
            'created_at': self.created_at.isoformat()
        }

class Attendance(db.Model):
    __tablename__ = 'attendance'
    
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
    __table_args__ = (db.UniqueConstraint('employee_id', 'date', name='unique_employee_date'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'date': self.date.isoformat(),
            'status': self.status,
            'employee_name': self.employee.full_name
        }

# ==================== HELPER FUNCTIONS ====================

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# ==================== ROUTES - PAGES ====================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attendance')
def attendance_page():
    return render_template('attendance.html')

# ==================== API ROUTES - EMPLOYEES ====================

@app.route('/api/employees', methods=['GET'])
def get_employees():
    try:
        employees = Employee.query.all()
        return jsonify([emp.to_dict() for emp in employees]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/employees', methods=['POST'])
def create_employee():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['employee_id', 'full_name', 'email', 'department']
        for field in required_fields:
            if not data.get(field) or not data.get(field).strip():
                return jsonify({'error': f'{field.replace("_", " ").title()} is required'}), 400
        
        # Validate email format
        if not validate_email(data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        
        # Check for duplicate employee_id
        existing = Employee.query.filter_by(employee_id=data['employee_id'].strip()).first()
        if existing:
            return jsonify({'error': 'Employee ID already exists'}), 409
        
        # Create new employee
        employee = Employee(
            employee_id=data['employee_id'].strip(),
            full_name=data['full_name'].strip(),
            email=data['email'].strip(),
            department=data['department'].strip()
        )
        
        db.session.add(employee)
        db.session.commit()
        
        return jsonify(employee.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        employee = Employee.query.get(id)
        if not employee:
            return jsonify({'error': 'Employee not found'}), 404
        
        db.session.delete(employee)
        db.session.commit()
        
        return jsonify({'message': 'Employee deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# ==================== API ROUTES - ATTENDANCE ====================

@app.route('/api/attendance', methods=['POST'])
def mark_attendance():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('employee_id'):
            return jsonify({'error': 'Employee is required'}), 400
        if not data.get('date'):
            return jsonify({'error': 'Date is required'}), 400
        if not data.get('status'):
            return jsonify({'error': 'Status is required'}), 400
        
        # Validate status
        if data['status'] not in ['Present', 'Absent']:
            return jsonify({'error': 'Status must be Present or Absent'}), 400
        
        # Check if employee exists
        employee = Employee.query.get(data['employee_id'])
        if not employee:
            return jsonify({'error': 'Employee not found'}), 404
        
        # Parse date
        try:
            attendance_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        # Check for duplicate attendance
        existing = Attendance.query.filter_by(
            employee_id=data['employee_id'],
            date=attendance_date
        ).first()
        
        if existing:
            return jsonify({'error': 'Attendance already marked for this date'}), 409
        
        # Create attendance record
        attendance = Attendance(
            employee_id=data['employee_id'],
            date=attendance_date,
            status=data['status']
        )
        
        db.session.add(attendance)
        db.session.commit()
        
        return jsonify(attendance.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/attendance/<int:employee_id>', methods=['GET'])
def get_attendance(employee_id):
    try:
        # Check if employee exists
        employee = Employee.query.get(employee_id)
        if not employee:
            return jsonify({'error': 'Employee not found'}), 404
        
        # Get attendance records
        records = Attendance.query.filter_by(employee_id=employee_id).order_by(Attendance.date.desc()).all()
        
        return jsonify([record.to_dict() for record in records]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# ==================== DATABASE INITIALIZATION ====================

def init_db():
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)