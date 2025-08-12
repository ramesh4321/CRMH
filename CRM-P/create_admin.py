from app import app, db, User
from werkzeug.security import generate_password_hash

def create_admin_user():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if admin user exists
        admin = User.query.filter_by(username='admin').first()
        
        if not admin:
            # Create admin user
            admin = User(
                username='admin',
                email='admin@crm.com',
                password_hash=generate_password_hash('admin123'),
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin user created successfully!")
            print("Username: admin")
            print("Password: admin123")
        else:
            print("ℹ️ Admin user already exists")
            # Update password to ensure it's correct
            admin.password_hash = generate_password_hash('admin123')
            db.session.commit()
            print("✅ Admin password updated!")
            print("Username: admin")
            print("Password: admin123")
        
        # Print all users for verification
        users = User.query.all()
        print(f"\n📊 Total users in database: {len(users)}")
        for user in users:
            print(f"  - {user.username} ({user.role})")

if __name__ == '__main__':
    create_admin_user()
