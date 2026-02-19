📅 Booking System API

This is a Django REST Framework–based Booking System API that allows customers to create bookings, select services, and apply offers. The system manages customers, bookings, services, and promotional offers with proper relational integrity.

🚀 Features

Create and manage customers

Create bookings with date & time

Assign multiple services to a booking

Assign multiple offers to services

Automatically handle booking confirmation timestamps

Prevent duplicate bookings for same customer, date, and time

Nested API responses (services inside bookings, bookings inside customers)

🛠️ Tech Stack

Python 3.12

Django 6+

Django REST Framework

PostgreSQL (recommended)

📂 Project Structure

Customer

Name

Email (unique)

Phone number (unique)

Booking

Customer (ForeignKey)

Booking date & time

Number of guests

Status (Pending / Confirmed / Cancelled)

Many-to-many relationship with Services

Auto confirmation timestamp when status becomes Confirmed

Service

Name

Description

Price

Duration

Category

Availability

Image URL

Many-to-many relationship with Offers

Offer

Name

Discount percentage
