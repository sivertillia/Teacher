from http.client import responses
from googleapiclient.discovery import build

api_key = 'AIzaSyDW8niLw8vOdR9SMHZmgeCNtKapBuB0AiY'

youtube = build('youtube', 'v3', developerKey=api_key)

r = youtube.channels().list(
    part='brandingSettings',
    # id='eugenesagaz'
    forUsername='eugenesagaz'
)

response = r.execute()
print(response)