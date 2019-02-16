# Flask-Blog Inspired By Corey Schafer

This is an example of a Flask app that demonstrate a simple blog on [Heroku](http://www.heroku.com) and [GCP](http://cloud.google.com). A running version of this app can be found [here](https://cloud.google.com).

Inspired by: [Corey Schafer](https://github.com/CoreyMSchafer).

## Deploy to Heroku

Deploy this app on Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Running Locally

Run the following commands to get started running this app locally:

```sh
$ git clone https://github.com/dungnv2602/flask_blog_showcase.git
$ cd flask_blog
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ FLASK_APP=flask_blog flask db upgrade
(venv) $ FLASK_APP=flask_blog FLASK_ENV=development flask run
```

Then visit `http://localhost:5000` to checkout locally.

## Deploying to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/dungnv2602/flask_blog_showcase.git
$ cd flask_blog
$ heroku create
Creating app... done, ⬢ mighty-beyond-15012
https://mighty-beyond-15012.herokuapp.com/ | https://git.heroku.com/mighty-beyond-15012.git
$ heroku addons:create 
$ heroku addons:create 
$ heroku config:set FLASK_APP=flask_blog
$ heroku config:set SECRET_KEY="`< /dev/urandom tr -dc 'a-zA-Z0-9' | head -c16`"
$ git push heroku master
$ heroku open
```

## Licensing

This example is open-sourced software licensed under the
[MIT license](https://opensource.org/licenses/MIT).

## Configuration for Linux Web Server

## Config Firewall

```sh
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 5000
```

## Get source code

```sh
git clone https://github.com/dungnv2602/flask_blog_showcase.git
```

## Install necessary python packages

```sh
sudo apt install python3-pip
sudo apt install python3-venv
```

## Config python web server

```sh
python3 -m venv flask_blog/venv
cd flask_blog
source venv/bin/activate
pip install -r requirements.txt
```