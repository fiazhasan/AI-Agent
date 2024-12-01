import streamlit as st
from textblob import TextBlob
import json
from typing import List, Dict

# Fitness Tracking Agent
class FitnessTrackingAgent:
    def __init__(self, activity_data=None):
        self.activity_data = activity_data if activity_data else []

    def analyze_activity(self):
        total_steps = sum(entry.get("steps", 0) for entry in self.activity_data)
        avg_steps = total_steps / len(self.activity_data) if self.activity_data else 0

        suggestion = "Great job! Maintain your activity levels."
        if avg_steps < 10000:
            suggestion = "Try to increase your weekly activity by 10% for better health."

        return {
            "average_steps": avg_steps,
            "total_steps": total_steps,
            "suggestion": suggestion
        }


# Sleep Analysis Agent
class SleepAnalysisAgent:
    def __init__(self, sleep_data=None):
        self.sleep_data = sleep_data if sleep_data else []

    def analyze_sleep(self):
        total_sleep = sum(entry.get("sleep_hours", 0) for entry in self.sleep_data)
        avg_sleep = total_sleep / len(self.sleep_data) if self.sleep_data else 0
        disturbances = sum(entry.get("disturbances", 0) for entry in self.sleep_data)

        suggestion = "Your sleep is consistent. Keep it up!"
        if avg_sleep < 7:
            suggestion = "Try to get at least 7 hours of sleep each night."

        return {
            "average_sleep_hours": avg_sleep,
            "total_disturbances": disturbances,
            "suggestion": suggestion
        }


# Journaling Sentiment Analysis Agent
class JournalingSentimentAgent:
    def analyze_sentiment(self, journal_entries):
        sentiments = []
        positive_count = 0
        negative_count = 0

        for entry in journal_entries:
            text = entry["entry"]
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity

            if polarity > 0:
                sentiments.append({"date": entry["date"], "sentiment": "positive", "polarity": polarity})
                positive_count += 1
            elif polarity < 0:
                sentiments.append({"date": entry["date"], "sentiment": "negative", "polarity": polarity})
                negative_count += 1
            else:
                sentiments.append({"date": entry["date"], "sentiment": "neutral", "polarity": polarity})

        summary = {
            "positive_percentage": (positive_count / len(journal_entries)) * 100,
            "negative_percentage": (negative_count / len(journal_entries)) * 100,
            "neutral_percentage": 100 - ((positive_count + negative_count) / len(journal_entries)) * 100
        }

        return {"sentiments": sentiments, "summary": summary}


# Data Integration Class
class DataIntegration:
    def __init__(self):
        """
        Initialize the data integration layer with embedded mock data.
        """
        self.data_source = {
            "user_id": "12345",
            "metrics": [
                {
                    "date": "2024-11-22",
                    "steps": 8500,
                    "heart_rate": 75,
                    "sleep_hours": 6.5,
                    "hrv": 45
                },
                {
                    "date": "2024-11-21",
                    "steps": 9500,
                    "heart_rate": 72,
                    "sleep_hours": 7.2,
                    "hrv": 50
                }
            ]
        }

    def load_data(self) -> List[Dict]:
        """
        Load and return the mock data.
        :return: List of dictionaries containing raw health metrics.
        """
        try:
            return self.data_source["metrics"]
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return []

    def normalize_data(self, data: List[Dict]) -> List[Dict]:
        """
        Normalize the data for consistent processing.
        :param data: Raw data list.
        :return: Normalized data list.
        """
        normalized = []
        for entry in data:
            normalized.append({
                "date": entry["date"],
                "steps": entry.get("steps", 0),
                "heart_rate": entry.get("heart_rate", None),
                "sleep_hours": round(entry.get("sleep_hours", 0), 2),
                "hrv": entry.get("hrv", None)
            })
        return normalized


# Streamlit Application
def main():
    st.title("Holistic Health Insights Dashboard")

    st.sidebar.title("Input Data")
    
    # User Input
    st.write("This dashboard provides insights on your fitness, sleep, journaling sentiment, and wearable data.")

    # Fitness Input
    fitness_input = st.sidebar.text_area("Enter JSON Activity Data", '[{"date": "2024-11-22", "steps": 8500, "calories": 300, "active_minutes": 45}]')

    # Sleep Input
    sleep_input = st.sidebar.text_area("Enter JSON Sleep Data", '[{"date": "2024-11-22", "sleep_hours": 6.5, "disturbances": 2}]')

    # Journal Input
    journal_input = st.sidebar.text_area("Enter JSON Journal Entries", '[{"date": "2024-11-22", "entry": "I feel really anxious about the upcoming presentation."}]')

    if st.sidebar.button("Generate Insights"):
        try:
            # Parse inputs
            fitness_data = json.loads(fitness_input)
            sleep_data = json.loads(sleep_input)
            journal_entries = json.loads(journal_input)

            # Process data with agents
            fitness_agent = FitnessTrackingAgent(activity_data=fitness_data)
            fitness_insights = fitness_agent.analyze_activity()

            sleep_agent = SleepAnalysisAgent(sleep_data=sleep_data)
            sleep_insights = sleep_agent.analyze_sleep()

            journal_agent = JournalingSentimentAgent()
            journal_insights = journal_agent.analyze_sentiment(journal_entries)

            # Data Integration
            data_integration = DataIntegration()
            raw_data = data_integration.load_data()
            normalized_data = data_integration.normalize_data(raw_data)

            # Display results in tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏃‍♂️ Fitness", "💤 Sleep", "📝 Journaling", "📊 Aggregated Insights", "⌚ Wearable Data"])

            with tab1:
                st.header("Fitness Insights")
                st.metric("Average Steps", fitness_insights["average_steps"])
                st.metric("Total Steps", fitness_insights["total_steps"])
                st.write(f"Suggestion: {fitness_insights['suggestion']}")

            with tab2:
                st.header("Sleep Insights")
                st.metric("Average Sleep Hours", sleep_insights["average_sleep_hours"])
                st.metric("Total Disturbances", sleep_insights["total_disturbances"])
                st.write(f"Suggestion: {sleep_insights['suggestion']}")

            with tab3:
                st.header("Journaling Insights")
                st.json(journal_insights["sentiments"])
                st.write(f"Summary: {journal_insights['summary']}")

            with tab4:
                st.header("Aggregated Insights")
                st.write("Coming soon: Advanced insights based on combined analysis.")

            with tab5:
                st.header("Wearable Data")
                st.subheader("Raw Data")
                st.json(raw_data)
                st.subheader("Normalized Data")
                st.json(normalized_data)

        except json.JSONDecodeError:
            st.error("Invalid JSON format in one of the inputs. Please check and try again.")


if __name__ == "__main__":
    main()
