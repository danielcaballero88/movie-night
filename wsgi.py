from movie_night import create_app
from dotenv import load_dotenv

# Load environment variables for flask command (used for '$ flask run')
# (commented out because its not necessary to load .flaskenv (it is default))
if False:
    # Load here the environment to load properly FLASK_ENV and/or FLASK_DEBUG
    # because they need to be set before creting the app to work ok when
    # called with the flask run command
    import os
    here_path = os.path.dirname(__file__)
    dotenv_path = os.path.join(here_path, '.flaskenv')
    load_dotenv(dotenv_path=dotenv_path)

app = create_app('development')

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')