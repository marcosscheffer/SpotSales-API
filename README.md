# SpotSales Sync

## Description

Develop an integrated platform that centralizes and automates the sales process, with internal communication via Slack and a checklist system to ensure quality and compliance. The platform will allow for the control and management of sellers and users, ensuring that only authorized individuals can access specific information and perform relevant actions.

## Requirements

Before you begin, make sure you have the following installed on your machine:

- Python 3.7 or higher
- pip (Python package manager)
- virtualenv (optional, but recommended)

## Installation
Follow the steps below to set up the development environment:

1. **Clone the repository:**

   ```bash
   git clone git@github.com:marcosscheffer/SpotSales-API.git
   cd SpotSales-API
   ```

2. **Create and activate a virtual environment:**

   On Unix or macOS:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment variables:**

   4.1. **Create a .env file**

   ```bash
   echo. > .env
   ```

   4.2. **Add environment variables**

   Open the `.env` file with your preferred text editor and add the following lines:

   ```plaintext
   MYSQL_USERNAME=yourusername
   MYSQL_PASSWORD=yourpassword
   ```

5. **Run migrations:**

   ```bash
   flask db upgrade
   ```
   
6. **Create a primary position:**

   ```bash
   flask user createprimaryposition
   ```

7. **Create a admin user:**

   ```bash
   flask user createadminuser
   ```

   Follow the prompts to create an admin user for the flask aplication.

## Starting the API
Once you have set up the environment and dependencies, you can start the API in mode development with the following command:

```bash
flask run
```

use the API at the following URL `http://127.0.0.1:8000`.

## Code Coverage

To ensure code quality, we use `coverage.py` to measure test coverage. Follow the steps below to generate and view the code coverage report.

### Installation

`coverage.py` should already be included in the `requirements.txt` file. If not, add the following line to `requirements.txt`:

```plaintext
coverage
pytest
```

Then, install the dependency:

```bash
pip install -r requirements.txt
```

### Running Tests with Coverage

1. **Run the tests and generate coverage data:**

   ```bash
   pytest
   ```

   This command runs all flask tests and collects coverage data.


2. **View the HTML report:**

   The HTML report will be generated in the `htmlcov` directory. To view it, open the `index.html` file in your browser:

   ```bash
   open htmlcov/index.html  # On macOS
   xdg-open htmlcov/index.html  # On Linux
   start htmlcov/index.html  # On Windows
   ```

### Coverage Configuration

Make sure the `pytest.ini` and `.coveragerc` file is correctly configured. Here is an example configuration you can use:

pytest.ini
```ini
[pytest]
testpaths = tests
addopts = --cov=app --cov-report=term --cov-report=html --cov-config=.coveragerc
```
.coveragerc
```ini
[run]
omit =
    */migrations/*
    app/models/*
    app/entities/*
    app/schemas/*
    app/services/*
    app/validations/*
    app/cli.py
    app/extensions.py
    app/config.py
    app/__init__.py
```

### Additional Tips

- **Excluding irrelevant code:** Use the `omit` option in the `.coveragerc` file to exclude files or directories that you do not want to measure coverage for, such as migration or test files.


- **CI/CD Integration:** Consider integrating `coverage.py` with your CI/CD pipeline to ensure code coverage is measured and reported automatically in each build.

## Project Structure
An overview of the project's directory structure:

```plaintext
SpotSales-API/
├── run.py
├── app/
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── lead_sale.py
│   │   ├── position.py
│   │   ├── seller.py
│   │   ├── user.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   ├── checklist_model.py
│   │   ├── lead_sale_model.py
│   │   ├── position_model.py
│   │   ├── seller_model.py
│   │   ├── user_model.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── checklist_schema.py
│   │   ├── lead_sale_schema.py
│   │   ├── position_schema.py
│   │   ├── seller_schema.py
│   │   ├── slack_schema.py
│   │   ├── user_auth_schema.py
│   │   ├── user_schema.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── lead_sale_service.py
│   │   ├── position_service.py
│   │   ├── seller_service.py
│   │   ├── slack_service.py
│   │   ├── user_auth_service.py
│   │   ├── user_service.py
│   ├── validations/
│   │   ├── __init__.py
│   │   ├── foreign_validate.py
│   │   ├── length_validate.py
│   │   ├── unique_validate.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── lead_sale_view.py
│   │   ├── position_view.py
│   │   ├── seller_view.py
│   │   ├── slack_view.py
│   │   ├── user_auth_view.py
│   │   ├── user_view.py
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── extensions.py
├── tests/
│   ├── __init__.py
│   ├── test_lead_sale_view.py
│   ├── test_position_view.py
│   ├── test_seller_view.py
│   ├── test_slack_view.py
│   ├── test_user_auth_view.py
│   ├── test_user_view.py
├── migrations/
├── .env
├── .coveragerc
├── .pytest.ini
├── .flaskenv
├── requirements.txt
└── README.md
```


## Contribution
To contribute to this project:

1. **Fork the repository.**

   Click on the "Fork" button at the top right corner of the repository page on GitHub to create a copy of the repository under your GitHub account.

2. **Clone your forked repository:**

   ```bash
   git clone git@github.com:marcosscheffer/SpotSales-API.git
   cd SpotSales-API
   ```

3. **Create a new branch for your feature or bug fix:**

   ```bash
   git checkout -b my-feature
   ```

4. **Make your changes.**

   Implement your feature or bug fix.

5. **Commit your changes:**

   ```bash
   git add .
   git commit -m "Add my new feature"
   ```

6. **Push to the branch:**

   ```bash
   git push origin my-feature
   ```

7. **Open a Pull Request.**

   Go to the repository on GitHub and you should see a prompt to open a pull request from your new branch. Click "Compare & pull request," add a description of your changes, and submit the pull request.

### Additional Guidelines

- **Code Style:** Ensure your code follows the project's coding style and conventions.
- **Testing:** Run the tests to ensure your changes do not break the existing code. Add tests for your new features or bug fixes if applicable.
- **Documentation:** Update the documentation to reflect your changes if necessary.


