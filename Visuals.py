
import streamlit as st
import pandas as pd
import altair as alt
import json

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Music Visualizations",
    page_icon="🎵"
)

st.title("Music Listening Dashboard 🎵")
st.write("Explore music listening habits through different charts.")

# PART 1: GRAPHS FROM data.json

# Read data from JSON file
with open("data.json", "r") as file:
    data = json.load(file)

months = data["months"]
genres = data["genres"]

# ---------------------------------
# GRAPH 1: STATIC PIE CHART
# ---------------------------------

st.header("1. Total Music Plays by Genre")

# Calculate total plays for each genre
genre_totals = []

for genre in genres:
    total = sum(genres[genre])
    genre_totals.append({
        "Genre": genre,
        "Plays": total
    })

# Convert the information into a DataFrame
pie_data = pd.DataFrame(genre_totals)

# Create pie chart using Altair
pie_chart = alt.Chart(pie_data).mark_arc().encode(
    theta="Plays:Q",
    color="Genre:N",
    tooltip=["Genre", "Plays"]
).properties(
    title="Total Plays by Music Genre"
)

st.altair_chart(pie_chart)

st.write("This pie chart shows the total number of plays for each music genre.")

# ---------------------------------
# GRAPH 2: DYNAMIC LINE CHART
# ---------------------------------

st.header("2. Monthly Music Listening Trends")

# Create a list of genres
genre_list = list(genres.keys())

# Set up session state
if "selected_genre" not in st.session_state:
    st.session_state["selected_genre"] = genre_list[0]

# Let the user select a genre
st.selectbox(
    "Choose a music genre:",
    genre_list,
    key="selected_genre"
)

# Get the selected genre from session state
selected_genre = st.session_state["selected_genre"]

# Get the listening data for that genre
monthly_plays = genres[selected_genre]

# Create a DataFrame for the line chart
line_data = pd.DataFrame({
    "Month": months,
    "Plays": monthly_plays
})

# Display dynamic chart
st.subheader("Monthly Plays for " + selected_genre)

st.line_chart(
    line_data,
    x="Month",
    y="Plays"
)

st.write("Select a different genre above to see how the graph changes.")

# PART 2: GRAPHS FROM data.csv
# This section will be completed in Part 2.
