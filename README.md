#librarian

Use the following commands to run:  
`python manage.py makemigrations `  
`python manage.py migrate `  
`python manage.py runserver `  
or using docker:  
`docker build -t librarian:latest .`  
`docker run -d -p 8000:8000 --name librarian_server librarian:latest`