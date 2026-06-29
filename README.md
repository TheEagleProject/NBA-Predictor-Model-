# NBA Game Prediction Model

A machine learning model that predicts NBA game outcomes using historical game data, achieving 63% accuracy.

## How It Works

- Cleans and sorts historical NBA game data by date
- Engineers 10 game rolling averages for each team to capture recent form
- Merges opponent statistics to provide matchup context
- Uses Sequential Feature Selection to identify the 30 most predictive features
- Trains a Ridge Classifier using a season-by-season backtesting pipeline

## Tech Stack

- Python
- pandas
- scikit-learn

## Results

- 63% prediction accuracy evaluated across multiple NBA seasons
- 30 features selected from raw game statistics via Sequential Feature Selection

## How To Run

1. Clone the repo
2. Install dependencies: `pip install pandas scikit-learn`
3. Add your `nba_games.csv` to a `/data` folder
4. Run `python model.py`