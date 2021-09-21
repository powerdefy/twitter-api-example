# Twitter API Call Example

Install
-----------
create virtual environment:

    $ virtualenv -p python3 env

activate virtual environment:

    $ source env/bin/activate

install requirement libs using pip:

    $ pip install -r requirement.txt
----
Configuration
-----------
please change application configuration in settings.py:

    PORT= 8888 # Server PORT
    CONSUMER_API_KEY= 'TWITTER CONSUMER KEY' #TWITTER CONSUMER KEY
    CONSUMER_API_SECRET_KEY= 'TWITTER CONSUMER SECRET' #TWITTER CONSUMER SECRET
    AUTH_URL= 'https://api.twitter.com/oauth2/token' #TWITTER OAUTH2.0 URL
    SEARCH_URL= 'https://api.twitter.com/1.1/search/tweets.json' #TWITTER SEARCH URL
    USER_TIMELINE_URL= 'https://api.twitter.com/1.1/statuses/user_timeline.json' #TWITTER USER TIMELINE URL
----
Unit Test
-----------
    $ python tests.py
----
Running
-----------
    $ python app.py
