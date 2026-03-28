def calculate_descent(altitude):

    try:
        #  Validation
        if altitude is None:
            raise ValueError("Altitude cannot be None")

        altitude = float(altitude)

        if altitude < 0:
            raise ValueError("Altitude must be >= 0")

        #  Atmospheric layers (top, bottom, speed m/s)
        layers = [
            (10000, 700, 2000),  # Exosphere
            (700, 85, 500),      # Thermosphere
            (85, 50, 200),       # Mesosphere
            (50, 12, 75),        # Stratosphere
            (12, 0, 20),         # Troposphere
        ]

        total_time = 0.0

        #Convert km to meters 
        altitude_m = altitude * 1000

        for top, bottom, speed in layers:

            top_m = top * 1000
            bottom_m = bottom * 1000

            if altitude_m > bottom_m:

                # distance traveled in this layer
                start = min(altitude_m, top_m)
                end = bottom_m

                distance = start - end

                if distance > 0:
                    time = distance / speed
                    total_time += time

        return round(total_time, 1)

    except Exception as e:
        return f"Error: {e}"