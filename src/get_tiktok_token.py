import requests
import os
# fundamental way to read credentials from this file
# It doesn’t return any data but rather loads all variables to the environment and we can store them into Python variables with os the library.
from dotenv import load_dotenv

# load .env file to environment
load_dotenv()

CLIENT_KEY=os.getenv("TIKTOK_CLIENT_KEY")
CLIENT_SECRET=os.getenv("TIKTOK_CLIENT_SECRET")

def get_access_token():
    url="https://open.tiktokapis.com/v2/oauth/token/"
    headers={"Content-Type":"application/x-www-form-urlencoded"}
    data={
        "client_key":CLIENT_KEY, 
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
    }
    
    # sends the POST request to TikTok with your credentials and waits for a response.
    # TikTok checks your keys → validates your app → and responds with a JSON containing the token.
    response = requests.post(url, headers=headers, data=data)

    # ensures your script will crash cleanly (raise an error) if TikTok returns something like “401 Unauthorized” or “400 Bad Request.”
    # Without it, you’d silently get bad responses and keep going.
    response.raise_for_status()

    token_info = response.json()

    access_token=token_info.get("access_token")
    print(access_token)
    return access_token

if __name__ == "__main__":
    get_access_token()