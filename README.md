Awwwards
===================

- - - -
Author: [Brian Mutai](https://github.com/Brayonski)
## Description
[Awwwards](https://awwwardy.herokuapp.com/) This is a web app that users can post projects,view,rate and search fr detailed description of the project. 

------------------------------------------------------------------------

## User 

1. View his/her profile page.
2. View projects overal score.
3. Search for projects.
4. Rate / review other users projects.
5. Post a project to be rated / reviewed.
6. View posted projects and their details.

## Features

+ [x] View posted projects and their details
+ [x] post a project to be rated / reviewed
+ [x] View my profile page
+ [x] Rate and review other users projects
+ [x] Search for projets
+ [x] View projects overal score
+ [ ] Creating API endpoints



## Installation

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python 3.6.4

### Cloning the repository
```bash
git clone https://github.com/Brayonski/awwwards && cd Gallery
```

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip3 install -r requirements
```

### Running Tests
```bash
python3 manage.py test
```

### Running the web app in development
```bash
./start.sh
```

## Live Demo

The web app can be accessed from the following link

https://awwwardy.herokuapp.com/

## Quickstart

```
usage: manage.py [-?] {server,test,shell,runserver} ...

positional arguments:
  {server,test,shell,runserver}
    server              Runs the Flask development server i.e. app.run()
    test                Run the unit tests.
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help            show this help message and exit
```

## Technology used

* [Django]

## Contributing

- Git clone [https://github.com/Brayonski/awwwards]
- Write your tests on `tests/`
- If everything is OK. push your changes and make a pull request. ;)

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Brian Mutai](https://github.com/Brayonski)

