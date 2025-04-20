## Features
- Predicts energy consumption in kWh.
- Takes into account weather parameters such as temperature, humidity, and wind speed.
- Supports location-based weather data fetching.
- Provides easy-to-understand predictions with an intuitive interface.

## Tech Stack
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn (Random Forest Regressor)
- **APIs**: OpenWeatherMap API for weather data
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git

## Installation Instructions

### Prerequisites
- Python 3.x
- Pip (Python package manager)

### Steps to Run the Project Locally:
1. Clone the repository:
   git clone https://github.com/sampada-dubey/energy-consumption-predictor

2. Navigate to the project folder:
   cd energy-consumption-project

3. Create a virtual environment (optional but recommended):
   python -m venv venv

4. Activate the virtual environment:
- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```
5. Install the dependencies:
   pip install -r requirements.txt

6. Run the application:
   python app.py

7. Visit `http://127.0.0.1:5000/` in your browser.

## Usage
- Once the app is running, open your browser and go to the home page.
- Enter the required details such as hour, day, month, and location for weather data.
- Click on "Predict" to get the energy consumption prediction in kWh based on the input values and weather data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Thanks to OpenWeatherMap API for providing weather data.
- Special thanks to the contributors of Scikit-learn for the Random Forest implementation.