import streamlit as st

st.set_page_config(
    page_title="Music Dashboard",
    page_icon="🎵"
)

st.title("Welcome to the Music Dashboard! 🎵")

st.write("""
This website explores music listening habits using
different charts and visualizations.

### About This Project

This project was created for CS 1301 Web Development Lab 2.

The dashboard uses JSON data to display music
listening trends across different genres.

### How to Use the Website

1. Open the Visuals page from the sidebar.
2. View the pie chart showing total plays by genre.
3. Select a music genre to explore monthly trends.
4. Watch the line graph update based on your selection.

Enjoy exploring the data!
""")
