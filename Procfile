release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn rest_ifsc_bank.wsgi --log-file -
