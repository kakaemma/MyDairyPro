[![Emmanuel Kakaire](https://img.shields.io/badge/Emmanuel%20Kakaire-MyDiary-green.svg)]()
[![Coverage Status](https://coveralls.io/repos/github/kakaemma/MyDairyPro/badge.svg?branch=challenge2)](https://coveralls.io/github/kakaemma/MyDairyPro?branch=challenge2)
[![Build Status](https://travis-ci.org/kakaemma/MyDairyPro.svg?branch=challenge2)](https://travis-ci.org/kakaemma/MyDairyPro)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-blue.svg)]()

# MyDairyPro
MyDiary is an online journal where users can pen down their thoughts and feelings.
# Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

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
POST| /api/v1/entries |Adds a diary entry 
GET| /api/v1/entries |Retrieves all diary entries 
GET| /api/v1/entries/<diary_id> |Retrieves a single diary entry 
PUT| /api/v1/entries/<diary_id> |Modifies diary entry 


