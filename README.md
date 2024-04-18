# job_finder

A Django project that fetches jobs from an API.
Users need to register then add queries to fetch from the api.

## Requirements

- API-key from [jsearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch)

## Installation

To install and run the project:

- Add your API-key to a .env-file in job_finder/job_finder/.env like this:\
`API_KEY=<Your_api_key>`
- Open a terminal in the project directory
- (optional) Create a virtual environment
- - run `python -m venv <name of virtual environment>`
- - activate virtual environment:
- - - Unix: `source <name of virtual environment>/bin/acrivate`
- - - Windows: `<name of virtual environment>\Scripts\activate.bat`
- run `pip install -r requirements.txt`
- run `python manage.py migrate`
- run `python manage.py runserver`

## Using the project

While the server is running, it should by default be running on `localhost:8000`.\
Open `localhost:8000` in a browser, you should encounter a login page.\
Log in if you have an account, otherwise register.\
Once registered you will encounter an empty page.\
Press "Edit profile" where you can add queries to your user.\
Example query: `Python developer Stockholm` - Finds Python developer jobs in Stockholm.\
If you now press `Jobs` or go back to `localhost:8000` it should populate an accordion with jobs.\
Each query will get its own accordion item.