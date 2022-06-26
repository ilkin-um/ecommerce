# Django Ecommerce Application

Developed with Test Driven Development approach. Technologies used: Django, Docker, PostgreSQL, Elasticsearch.

To run the application:
- Download the project and move to the project directory
- Create a virtual environment: ` python -m venv venv `
- Activate the virtual environment: ` venv\Scripts\Activate `
- Install poetry: ` pip install poetry `
- Install dependencies specified in pyproject.toml : ` poetry update `
- Create and run Docker container: ` docker-compose up -d `
- Load predefined fixtures into the dockerized PostgreSQL: ` python manage.py load-fixtures `
- Run the application: ` python manage.py runserver `
