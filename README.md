[![Emmanuel Kakaire](https://img.shields.io/badge/Emmanuel%20Kakaire-MyDiary-green.svg)]()
[![Coverage Status](https://coveralls.io/repos/github/kakaemma/MyDairyPro/badge.svg?branch=challenge3)](https://coveralls.io/github/kakaemma/MyDairyPro?branch=challenge3)
[![Build Status](https://travis-ci.org/kakaemma/MyDairyPro.svg?branch=challenge2)](https://travis-ci.org/kakaemma/MyDairyPro)
[![Maintainability](https://api.codeclimate.com/v1/badges/8bff641ade47dbc52dee/maintainability)](https://codeclimate.com/github/kakaemma/MyDairyPro/maintainability)

# MyDairyPro
MyDiary is an online journal where users can pen down their thoughts and feelings.
# Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

> The API documentation is at;

> https://mydiary3.docs.apiary.io/


# Requirements
`Python 3+, python-pip, virtualenv`

### Installation
Clone the repository

```
git clone https://github.com/kakaemma/MyDairyPro.git
cd MyDiaryPro
```

### Create a virtualenv, and activate it:
I am assuming you are using a windows machine

```
virtualenv env
cd env/Scripts/activate
```

### Then install all dependecies required to run the application

```
pip install requirements.txt
```
```
install PostgreSQL
```
```
CREATE DATABASE mydiary_pro;
CREATE USER admin  PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE mydiary_pro TO admin;

```

### Then, run the application:
```
$ python run.py
```
### To see the application running:
Install postman and access the application at:

```
http://localhost:5000
```
### Running the tests
To run tests, you need nose installed on your computer
```
$ pip install nose
```
running the tests
```
$ nosetests tests
```

### API resources

These are the endpoints available in My Diary API

HTTP Method | Endpoint | Description| 
------------ | ------------- | ------------- 
POST| /api/v1/auth/signup |Register a user
POST| /api/v1/auth/login |Login a user 
POST| /api/v1/entries |Adds a diary entry 
GET| /api/v1/entries |Retrieves all diary entries 
GET| /api/v1/entries/<diary_id> |Retrieves a single diary entry 
PUT| /api/v1/entries/<diary_id> |Modifies diary entry 

[![Demo video](https://user-images.githubusercontent.com/7983999/43614225-74517850-96aa-11e8-9c24-229b853876e5.png)](https://www.youtube.com/watch?v=jst0jaaHGhY)




