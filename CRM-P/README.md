# CRM System - Healthcare Management Platform

A comprehensive Customer Relationship Management (CRM) system built with Python Flask, designed specifically for healthcare facilities to manage patients, appointments, billing, and internal communications.

## 🚀 Features

### Core Modules
- **Appointments Management** - Schedule, track, and manage patient appointments
- **Patient Management** - Complete patient records and information
- **Billing System** - Track invoices, payments, and financial records
- **Medical Records** - Store and manage patient medical history
- **Investigations** - Schedule and track medical tests and procedures

### Marketing & Communication
- **Campaign Module** - Create and manage marketing campaigns
- **Omni-channel Campaigns** - Support for Email, SMS, and WhatsApp
- **Patient Retention** - Marketing offers and retention strategies
- **Custom Templates** - Personalized communication templates

### Operations Management
- **Patient Complaint Management** - Track and resolve patient issues
- **Inter-Department Communication** - Internal messaging system
- **Patient Communication Tracker** - Monitor all patient interactions
- **Dashboard Analytics** - Revenue, appointment, and surgery insights

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite (can be configured for PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Authentication**: Flask-Login
- **Database ORM**: SQLAlchemy
- **Charts**: Chart.js

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CRM-P
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///crm.db
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Default login credentials: `admin` / `admin123`

## 🗄️ Database Setup

The application automatically creates the database and tables on first run. The default admin user is created automatically.

### Database Models
- **Users** - Staff and doctor accounts
- **Patients** - Patient information and demographics
- **Appointments** - Scheduled appointments and status
- **Billing** - Financial records and invoices
- **Medical Records** - Patient medical history
- **Investigations** - Medical tests and procedures
- **Campaigns** - Marketing campaigns and templates
- **Complaints** - Patient complaint tracking
- **Communications** - Inter-department messaging

## 🔐 Authentication & Security

- **User Roles**: Admin, Doctor, Staff
- **Password Hashing**: Secure password storage using Werkzeug
- **Session Management**: Flask-Login for user sessions
- **Access Control**: Role-based access to different modules

## 📱 User Interface

### Modern Design
- Responsive Bootstrap 5 interface
- Beautiful gradient color scheme
- Interactive charts and statistics
- Mobile-friendly design

### Dashboard Features
- Real-time statistics
- Revenue charts
- Appointment status overview
- Quick action buttons

## 🚀 Deployment

### Development
```bash
python app.py
```

### Production
```bash
# Using Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using Waitress (Windows)
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Environment Variables
- `SECRET_KEY`: Flask secret key for sessions
- `DATABASE_URL`: Database connection string
- `FLASK_ENV`: Set to 'production' for production deployment

## 📊 API Endpoints

### Authentication
- `POST /login` - User login
- `GET /logout` - User logout

### Core Modules
- `GET /dashboard` - Main dashboard
- `GET /appointments` - List appointments
- `POST /appointments/new` - Create appointment
- `GET /patients` - List patients
- `POST /patients/new` - Create patient
- `GET /billing` - List bills
- `GET /medical-records` - List medical records
- `GET /investigations` - List investigations

### Marketing & Communication
- `GET /campaigns` - List campaigns
- `POST /campaigns/new` - Create campaign
- `GET /complaints` - List complaints
- `GET /communications` - List messages
- `POST /communications/new` - Send message

## 🔧 Configuration

### Database Configuration
The system supports multiple database backends:
- **SQLite** (default): `sqlite:///crm.db`
- **PostgreSQL**: `postgresql://user:pass@localhost/dbname`
- **MySQL**: `mysql://user:pass@localhost/dbname`

### Email Configuration
Configure email settings in the `.env` file:
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## 📈 Customization

### Adding New Modules
1. Create new database models in `app.py`
2. Add routes for the new module
3. Create HTML templates in the `templates/` folder
4. Update the navigation menu in `base.html`

### Styling
- Custom CSS in `base.html`
- Bootstrap 5 classes for responsive design
- Font Awesome icons for visual elements

## 🧪 Testing

```bash
# Run basic tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=app tests/
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔮 Future Enhancements

- **Mobile App**: Native iOS and Android applications
- **AI Integration**: Chatbot for patient queries
- **Advanced Analytics**: Machine learning insights
- **Telemedicine**: Video consultation integration
- **Payment Gateway**: Online payment processing
- **Multi-language Support**: Internationalization
- **API Documentation**: Swagger/OpenAPI specs
- **Webhook Support**: Third-party integrations

## 📊 Performance Optimization

- Database indexing for large datasets
- Caching for frequently accessed data
- Pagination for large lists
- Image optimization for patient photos
- CDN integration for static assets

---

**Built with ❤️ for the healthcare community**
