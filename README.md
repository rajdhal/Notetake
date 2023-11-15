# Notetake

Notetake is a Django-based web application that allows users to upload and share class-specific documents. Users can upload documents, and others can download and utilize them.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication: Users can create accounts and log in to the system.
- Document upload: Users can upload class-specific documents.
- Document download: Users can browse and download documents uploaded by others.
- [Add more features here]

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python [version]
- Django [version]
- [Any other dependencies]

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


## Contributing

Contributions are welcome! Please follow these guidelines:

- Fork the repository.
- Create a new branch: `git checkout -b feature-name`
- Make your changes and commit them: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin feature-name`
- Submit a pull request.