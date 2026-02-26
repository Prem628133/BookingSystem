📅 Booking System API

A Django REST Framework–based Booking System API designed to manage users, bookings, services, and promotional offers with proper relational integrity and role-based architecture.

The system supports JWT authentication, prevents duplicate bookings, and automatically manages booking confirmation timestamps.

🚀 Features

Custom User Model with Roles (ADMIN / STAFF / CUSTOMER)

JWT Authentication (Access & Refresh Tokens)

Booking creation and management

Service management

Offer management

Many-to-many relationship between Bookings and Services

Many-to-many relationship between Services and Offers

Automatic confirmation timestamp handling

Duplicate booking prevention

PostgreSQL database support

Dockerized environment

🛠️ Tech Stack

Python 3.12

Django 6+

Django REST Framework

Simple JWT

PostgreSQL

Docker & Docker Compose

📂 Data Models
👤 User (Custom User Model)

Extends Django's AbstractUser.

Fields:

username (unique)

password

role (ADMIN / STAFF / CUSTOMER)

email

phone_number

This model replaces the need for a separate Customer model.

📅 Booking

Fields:

customer (ForeignKey to User)

booking_date

booking_time

number_of_guests

status (Pending / Confirmed / Cancelled)

is_confirmed

confirmed_at

cancelled_at

services (ManyToMany → Service)

created_at

Constraints

Unique booking per customer, date, and time.

Automatic Behavior

When status changes to Confirmed, the system automatically:

Sets confirmed_at

Sets is_confirmed = True

💼 Service

Fields:

name

description

price

duration

category

is_available

image_url

offers (ManyToMany → Offer)

🎁 Offer

Fields:

name

discount_percentage

start_date

end_date

🔐 Authentication

Authentication is handled using JWT (JSON Web Tokens).

The system provides:

Token obtain endpoint

Token refresh endpoint

Protected endpoints require a valid access token in the Authorization header.

🐳 Docker Setup

The project includes Docker configuration for:

Web application container

PostgreSQL database container

Persistent database volume

To start the project:

docker compose up --build

The application runs on port 8000.
PostgreSQL runs on port 5433.

⚙️ Local Development Setup

Create and activate virtual environment

Install dependencies

Configure PostgreSQL database

Run migrations

Create superuser

Start development server

🔒 Data Integrity Rules

Unique username enforced

Unique booking per customer, date, and time

ForeignKey constraints maintained

Many-to-many relationships handled correctly

JWT authentication required for secured endpoints

📌 Future Improvements

Role-based permission enforcement (ADMIN / STAFF restrictions)

Booking slot availability validation

Offer auto-application logic

Payment integration

Email/SMS notifications

API documentation (Swagger / Redoc)

CI/CD integration

Production deployment configuration

👨‍💻 Author

Prem Kumar
Django REST Framework Booking System API

Name

Discount percentage

