from FinishLineApp.__init__ import create_app

import os
from dotenv import load_dotenv

basedir = os.path.dirname(__file__)
load_dotenv(os.path.join(basedir, '.env'))

app_type = os.environ.get("APP_TYPE")

app = create_app(app_type)

if __name__ == "__main__":
    app.run()