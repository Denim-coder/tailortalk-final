import os
import json
from google.oauth2 import service_account
from datetime import datetime, timedelta
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "primary"

SERVICE_ACCOUNT_INFO = json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"])

def get_service():
    creds = service_account.Credentials.from_service_account_info(
        SERVICE_ACCOUNT_INFO, scopes=SCOPES)
    return build("calendar", "v3", credentials=creds)

def check_availability(start_time, end_time):
    service = get_service()
    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_time,
        timeMax=end_time,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])
    print("\n📅 DEBUG - Checking availability:")
    print("Start:", start_time)
    print("End:  ", end_time)
    print("📋 Total events found:", len(events))
    for event in events:
        print("  ➤", event.get('summary'), event.get('start'), event.get('end'))

    return len(events) == 0

def create_event(summary, start_time, end_time):
    service = get_service()
    event = {
        "summary": summary,
        "start": {"dateTime": start_time, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end_time, "timeZone": "Asia/Kolkata"},
    }
    return service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

def get_day_events(date_obj):
    service = get_service()
    start = datetime(date_obj.year, date_obj.month, date_obj.day, 0, 0).isoformat() + "+05:30"
    end = datetime(date_obj.year, date_obj.month, date_obj.day, 23, 59).isoformat() + "+05:30"

    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start,
        timeMax=end,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    return events_result.get("items", [])
