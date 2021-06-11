# pip install google-api-python-client
from googleapiclient.discovery import build

api_key = 'AIzaSyDW8niLw8vOdR9SMHZmgeCNtKapBuB0AiY'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    id='UC7f5bVxWsm3jlZIPDzOMcAg'
)

response = request.execute()
print(response)