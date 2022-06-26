# Django Ecommerce Application

Developed with Test Driven Development approach. Technologies used: Django, Docker, PostgreSQL, Elasticsearch.

To run the application:
- Download the project and move to the project directory
- Create a virtual environment: <sub>python -m venv venv </sub>
- Activate the virtual environment: <sub> venv\Scripts\Activate </sub>
- Install poetry: <sub> pip install poetry</sub>
- Install dependencies specified in pyproject.toml : <sub>poetry update </sub>
- Create and run Docker container: <sub> docker-compose up -d </sub>
- Load predefined fixtures into the dockerized PostgreSQL: <sub> python manage.py load-fixtures </sub>
- Run the application: <sub>python manage.py runserver </sub>
