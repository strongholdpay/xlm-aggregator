# xlm-aggregator

Aggregation of xlm/btc pricing and volume across various trading platforms.


### Setup

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/xlm-aggregator.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv xlm-aggregator --python=/path/to/python3
    pip install -r requirements.txt

#### Database Setup

You will need to setup a Postgres Database

Install Postgres

Create DB

	createdb stronghold-sandbox

Start a python shell and run the following to create the tables:

	import database
	database.init_db()


### Run Program

Ensure your virtual environment is active, then run the following:

	python get-orderbooks.py


