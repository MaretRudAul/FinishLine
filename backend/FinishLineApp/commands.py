from flask import Flask
from FinishLineApp import db
from FinishLineApp.models import Event, db_fill_samples, db_verify_sample_data, db_fill_with_scrape
from datetime import datetime

def register_commands(app: Flask):
    @app.cli.command("seed_db")
    def seed_db():
        db_fill_with_scrape()
        print("Database seeded!")

