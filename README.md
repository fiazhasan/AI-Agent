# Holistic Health Insights Dashboard

## Overview
The **Holistic Health Insights Dashboard** is a Streamlit-based web application designed to provide personalized health insights based on various inputs, including fitness tracking, sleep analysis, and journaling sentiment. This application leverages specialized AI agents to process data from wearable devices, analyze sleep patterns, and evaluate the sentiment of journal entries.

## Features
- **Fitness Tracking**: Analyzes steps and provides suggestions based on user activity data.
- **Sleep Analysis**: Evaluates sleep hours and disturbances, offering recommendations for improving sleep quality.
- **Journaling Sentiment Analysis**: Analyzes the sentiment of journal entries, categorizing them as positive, negative, or neutral, and provides an overall sentiment summary.
- **Wearable Data Integration**: Displays raw and normalized health data from a mock data source for deeper insights.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- **Python 3.7+**
- **Streamlit**: For creating the web application.
- **TextBlob**: For sentiment analysis in journaling.
- **JSON**: For parsing and handling input data.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/holistic-health-dashboard.git
   cd holistic-health-dashboard
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open the application in your browser at `http://localhost:8501`.

### Inputs
The application expects user inputs in JSON format for:
- **Fitness Data**: Activity data, including steps, calories, and active minutes.
- **Sleep Data**: Sleep hours and disturbances.
- **Journal Entries**: Text entries for sentiment analysis.

Example JSON format for each input:
- **Fitness Data**:
   ```json
   [{"date": "2024-11-22", "steps": 8500, "calories": 300, "active_minutes": 45}]
   ```
- **Sleep Data**:
   ```json
   [{"date": "2024-11-22", "sleep_hours": 6.5, "disturbances": 2}]
   ```
- **Journal Entries**:
   ```json
   [{"date": "2024-11-22", "entry": "I feel really anxious about the upcoming presentation."}]
   ```

### Using the Dashboard
1. Enter the relevant JSON data in the sidebar for **Fitness**, **Sleep**, and **Journal Entries**.
2. Click **Generate Insights** to view the results.
3. Explore the insights across five tabs:
   - **Fitness**: Metrics like average steps and total steps, with a health suggestion.
   - **Sleep**: Average sleep hours, total disturbances, and sleep improvement suggestions.
   - **Journaling**: Sentiment analysis of journal entries with a summary.
   - **Aggregated Insights**: (Coming soon) Insights based on combined analysis of the data.
   - **Wearable Data**: View raw and normalized health data.

## AI Agents and Their Logic

### Fitness Tracking Agent
- **Purpose**: Analyzes physical activity data (steps) to evaluate the user's fitness level.
- **Logic**:
  - It calculates the total and average steps over the input period.
  - Provides a suggestion to improve physical activity if average steps fall below 10,000.
#### Output Example:
![Fitness Agent Output](images/fitness_output.png)

### Sleep Analysis Agent
- **Purpose**: Analyzes sleep data to assess the user's sleep quality.
- **Logic**:
  - It calculates the total sleep hours and the number of disturbances.
  - If the average sleep is below 7 hours, it recommends getting more sleep.

### Journaling Sentiment Analysis Agent
- **Purpose**: Analyzes the sentiment of journal entries to gauge the user's emotional state.
- **Logic**:
  - Each journal entry is evaluated for sentiment polarity using **TextBlob**.
  - The sentiment is categorized into positive, negative, or neutral.
  - The summary provides the percentage of positive, negative, and neutral entries.

### Data Integration Class
- **Purpose**: Loads and normalizes wearable data (e.g., steps, heart rate, sleep) from a mock data source for visualization.
- **Logic**:
  - It provides mock data (user metrics) for testing purposes.
  - The data is normalized to ensure consistency in the application.




## Folder Structure
```
holistic-health-dashboard/
│
├── app.py                   # Main Streamlit app file
├── requirements.txt         # List of dependencies
└── README.md                # Documentation for the project
```

## Dependencies
The project requires the following Python packages:
- **streamlit**: `pip install streamlit`
- **textblob**: `pip install textblob`
- **json**: (Included in Python standard library)

### Sample `requirements.txt`:
```
streamlit==1.10.0
textblob==0.15.3
```
---

This README should provide a clear guide for setting up and using your project.
