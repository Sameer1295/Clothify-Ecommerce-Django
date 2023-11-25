# Clothify - Django Ecommerce Application

## Project Overview

Clothify is a Django-based Ecommerce application designed for clothing stores. It allows users to browse, select, and purchase clothing products. The application provides a wide range of features including product management, user authentication, and shopping cart functionality.

![image](https://github.com/Sameer1295/Clothify-Ecommerce-Django/assets/29782669/e2529c41-dfc8-4e33-8c50-6a2a7eb74736)


## Key Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Vendor Management**: Admins can create and manage vendor accounts.
- **Product Management**: Admins can add and edit product details, including name, description, price, and images.
- **Product Categories**: Products are organized into categories for easy browsing.
- **Size and Color Variants**: Each product can have size and color variants.
- **User Shopping Experience**: Users can view products, get product details, and add them to the shopping cart.
- **Shopping Cart**: Users can manage their shopping cart, update quantities, and proceed to checkout.
- **User-Friendly Interface**: Clothify provides a user-friendly interface to enhance the shopping experience.
- **Checkout**: checkout process for users to finalize their orders.
- **Creating Orders**: feature to create and manage orders for admin users.
- **Payment Integration**: Integration with payment gateways for secure and convenient online payments.

# Project Setup

This Django project requires initial setup steps to configure environment variables, databases, and external service keys.

## Prerequisites

- Python 3.x
- Django
- MySQL (Make sure MySQL is installed and running)
- Razorpay account (for payment gateway integration)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sameer1295/Clothify-Ecommerce-Django.git

2. Cd into project directory
   ```bash
   cd Clothify-Ecommerce-Django/

3. Create .env file using .env.example file
   ```bash 
    cp clothify/.env.example clothify/.env

4. Update .env file with MYSQL DB Credentials and DB name

5. Run migrations
   ```bash
   python manage.py migrate

6. Run server
   ```bash
   python manage.py runserver
