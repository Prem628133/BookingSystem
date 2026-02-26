📅 Booking System API

A Django REST Framework–based Booking System API designed to manage users, bookings, services, and promotional offers with proper relational integrity and role-based architecture.

The system supports JWT authentication, prevents duplicate bookings, and automatically manages booking confirmation timestamps.

🚀 Features

1.Custom User Model with Roles (ADMIN / STAFF / CUSTOMER)

2.JWT Authentication (Access & Refresh Tokens)

3.Booking creation and management

4.Service management

5.Offer management

6.Many-to-many relationship between Bookings and Services

7.Many-to-many relationship between Services and Offers

8.Automatic confirmation timestamp handling

9.Duplicate booking prevention

10.PostgreSQL database support

11.Dockerized environment

🛠️ Tech Stack

1.Python 3.12

2.Django 6+

3.Django REST Framework

4.Simple JWT

5.PostgreSQL

6.Docker & Docker Compose

📂 Data Models
👤 User (Custom User Model)

1.Extends Django's AbstractUser.

Fields:

1.username (unique)

2.password

3.role (ADMIN / STAFF / CUSTOMER)

4.email

5.phone_number

This model replaces the need for a separate Customer model.

📅 Booking

Fields:

1.customer (ForeignKey to User)

2.booking_date

3.booking_time

4.number_of_guests

5.status (Pending / Confirmed / Cancelled)

6.is_confirmed

7.confirmed_at

8.cancelled_at

9.services (ManyToMany → Service)

10.created_at

Constraints

1.Unique booking per customer, date, and time.

Automatic Behavior

When status changes to Confirmed, the system automatically:

1.Sets confirmed_at

2.Sets is_confirmed = True

💼 Service

Fields:

1.name

2.description

3.price

4.duration

5.category

6.is_available

7.image_url

8.offers (ManyToMany → Offer)

🎁 Offer

Fields:

1.name

2.discount_percentage

3.start_date

4.end_date

🔐 Authentication

Authentication is handled using JWT (JSON Web Tokens).

The system provides:

1.Token obtain endpoint

2.Token refresh endpoint

3.Protected endpoints require a valid access token in the Authorization header.

🐳 Docker Setup

The project includes Docker configuration for:

1.Web application container

2.PostgreSQL database container

3.Persistent database volume

To start the project:

~docker compose up --build

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

1.Unique username enforced

2.Unique booking per customer, date, and time

3.ForeignKey constraints maintained

4.Many-to-many relationships handled correctly

5.JWT authentication required for secured endpoints

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

-Prem Kumar
-Django REST Framework Booking System API

Name

1.Discount percentage


