# Okta Python3 OAuth2 Flask Application

This project is a light weight flask web application used to demonstrate the use of OAuth2 Tokens
from an Okta provider.

---

## Project Structure

**[app.py](app.py)** - contains the Flask application

**[/oauth2](./oauth2/oauth2.py)** - contains the OAuth2 class for JWT authorization use to enable endpoint security

## Installing

Create a virtual environment for Python3

```bash
virtualenv -p python3 envname
source envname/bin/activate
```

Install pip dependencies for project

```bash
pip install -r requirements.txt
```

## Run Server

To run development Server

```bash
flask run
```

## Links

**[Python](https://www.python.org/)** - general information on the Python programming language

**[Flask](http://flask.pocoo.org/)** - information on Flask, microframework for Python

**[Otka](https://developer.okta.com/docs/api/resources/oidc#keys)** - information on Okta's API

## Authors

* **Mark Sikora** - *Initial work* - [LinkedIn](https://www.linkedin.com/in/mark-m-sikora/)

## License

This project is licensed under the MIT License - see the [MIT](https://opensource.org/licenses/MIT) file for details
