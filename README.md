# Django Practice [ 1 ]
This is my first Django practice rendering a text histogram. A text is given in ```views.py``` and its words were counted, then appended into a dictionary to be looped over for rendering its elements as Listed Items (```<li>```).

To run this project after cloning, run the following command first for migration
```
python manage.py migrate
```

Then, running the local server
```
python manage.py runserver
```

_Note: after running the project locally, you may need to add the URL's slug manually from ```urls.py``` as the homepage was not set_
