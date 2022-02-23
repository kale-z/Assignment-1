# Django Text Histogram
This is my first Django practice rendering a text histogram. 


<br>

## Getting Started
A desired or specific text is given in ```views.py```. The text's words are getting counted then append them into a dictionary to iterate over it in a loop for rendering its elements as Listed Items (```<li>```). Currently, I have inserted the following sentence:

> Netflix use information about the things people buy or rent to determine which people or items are similar to one another, and then make recommendations based on purchase history. Other sites like Pandora and Last.fm use your ratings of different bands and songs to create custom radio stations


<br>

## Usage
To run this project after cloning, run the following command first for migration
```
python manage.py migrate
```

Then, running the local server
```
python manage.py runserver
```
_Note: after running the project locally, you may need to add the URL's slug manually from ```urls.py``` as the homepage was not set_
