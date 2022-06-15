# Wanderlust - A travel based blog!

A web application designed as a Blog in which users can read and share their own travel experience

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

The things you need before running this application:

* [Python3.9](https://www.python.org/downloads/release/python-3913/)
* [Visual code](https://code.visualstudio.com/download) (or) [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

## Installation

A step by step guide that will tell you how to get the development environment up and running.


* Step 1: Open Terminal to run these commands
    ```sh
    pip install -r requirements.txt
    ```
    > Note: It is recommended to use a virtualenv
    
* Step 2: 
    ```sh
    python manage.py migrate
    ```
* Step 3: 
    ```sh
    python manage.py runserver
    ```
* Step 4: Open [http://localhost:8000](http://localhost:8000)
    
## Options Available in the web application

1. Create a new Blog post 
2. Update / Delete an existing Blog post 
3. Create a new user
4. Upload profile picture for the user 
5. Access admin site for the application to manage posts and user information
