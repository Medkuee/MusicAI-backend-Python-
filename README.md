# INTRO

- This project is for collecting applicant data from various job posting platform.
- We use Python 3.7 + Beautiful Soup + Selenium + AWS for the tech stack.
  - Beautiful Soup Documentation (For parsing the HTML)
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
  - Selenium Documentation (For controlling the browser)
    https://www.selenium.dev/documentation/

# LOCAL INSTALLATION

1. Create virtual environment: `python3 -m venv env`
2. Activate virtual environment: `source env/bin/activate`
3. Install packages: `pip3 install -r requirements.txt`
4. Start a MySql database with docker using: `docker-compose up -d`.
5. Create a `.env` file and add the `DATABASE_URL` environment variable.

   - The `.env.example` file is provided as reference.

6. Start the project: `python3 lambda_function.py`

