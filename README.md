# Binance Data Collection and Visualization

## Data Collection from Binance API and Flask UI (with ploty)

This script collects data from the Binance API for a given interval (e.g., 1d, 4h, 1h) and symbol (e.g., BTCUSDT, ETHUSDT). The data is saved in CSV format and can be used for further analysis or visualization.

## What was done ?
In this project, the following tasks were accomplished:

#### Data Collection and Storage
Developed a script to collect data from the Binance API for a specified interval and symbol.
Saved the collected data in CSV format for easy storage and analysis.
Implemented a relational database to store the data for long-term use.
#### Data Collection Automation
Integrated automatic migrations generation and tracking system using Flask-Migrate.
Implemented a Dockerfile for easy deployment and management of the database container.
#### Cron Jobs
Created cron jobs using the BackgroundScheduler from apscheduler library.
Scheduled the data collection script to run at regular intervals (e.g., every 1D, 4H, 1H).
#### Flask UI
Developed a Flask-based web application to display candlestick data and market cap information.
Utilized Plotly as a module for dynamic and interactive visualization of candlestick data.
Implemented a pie chart to represent the market capitalization of the top 10 symbols.
#### Docker Integration
Added a Dockerfile to containerize the Flask application and simplify deployment.
Enabled easy setup and deployment of the entire application stack using Docker.
#### Automatic Migrations
Integrated Flask-Migrate to handle automatic migrations for database schema changes.
Simplified the process of managing and applying database migrations.

### How to run and use

To run the data collection script:

1. Clone this repository to your local machine.
```commandline
git clone https://github.com/smikayel/assessment.git
```
2. activate virtual environment 
```commandline
python -m venv venv
```
3. activate virtual environment, for this type
```commandline
.\venv\Scripts\activate
```
4. Install the required dependencies by running 
```commandline
pip install -r requirements.txt
```
5. copy the `.env.example` file and rename to `.env`
6. run the docker file with docker command
```commandline
docker compose up
```
7. Open new terminal in project directory and make migrations with command
```commandline
flask db upgrade
```
(be sure that the venv activated... (it's new terminal you need to reactivate venv))
4. Run the server with crons with command `python app.py`.

You can customize the deployment frequency by scheduling the script to run at regular intervals using tools like cron or task scheduler.

### Data Storage

The collected data is saved in CSV format for easy storage and analysis. Each row in the CSV file represents a data point with relevant information such as timestamp, open, high, low, close prices, and volume.

## Task 2: Flask UI with Candlestick Chart and Pie Chart

This Flask-based web application displays candlestick data and market cap information using Plotly for dynamic visualization.

### Setup and Usage

To run the Flask UI:

1. Make sure you have Python installed on your machine.
2. Clone this repository and navigate to the project directory.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Set the necessary configurations, such as the database connection and market symbols, in the Flask app.
5. Run the Flask app using `python app.py`.
6. Access the UI by opening `http://localhost:5000` in your web browser.

### Candlestick Chart

The candlestick chart displays the open, high, low, and close prices for a selected symbol and interval. It allows you to visualize the price movements over time.

### Market Cap Pie Chart

The pie chart represents the market capitalization of the top 10 symbols. It provides a visual breakdown of the relative market size of each symbol.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Create a pull request to merge your changes into the main repository.

Feel free to open issues for any bugs, feature requests, or questions you may have.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.