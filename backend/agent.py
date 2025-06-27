from datetime import datetime, timedelta
import string
import dateparser
import re
from backend.calendar_utils import check_availability, create_event, get_day_events


def get_next_weekday(target_weekday: str):
    weekdays = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }
    today = datetime.now()
    target = weekdays.get(target_weekday.lower())
    if target is None:
        return None
    days_ahead = (target - today.weekday() + 7) % 7
    days_ahead = days_ahead if days_ahead else 7
    return today + timedelta(days=days_ahead)


def chat_with_user(user_input: str):
    print("🛠️ Raw user_input:", user_input)
    user_input = user_input.lower()

    # ✅ 1. Check availability intent
    if "am i free" in user_input or "do i have anything" in user_input or "is my calendar" in user_input:
        match = re.search(
            r"(tomorrow|today|on .*|next .*|[0-9]{1,2} .*|july .*|august .*|monday|tuesday|wednesday|thursday|friday|saturday|sunday)",
            user_input
        )
        date_text = match.group() if match else user_input
        date_text = date_text.translate(str.maketrans('', '', string.punctuation)).strip()
        print("📅 Extracted date phrase:", date_text)

        parsed_date = dateparser.parse(
            date_text,
            settings={
                'PREFER_DATES_FROM': 'future',
                'TIMEZONE': 'Asia/Kolkata',
                'TO_TIMEZONE': 'Asia/Kolkata',
                'RETURN_AS_TIMEZONE_AWARE': False
            },
            languages=['en']
        )

        # 🛠️ Fallback if "next friday" etc. fails to parse
        if not parsed_date and "next" in date_text:
            parts = date_text.split()
            if len(parts) >= 2 and parts[1] in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                parsed_date = get_next_weekday(parts[1])

        print("🧠 Parsed date:", parsed_date)

        if not parsed_date:
            return "❓ I couldn't understand the date. Try asking like 'Am I free tomorrow?'"

        events = get_day_events(parsed_date)
        if not events:
            return "✅ You're free on that day! No meetings scheduled."
        else:
            response = "📅 You have these events:\n"
            for event in events:
                summary = event.get('summary', 'No title')
                start = event['start'].get('dateTime', event['start'].get('date'))
                response += f"• {summary} at {start}\n"
            return response

    # ✅ 2. Booking intent
    if "book" in user_input or "schedule" in user_input or "meeting" in user_input:
        match = re.search(
            r"(tomorrow|today|next\s+\w+|on\s+\w+day|july\s+\d{1,2}|august\s+\d{1,2}|\w+day|\d{1,2}(st|nd|rd|th)?\s+\w+)",
            user_input
        )

        time_text = match.group() if match else user_input
        print("🧪 Extracted time text:", time_text)

        parsed_time = dateparser.parse(
            time_text,
            settings={
                'PREFER_DATES_FROM': 'future',
                'TIMEZONE': 'Asia/Kolkata',
                'TO_TIMEZONE': 'Asia/Kolkata',
                'RETURN_AS_TIMEZONE_AWARE': False
            },
            languages=['en']
        )
        print("🧠 Parsed time:", parsed_time)

        if not parsed_time:
            return "❓ I couldn't understand the time. Try something like 'Book a meeting tomorrow at 4 PM'."

        start_dt = parsed_time + timedelta(minutes=10)
        end_dt = start_dt + timedelta(minutes=30)

        start = start_dt.strftime("%Y-%m-%dT%H:%M:%S+05:30")
        end = end_dt.strftime("%Y-%m-%dT%H:%M:%S+05:30")

        print(f"🔁 Parsed and checking slot: {start} → {end}")
        if check_availability(start, end):
            event = create_event("Meeting with TailorTalk", start, end)
            return f"✅ Booked your slot: {event.get('htmlLink')}"
        else:
            return "❌ Sorry, that slot is not available."

    return "👋 Tell me when you'd like to schedule your meeting."
