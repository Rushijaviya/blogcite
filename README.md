# BlogSite
# Publish Your Blog 
This Django aap is for publishing your blog online.

## Deploy on Heroku
https://blogcite.herokuapp.com/

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Rushijaviya/blogcite.git
$ cd blogcite
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv blog
$ blog/Scripts/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Features:
* Publish Your Blog
* Add Featured Image
* Share blog via E-mail
* Add Comments on blog
* Contact Us