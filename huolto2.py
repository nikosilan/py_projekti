import random

# Define possible airports and their event weights
airports = {
    "Lontoo": {"service_chance": 0.5, "refuel_chance": 0.3, "bonus_chance": 0.1},
    "Helsinki": {"service_chance": 0.4, "refuel_chance": 0.4, "bonus_chance": 0.05},
    "New York": {"service_chance": 0.6, "refuel_chance": 0.3, "bonus_chance": 0.15},
    "Tokyo": {"service_chance": 0.3, "refuel_chance": 0.5, "bonus_chance": 0.2},
}

airport = "Lontoo"  # Starting airport (can be changed dynamically)

# Define the player's initial plane condition
plane_health = 100
fuel_level = 50


def airport_service_event(airport):
    """
    Random event at the airport, including maintenance, refueling, or a lucky bonus.
    The event chances depend on the airport.
    """
    service_chance = airports[airport]["service_chance"]
    refuel_chance = airports[airport]["refuel_chance"]
    bonus_chance = airports[airport]["bonus_chance"]

    roll = random.random()

    # Handle service (maintenance) event
    if roll < service_chance:
        return "Huolto: Lentokoneesi on tarkastettu ja korjattu.", "maintenance"

    # Handle refuel event
    elif roll < service_chance + refuel_chance:
        return "Tankkaus: Lentokoneesi on tankattu.", "refuel"

    # Handle lucky bonus event
    elif roll < service_chance + refuel_chance + bonus_chance:
        return "Onnen bonus: Löysit aarteen! Saat 50€.", "bonus"

    # No event happens
    else:
        return "Ei tapahtumaa.", "none"


def update_plane_condition(event_type):
    global plane_health, fuel_level

    if event_type == "maintenance":
        plane_health = min(100, plane_health + 10)  # Max health is 100
    elif event_type == "refuel":
        fuel_level = min(100, fuel_level + 20)  # Max fuel is 100
    elif event_type == "bonus":
        return 50  # Player gets 50€ bonus (you can use this for upgrades later)
    return 0  # No bonus if event is "none"


# Run the event function
tapahtuma, event_type = airport_service_event(airport)

# Update plane condition based on event
bonus = update_plane_condition(event_type)

# Print the outcome
print(f"Saavuit lentokentälle: {airport}")
print(f"Tapahtuma: {tapahtuma}")

# If player got a bonus, print it
if bonus:
    print(f"Sait bonusrahaa: {bonus}€")

# Display updated plane condition
print(f"Lentokoneen kunto: {plane_health}%")
print(f"Lentokoneen polttoaine: {fuel_level}%")
