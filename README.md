# GenLayer Weather Suite

A comprehensive weather data library for GenLayer Intelligent Contracts.
Fetch real-time temperature, humidity, wind speed, and forecasts directly
on-chain — no oracles, no middleware, no third-party trust required.

## Features

- Get current temperature for any city
- Get current humidity for any city
- Get current wind speed for any city
- Get a full weather forecast summary
- Compare weather between two cities side by side

## Contract Functions

| Function | Input | Output |
|----------|-------|--------|
| `get_temperature(city)` | City name | Temperature in Celsius |
| `get_humidity(city)` | City name | Humidity percentage |
| `get_wind_speed(city)` | City name | Wind speed in km/h |
| `get_full_forecast(city)` | City name | Full weather summary |
| `compare_weather(city1, city2)` | Two city names | Side-by-side comparison |

## How to Use

1. Open [GenLayer Studio](https://studio.genlayer.com)
2. Create a new contract
3. Paste the contents of `weather_suite.py`
4. Deploy to the GenLayer testnet
5. Call any function with a city name like `Lagos`, `London`, or `New York`

## Example Output

**get_full_forecast("Lagos")**
**compare_weather("Lagos", "London")**
## Built With

- [GenLayer](https://genlayer.com) — AI-powered blockchain
- [wttr.in](https://wttr.in) — Free weather API

## License

MIT
