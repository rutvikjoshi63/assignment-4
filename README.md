# Canvas Discussion Poster

A simple Python script that posts messages to Canvas LMS discussion boards using the Canvas API.

## What This Does

This script demonstrates how to:
- Authenticate with the Canvas API using an access token
- Make POST requests to create discussion posts
- Handle errors and read configuration from files

## Prerequisites

- Python 3.6 or higher
- A Canvas LMS account with API access

## Setup

### 1. Install Required Packages
```bash
pip install -r requirements.txt
```

### 2. Get Your Canvas Access Token

1. Log into Canvas
2. Go to **Account** → **Settings**
3. Scroll down to **Approved Integrations**
4. Click **+ New Access Token**
5. Give it a name (e.g., "API Learning Project")
6. Click **Generate Token**
7. **Copy the token immediately** (you won't see it again!)

### 3. Create Your Token File

Create a file named `canvas_token.txt` in the same directory as the script:
```bash
echo "your_token_here" > canvas_token.txt
```

Or just create the file and paste your token in it (no quotes needed).

### 4. Configure the Script

Edit `post_to_canvas.py` and update these values:
```python
CANVAS_URL = "https://your-school.instructure.com"  # Your Canvas URL
COURSE_ID = "123456"   # Your course ID
TOPIC_ID = "789012"    # Discussion topic ID
```

**Finding IDs:**
- **Course ID**: Look at your course URL: `canvas.school.edu/courses/123456`
- **Topic ID**: Open a discussion, look at the URL: `...discussion_topics/789012`

## Usage

Run the script:
```bash
python post_to_canvas.py
```

If successful, you'll see:
```
Success! Post created.
Post ID: 987654
```

## Security Notes

⚠️ **Important**: Your access token is like a password!

- **Never commit `canvas_token.txt` to Git**
- Add it to your `.gitignore`:
```
  canvas_token.txt
```
- Don't share your token with anyone
- Delete tokens you're not using from Canvas settings

## Testing Safely

**Best practices:**
- Create a test discussion board in your course
- Use it for practice before posting to real discussions
- Consider creating a sandbox course for API experiments

## Troubleshooting

### Error: Token file is empty
- Make sure you pasted your token into `canvas_token.txt`
- Check that there are no extra spaces or quotes

### Error: canvas_token.txt file not found
- Make sure the file is in the same directory as your script
- Check the filename spelling

### Error: 401 Unauthorized
- Your token may be invalid or expired
- Generate a new token in Canvas

### Error: 404 Not Found
- Check that your `COURSE_ID` and `TOPIC_ID` are correct
- Make sure you have access to that course/discussion

### Error: 403 Forbidden
- You may not have permission to post in that discussion
- Check if the discussion is locked or restricted

## Customizing Your Post

Change the message in the script:
```python
message_data = {
    "message": "Your custom message here!"
}
```

You can also use HTML formatting:
```python
message_data = {
    "message": "<p>Hello!</p><ul><li>Item 1</li><li>Item 2</li></ul>"
}
```

## Learning Resources

- [Canvas API Documentation](https://canvas.instructure.com/doc/api/)
- [Discussion Topics API](https://canvas.instructure.com/doc/api/discussion_topics.html)
- [Python Requests Library](https://requests.readthedocs.io/)

