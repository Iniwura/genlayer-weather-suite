from genlayer import *

class WeatherSuite(gl.Contract):
    """
    GenLayer Weather Suite
    A comprehensive weather data library for Intelligent Contracts.
    Fetches real-time weather data from wttr.in — no API keys required.
    """

    def __init__(self):
        pass

    @gl.public.view
    def get_temperature(self, city: str) -> str:
        """Fetch the current temperature for any city in Celsius."""
        data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
        return gl.exec_prompt(
            f"From this weather data, extract ONLY the current temperature "
            f"in Celsius for {city}. Return just the number and unit, nothing else: {data}"
        )

    @gl.public.view
    def get_humidity(self, city: str) -> str:
        """Fetch the current humidity percentage for any city."""
        data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
        return gl.exec_prompt(
            f"From this weather data, extract ONLY the current humidity "
            f"percentage for {city}. Return just the number and percent sign, nothing else: {data}"
        )

    @gl.public.view
    def get_wind_speed(self, city: str) -> str:
        """Fetch the current wind speed for any city in km/h."""
        data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
        return gl.exec_prompt(
            f"From this weather data, extract ONLY the current wind speed "
            f"in km/h for {city}. Return just the number and unit, nothing else: {data}"
        )

    @gl.public.view
    def get_full_forecast(self, city: str) -> str:
        """Get a complete weather summary including all conditions for any city."""
        data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
        return gl.exec_prompt(
            f"From this weather data for {city}, provide a clean summary including: "
            f"current temperature in Celsius, humidity percentage, wind speed in km/h, "
            f"and a brief weather condition description. Format it neatly: {data}"
        )

    @gl.public.view
    def compare_weather(self, city1: str, city2: str) -> str:
        """Compare current weather between two cities side by side."""
        data1 = gl.get_webpage(f"https://wttr.in/{city1}?format=j1")
        data2 = gl.get_webpage(f"https://wttr.in/{city2}?format=j1")
        return gl.exec_prompt(
            f"Compare the current weather between {city1} and {city2}. "
            f"Data for {city1}: {data1}. Data for {city2}: {data2}. "
            f"Return a brief comparison of temperature, humidity and wind speed for both cities."
        )

    @gl.public.view
    def get_uv_index(self, city: str) -> str:
        """Fetch the current UV index and risk level for any city."""
        data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
        return gl.exec_prompt(
            f"From this weather data, extract ONLY the current UV index for {city}. "
            f"Return just the number and a one-word risk level (Low/Moderate/High/Very High): {data}"
        )

    @gl.public.view
    def get_3day_forecast(self, city: str) -> str:
        """Get a 3-day weather forecast for any city."""
        data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
        return gl.exec_prompt(
            f"From this weather data for {city}, extract the 3-day forecast. "
            f"For each day return: date, max temperature, min temperature, and weather condition. "
            f"Format each day on a new line clearly: {data}"
        )

    @gl.public.view
    def get_feels_like(self, city: str) -> str:
        """Fetch the feels-like temperature for any city."""
        data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
        return gl.exec_prompt(
            f"From this weather data for {city}, extract ONLY the feels-like temperature in Celsius. "
            f"Return just the number and unit, nothing else: {data}"
        )

    @gl.public.view
    def is_raining(self, city: str) -> str:
        """Check if it is currently raining in any city."""
        data = gl.get_webpage(f"https://wttr.in/{city}?format=j1")
        return gl.exec_prompt(
            f"Based on this weather data for {city}, is it currently raining or about to rain? "
            f"Answer with only Yes or No followed by one short reason: {data}"
        )

