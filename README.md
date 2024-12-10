# WeatherApp

WeatherApp is a desktop application built with Python and Tkinter that provides real-time weather information for any city. It fetches data from the OpenWeatherMap API and displays it in a user-friendly interface.

## Features
- Get current weather information for any city.
- Displays weather conditions, temperature, and an icon representing the weather.
- Modern and intuitive user interface.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mihir13/WeatherApp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd WeatherApp
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Set your OpenWeatherMap API key as an environment variable:
   ```bash
   export WEATHER_API_KEY='your_api_key_here'
   ```

## Usage
Run the application:
```bash
python WeatherApp.py
```
Enter the city name in the input field and click "Get Weather" to see the current weather information.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
