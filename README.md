EcoAware web Application

Welcome to the EcoAware Web Application repository! This project aims to create a digital platform to promote environmental awareness and conservation efforts.
It includes features for managing donations, posts, and newsletter subscriptions. This README file provides an overview of the project, setup instructions,
and other essential information.


Table of Contents
Project Overview
Features
Tech Stack
Setup Instructions
Usage
Contributing
Contact


Project Overview
EcoAware is a web application designed to foster environmental responsibility. It allows users to:
Make donations to support EcoAware  environmental initiatives.
Post articles and updates related to conservation efforts.
Subscribe to newsletters for the latest updates and news.
Features
Donations: Securely accept and manage donations.
Posts: Create, read, update, and delete articles and updates.
Newsletter Subscription: Users can subscribe to receive regular newsletters.
Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: SQLite (for development), PostgreSQL (for production)
Deployment: Heroku
Setup Instructions
Prerequisites
Python 3.x
pip (Python package installer)
Git
Virtualenv (optional but recommended)


Installation
Clone the Repository
git clone  https://github.com/madol-abraham/Ecoaware_2.git
 cd ecoaware_2
2.Create a Virtual Environment
python -m venv env source env/bin/activate # On Windows use `env\Scripts\activate`
3. Install Dependencies
pip install -r requirements.txt
4. Apply Migrations
 python manage.py migrate
5.Create a Superuser 
python manage.py createsuperuser
6. Run the Development Server
python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/


Usage
Accessing the Admin Panel
Navigate to http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created earlier. From here, you can manage donations, posts, and newsletters.
Frontend Integration
To import the frontend into Django:
Place your HTML, CSS, and JavaScript files in the appropriate directories within your Django app.
Update the settings.py file to include the frontend templates and static files.
Use Django's template engine to render the frontend pages.
Contributing
We welcome contributions to improve the EcoAware web application! Here's how you can help:
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
Contact
For any inquiries or feedback, please reach out to Madol Abraham Kuol Madol at 
m.madol@alustudent.com.


Thank you for using EcoAware! Together, we can make a difference in protecting our planet.
