import math

class Location:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

    def calculate_distance(self, other_location, unit="km"):
        import math
        # Haversine formula to calculate distance between two points on the Earth
        
        radius_km = 6371                    # Earth radius in kilometers
        radius_mi = (radius_km * 0.621371)  # Earth of radius in miles
        
        dlat = math.radians(other_location.latitude - self.latitude)
        dlon = math.radians(other_location.longitude - self.longitude)
        a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(self.latitude)) * \
            math.cos(math.radians(other_location.latitude)) * math.sin(dlon / 2) ** 2
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        valid_units = ["km", "kilometers", "miles", "mi"]
        if unit.lower() not in valid_units:
            raise ValueError(f"Invalid unit '{unit}'. Please use one of the following: {', '.join(valid_units)}.")
                
        if unit.lower() in ["miles", "mi"]:
            radius = radius_mi
        else:
            radius = radius_km
        
        distance = radius * c
        
        return f"{distance:.2f} {unit.lower()}"
