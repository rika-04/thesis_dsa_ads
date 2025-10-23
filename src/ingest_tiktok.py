import requests
import os
from src.get_tiktok_token import get_access_token
import pandas as pd
# fundamental way to read credentials from this file
# It doesn’t return any data but rather loads all variables to the environment and we can store them into Python variables with os the library.
from dotenv import load_dotenv

 # fetch a new 2-hour token automatically, since the token renews in 7200s (2h)
ACCESS_TOKEN = get_access_token() 
