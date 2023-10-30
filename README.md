# Rain Alert 🌧️

Rain Alert is a simple Python script that sends you email alerts when it's going to rain in your area, so you don't forget to carry an umbrella!

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Rain Alert is a Python project that utilizes OpenWeatherMap API to check if it will rain today in the locations you specify. If rain is in the forecast, the script will send an email alert.

## Features

### 1. Data Caching

Rain Alert includes a powerful data caching mechanism. This is facilitated by the `DataParser` and `JsonHandler` classes. Here's how it works:

- **DataParser**: This class handles fetching data from the OpenWeatherMap API. It also includes a caching mechanism to prevent excessive API calls. The data fetched from the API is stored locally with a validity period, ensuring that you stay within rate limits while reducing redundant calls.

- **JsonHandler**: The `JsonHandler` class is responsible for handling the storage of cached data. It can update the cache with new data and remove old data. This ensures that the script runs efficiently without overwhelming the API.

### 2. Customizable Data Validity

The `DataParser` class allows you to set the validity period for cached data. You can specify how long the data remains valid before a new API call is made. This feature helps you balance the need for accurate information and staying within the API rate limit threshold.

## Prerequisites

Before you can run Rain Alert locally, you need to have the following prerequisites:

- Python 3.x installed on your machine.
- Access to an OpenWeatherMap API key. You can obtain one by signing up at [OpenWeatherMap](https://openweathermap.org/api).
- Email credentials for sending alerts. Make sure you have an email ID and key (get from Gmail, which is under 2-factor authentication) ready. Please note that the above key is the developer key to send mail via software and is not the same as your email password.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/Rain-Alert.git
   cd Rain-Alert


2. Install the required Python packages. This project relies on `pandas` for data handling. If you don't have it installed, run:

   ```bash
   pip install pandas
   ```

3. Set your OpenWeatherMap API key and email credentials as environment variables:

   ```bash
   export OPEN_WEATHER_API_KEY=your_openweather_api_key
   export SENDER_EMAIL_ID=your_email@example.com
   export SENDER_EMAIL_KEY=your_email_password
   ```

## Usage

To start receiving rain alerts, follow these steps:

1. Prepare a CSV file named `rain_alert_receiver.csv` with the following format:

   ```csv
   email_id, lat, lng
   recipient1@example.com, 12.34, 56.78
   recipient2@example.com, 23.45, 67.89
   ```

   This file should contain the email addresses and corresponding latitude and longitude coordinates of the locations you want to monitor.

2. Run the Rain Alert script:

   ```bash
   python rain_alert.py
   ```

   The script will read the CSV file, check the weather for each location, and send email alerts if rain is in the forecast.

## Contributing

We welcome contributions to improve Rain Alert. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with your feature or bug fix.
3. Make your changes and ensure the code is well-documented.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need assistance, you can contact the project maintainer at manish.joshi.eng@gmail.com.

```
