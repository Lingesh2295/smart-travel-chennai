from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from maps import (
    get_distance_and_duration,
    calculate_time_by_mode,
    calculate_cost_by_mode
)

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve frontend


@app.get("/")
def serve_ui():
    return FileResponse("static/index.html")


# Chat API
@app.get("/chat")
def chat(user_message: str):
    # Simple parsing (you can replace with NLP later)
    if " to " not in user_message.lower():
        return {"error": "Please ask like: From A to B"}

    parts = user_message.lower().split(" to ")
    source = parts[0].strip().title()
    destination = parts[1].strip().title()

    distance_km, duration_text = get_distance_and_duration(source, destination)

    if distance_km is None:
        return {"error": "Unable to fetch route. Check locations or API key."}

    # ✅ DEFINE FIRST (this fixes your error)
    mode_times = calculate_time_by_mode(distance_km)
    mode_costs = calculate_cost_by_mode(distance_km)

    return {
        "source": source,
        "destination": destination,
        "distance_km": round(distance_km, 2),
        "estimated_time": duration_text,

        "travel_options": {
            "Metro": {
                "cost": f"₹{mode_costs['Metro']}",
                "time": mode_times["Metro"]
            },
            "Bus": {
                "cost": f"₹{mode_costs['Bus']}",
                "time": mode_times["Bus"]
            },
            "Auto": {
                "cost": f"₹{mode_costs['Auto']}",
                "time": mode_times["Auto"]
            },
            "Cab": {
                "cost": f"₹{mode_costs['Cab']}",
                "time": mode_times["Cab"]
            }
        }
    }
