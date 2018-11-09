Deployed to AWS Elastic Beanstalk here: http://jack-tss.us-east-2.elasticbeanstalk.com/

# How to run
*Requirements: Python3*

1. `python3 -m venv appenv`
2. `source appenv/bin/activate`
3. `git clone https://github.com/jackcbrown89/django-timestamp-server.git`
4. `cd django-timestamp-server`
5. `pip install -r requirements.txt`
6. `python manage.py runserver`
7. Open http://127.0.0.1:8000/
