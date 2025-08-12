#!/usr/bin/env python3
"""
CRM System Startup Script
Run this script to start the CRM application
"""

import os
import sys
from app import app, db
from datetime import datetime

def create_logs_directory():
    """Create logs directory if it doesn't exist"""
    if not os.path.exists('logs'):
        os.makedirs('logs')
        print("Created logs directory")

def print_startup_info():
    """Print startup information"""
    print("=" * 60)
    print("🏥 CRM System - Healthcare Management Platform")
    print("=" * 60)
    print(f"🚀 Starting application at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Server will be available at: http://localhost:5000")
    print(f"🔑 Default login: admin / admin123")
    print(f"📁 Database: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print(f"🔧 Environment: {app.config.get('FLASK_ENV', 'development')}")
    print("=" * 60)

def main():
    """Main startup function"""
    try:
        # Create logs directory
        create_logs_directory()
        
        # Print startup information
        print_startup_info()
        
        # Initialize database
        with app.app_context():
            db.create_all()
            print("✅ Database initialized successfully")
        
        # Start the application
        print("🚀 Starting Flask development server...")
        print("📝 Press Ctrl+C to stop the server")
        print("-" * 60)
        
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            use_reloader=True
        )
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
