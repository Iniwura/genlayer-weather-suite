from genlayer import *

@gl.public.view
def get_temperature(city: str) -> str:
    """Fetch the current temperature for any city."""
    data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
    return gl.exec_prompt(
        f"From this weather data, extract ONLY the current temperature "
        f"in Celsius for {city}. Return just the number and unit, nothing else: {data}"
    )

@gl.public.view
def get_humidity(city: str) -> str:
    """Fetch the current humidity percentage for any city."""
    data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
    return gl.exec_prompt(
        f"From this weather data, extract ONLY the current humidity "
        f"percentage for {city}. Return just the number and percent sign, nothing else: {data}"
    )

@gl.public.view
def get_wind_speed(city: str) -> str:
    """Fetch the current wind speed for any city."""
    data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
    return gl.exec_prompt(
        f"From this weather data, extract ONLY the current wind speed "
        f"in km/h for {city}. Return just the number and unit, nothing else: {data}"
    )

@gl.public.view
def get_full_forecast(city: str) -> str:
    """Get a complete weather summary for any city."""
    data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
    return gl.exec_prompt(
        f"From this weather data for {city}, provide a clean summary including: "
        f"current temperature in Celsius, humidity percentage, wind speed in km/h, "
        f"and a brief weather condition description. Format it neatly: {data}"
    )

@gl.public.view
def compare_weather(city1: str, city2: str) -> str:
    """Compare current weather between two cities side by side."""
    data1 = gl.get_webpage(f"https://wttr.in/{city1}?format=j1")
    data2 = gl.get_webpage(f"https://wttr.in/{city2}?format=j1")
    return gl.exec_prompt(
        f"Compare the current weather between {city1} and {city2}. "
        f"Data for {city1}: {data1}. Data for {city2}: {data2}. "
        f"Return a brief comparison of temperature, humidity and wind speed for both cities."
    )

@gl.public.view
def get_uv_index(city: str) -> str:
    """Fetch the current UV index for any city."""
    data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
    return gl.exec_prompt(
        f"From this weather data, extract ONLY the current UV index for {city}. "
        f"Return just the number and a one-word risk level (Low/Moderate/High/Very High): {data}"
    )

@gl.public.view
def get_3day_forecast(city: str) -> str:
    """Get a 3-day weather forecast for any city."""
    data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
    return gl.exec_prompt(
        f"From this weather data for {city}, extract the 3-day forecast. "
        f"For each day return: date, max temperature, min temperature, and weather condition. "
        f"Format each day on a new line clearly: {data}"
    )

