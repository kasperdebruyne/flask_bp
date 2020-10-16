from app import create_app

# for prod
from dotenv import load_dotenv
load_dotenv('.env')  #the path to your .env file (or any other file with environment variables you want to load)

app = create_app()