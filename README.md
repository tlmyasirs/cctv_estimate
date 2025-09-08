# CCTV Cost Estimator

A simple web application to provide a rough estimate for a CCTV system.

## Features

*   Select from a list of available NVRs (Network Video Recorders).
*   Choose from a variety of cameras.
*   Select the required storage size.
*   Get a real-time cost estimate.

## Technologies Used

*   Python
*   Django
*   HTML
*   CSS
*   JavaScript

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd <project-directory>
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1.  Access the application by navigating to `http://127.0.0.1:8000/` in your web browser.
2.  Use the admin panel at `http://127.0.0.1:8000/admin/` to add or modify the NVRs, cameras, and HDDs.
3.  On the main page, select the desired components to see the estimated cost.
