import os

# Method 1: Get with default
api_key = os.environ.get('API_KEY', 'demo-key')

# Method 2: Check if exists
if 'API_KEY' in os.environ:
    api_key = os.environ['API_KEY']
else:
    print("No API key found")

# Method 3: Will crash if not found
api_key = os.environ['API_KEY']  # KeyError if missing!