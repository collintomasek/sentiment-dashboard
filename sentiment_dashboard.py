import streamlit as st
import pandas as pd
from textblob import TextBlob
import plotly.express as px

# --- 1. SET UP THE PAGE CONFIGURATION ---
st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

st.title("📊 Customer Review Sentiment Dashboard")
st.markdown("Upload a CSV file of reviews to analyze the overall sentiment.")

# --- 2. SIDEBAR FOR FILE UPLOAD ---
with st.sidebar:
    st.header("Upload Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    st.markdown("""
    **Example CSV format:**
    | reviewID | review_text |
    |----------|-------------|
    | 1        | Great app!  |
    """)

# --- 3. MAIN APP LOGIC ---
if uploaded_file is not None:
    # Read the CSV
    try:
        df = pd.read_csv(uploaded_file)
        
        # Check if the 'review_text' column exists
        if 'review_text' in df.columns:
            
            # Show raw data (preview)
            st.subheader("Raw Data Preview")
            st.dataframe(df.head())

            # --- SENTIMENT ANALYSIS ---
            st.write("⏳ Analyzing sentiment...")
            
            # Define a function to get sentiment score
            def get_sentiment(text):
                blob = TextBlob(str(text))
                return blob.sentiment.polarity
            
            # Apply the function to the dataset
            df['sentiment_score'] = df['review_text'].apply(get_sentiment)

            # Categorize the sentiment based on the score
            def categorize_sentiment(score):
                if score > 0.1:
                    return 'Positive'
                elif score < -0.1:
                    return 'Negative'
                else:
                    return 'Neutral'
            
            df['sentiment_category'] = df['sentiment_score'].apply(categorize_sentiment)

            # --- VISUALIZATION ---
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Sentiment Distribution")
                sentiment_counts = df['sentiment_category'].value_counts().reset_index()
                sentiment_counts.columns = ['Category', 'Count']
                
                # Create a Bar Chart using Plotly
                fig = px.bar(sentiment_counts, x='Category', y='Count', 
                             color='Category', 
                             color_discrete_map={'Positive':'green', 'Negative':'red', 'Neutral':'gray'})
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.subheader("Key Metrics")
                total_reviews = len(df)
                positive_reviews = len(df[df['sentiment_category'] == 'Positive'])
                negative_reviews = len(df[df['sentiment_category'] == 'Negative'])
                
                st.metric("Total Reviews", total_reviews)
                st.metric("Positive Reviews", f"{positive_reviews} ({(positive_reviews/total_reviews)*100:.1f}%)")
                st.metric("Negative Reviews", f"{negative_reviews} ({(negative_reviews/total_reviews)*100:.1f}%)")

            # Show the analyzed dataframe
            st.subheader("Analyzed Data")
            st.dataframe(df)
            
            # Download button for the results
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Analyzed CSV", data=csv, file_name="sentiment_results.csv", mime="text/csv")

        else:
            st.error("CSV must contain a column named 'review_text'")
            
    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Awaiting CSV upload. Please upload a file to begin.")