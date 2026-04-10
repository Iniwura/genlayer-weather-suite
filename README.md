# GenLayer Weather Suite

A reusable weather data library for GenLayer Intelligent Contracts to fetch
real-time temperature, humidity, wind speed, UV index, and forecasts for any
city in the world — no API keys required.

## Features

- Current temperature for any city
- Current humidity for any city
- Current wind speed for any city
- Feels-like temperature
- UV index with risk level
- Rain detection
- Full weather summary
- Side-by-side city comparison
- 3-day weather forecast

## Contract Functions

| Function | Input | Output |
|----------|-------|--------|
| `get_temperature(city)` | City name | Temperature in Celsius |
| `get_humidity(city)` | City name | Humidity percentage |
| `get_wind_speed(city)` | City name | Wind speed in km/h |
| `get_feels_like(city)` | City name | Feels-like temperature |
| `get_uv_index(city)` | City name | UV index + risk level |
| `is_raining(city)` | City name | Yes/No + reason |
| `get_full_forecast(city)` | City name | Full weather summary |
| `compare_weather(city1, city2)` | Two city names | Side-by-side comparison |
| `get_3day_forecast(city)` | City name | 3-day forecast |

## How to Deploy

1. Open [GenLayer Studio](https://studio.genlayer.com)
2. Create a new contract
3. Paste the contents of `contracts/weather_suite.py`
4. Click **Deploy**
5. Call any function with a city name

## Example Outputs

**get_full_forecast("Lagos")**
```
Temperature: 31°C
Humidity: 78%
Wind Speed: 14 km/h
Condition: Partly cloudy with light breeze
```

**compare_weather("Lagos", "London")**
```
Lagos: 31°C, 78% humidity, 14 km/h wind
London: 12°C, 85% humidity, 22 km/h wind
Lagos is significantly warmer and less windy than London.
```

**get_3day_forecast("Paris")**
```
Day 1 (Mon): Max 18°C, Min 11°C - Cloudy
Day 2 (Tue): Max 21°C, Min 13°C - Sunny
Day 3 (Wed): Max 16°C, Min 10°C - Light Rain
```

## Repository Structure

```
genlayer-weather-suite/
├── contracts/
│   └── weather_suite.py       # Main Intelligent Contract
├── examples/
│   ├── city_weather_report.py # Single city examples
│   ├── city_comparison.py     # City comparison examples
│   └── forecast_tracker.py   # Forecast examples
├── utils/
│   └── supported_cities.py   # Reference city list
├── LICENSE
└── README.md
```

## Built With

- [GenLayer](https://genlayer.com) — AI-powered blockchain
- [wttr.in](https://wttr.in) — Free open-source weather API

## License

MIT

