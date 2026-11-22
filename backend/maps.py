
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# -------------------------------
# GOOGLE MAPS API KEY
# -------------------------------


# -------------------------------
# GET DISTANCE & DURATION
# -------------------------------
def get_distance_and_duration(source, destination):
    url = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
        "origin": source,
        "destination": destination,
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # ✅ SAFETY CHECK
    if data.get("status") != "OK" or not data.get("routes"):
        return None, None

    leg = data["routes"][0]["legs"][0]

    distance_km = leg["distance"]["value"] / 1000
    duration_text = leg["duration"]["text"]

    return distance_km, duration_text


# -------------------------------
# CALCULATE TIME PER MODE
# -------------------------------
def calculate_time_by_mode(distance_km):
    speeds = {
        "Metro": 35,   # km/h
        "Bus": 20,
        "Auto": 25,
        "Cab": 30
    }

    times = {}

    for mode, speed in speeds.items():
        hours = distance_km / speed
        minutes = int(hours * 60)
        times[mode] = f"{minutes} mins"

    return times


# -------------------------------
# CALCULATE COST PER MODE
# -------------------------------
def calculate_cost_by_mode(distance_km):
    costs = {
        "Metro": 30,                  # flat fare
        "Bus": 25,                    # flat fare
        "Auto": int(distance_km * 15),
        "Cab": int(distance_km * 18)
    }

    return costs
