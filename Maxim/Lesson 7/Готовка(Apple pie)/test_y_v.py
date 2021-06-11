# pip install google-api-python-client
from googleapiclient.discovery import build

api_key = 'AIzaSyDW8niLw8vOdR9SMHZmgeCNtKapBuB0AiY'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.videos().list(
    part='contentDetails',
    id='I8K3iYcxPl0'
)

response = request.execute()
print(response)