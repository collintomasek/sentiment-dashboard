# Customer Review Sentiment Dashboard

An interactive web application built with **Streamlit** that allows users to perform bulk sentiment analysis on customer reviews via CSV uploads.

## Features
* **CSV Data Upload**: Easily upload datasets containing customer feedback.
* **Automated Sentiment Analysis**: Uses the `TextBlob` library to calculate polarity scores and categorize reviews as Positive, Neutral, or Negative.
* **Real-time Visualizations**: View sentiment distribution through interactive `Plotly` bar charts.
* **Key Performance Metrics**: Instantly see total review counts and the percentage of positive vs. negative feedback.
* **Data Export**: Download the processed results as a new CSV file including the assigned sentiment scores and categories.

## Tech Stack
* **Frontend/App Framework**: [Streamlit](https://streamlit.io/)
* **Data Analysis**: Pandas
* **Natural Language Processing**: TextBlob
* **Visualizations**: Plotly Express

## Getting Started

### 1. Prerequisites
Ensure you have Python installed, then install the required dependencies:
```bash
pip install streamlit pandas textblob plotly
