# Notetake

Notetake is a Django-based web application that allows users to upload and share class-specific documents. Users can upload documents, and others can download and utilize them.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- **User Authentication:** Users can create accounts and log in to the system.
- **Document Upload:** Users can upload class-specific documents.
- **Document Download:** Users can browse and download documents uploaded by others.
- **Inline PDF Viewing:** View uploaded PDF documents directly within the application.
- **RESTful API Endpoints:** Expose API endpoints for interacting with the application programmatically.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Django

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rajdhal/Notetake.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Notetake
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Environment Configuration

To run the application, you need to set up a `.env` file with a Django secret key. Follow these steps:

1. Create a new file named `.env` in the root of the project.

2. Open the `.env` file in a text editor and add the following line:

   ```plaintext
   SECRET_KEY = your_django_secret_key
   ```

   Replace `your_django_secret_key` with a secure and unique secret key. You can generate one using:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. Save the `.env` file into the root folder.

### Continue with Installation

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Log in with the superuser credentials created in step 5.

## Usage

1. Log in or create an account.
2. Upload class-specific documents.
3. Browse and download documents uploaded by others.
4. View PDF documents inline within the application.
5. Utilize the RESTful API endpoints for programmatic interaction.
6. Note: Only admin accounts can add or change the list of courses.

## Contributing

Contributions are welcome! Please follow these guidelines:

- Fork the repository.
- Create a new branch: `git checkout -b feature-name`
- Make your changes and commit them: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin feature-name`
- Submit a pull request.
