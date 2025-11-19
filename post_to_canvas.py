import requests
import sys

# Configuration
CANVAS_URL = "https://canvas.cmu.edu" # Your Canvas URL (E.g. https://canvas.cmu.edu)
COURSE_ID = "50567"  # Our course ID (from the course URL)
TOPIC_ID = "770528"  # Discussion topic ID (from the discussion URL)

# Read the access token from file
try:
    with open("canvas_token.txt", "r") as f:
        ACCESS_TOKEN = f.read().strip()
    
    # Check if token is empty
    if not ACCESS_TOKEN:
        print("Error: Token file is empty!")
        print("Please add your Canvas access token to canvas_token.txt")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: canvas_token.txt file not found!")
    print("Please create a canvas_token.txt file with your access token.")
    sys.exit(1)

# Set up headers with authentication
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# The message you want to post
message_data = {
    "message": "Hello from the Canvas API!"
}

# API endpoint for posting to a discussion
url = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/discussion_topics/{TOPIC_ID}/entries"

# Make the POST request
response = requests.post(url, headers=headers, data=message_data)

# Check if it worked
if response.status_code == 201:
    print("Success! Post created.")
    print(f"Post ID: {response.json()['id']}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
