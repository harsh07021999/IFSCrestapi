### IFSCrestapi

Requirements:-

All the reqiurements are in requirements.txt file

How to run locally :-

Type these commands in cmd:-
virtualenv env
then activate the environment then
pip install -r requirements.txt
python manage.py makemigration
python manage.py migrate
python manage.py runserver

Then follow the instructions in the description given.

Description:-

This an api created to:-

1. Given a bank branch IFSC code, get branch details

2. Given a bank name and city, gets details of all branches of the bank in the city

After setting up locally you can head to :-

http://localhost:8000/api/ifsc/{ifsccode}  (type ifsc code, city and bank-name without any brackets and hiphens to see the work) 

http://localhost:8000/api/branches/{city}/{bank-name}

in your browser to get started.

This website is hosted on pythonanywhere some examples are :-

http://harshdjango.pythonanywhere.com/api/branches/ALLAHABAD/AXIS%20BANK

http://harshdjango.pythonanywhere.com/api/ifsc/CORP0003209
