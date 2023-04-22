import streamlit as st
import plotly.express as px
import pandas as pd
from backend import fetch_data

# Add title, textbox, slider, dropdown list, and subheader.
st.title("Weather Forcast for the Next Days")
st.write("")
place = st.text_input("Location (type in the name of the city):")
st.write("")
days = st.slider("How many days of forecast do you want for that location?", min_value=1, max_value=5,
                 help="Choose how many days of forecast you want to display.")
st.write("")
option = st.selectbox("Select data to view:", ("Temperature", "Sky"))
st.write("")
st.subheader(f"{option} for the next {days} days in {place}")
st.write("")


if place:
    try:
        # Pass the number of days and Temperature or Sky as arguments.
        filtered_data = fetch_data(place, days)
        # print(filtered_data)

        if option == "Temperature":
            temperatures = [item["main"]["temp"] / 10 - 10 for item in filtered_data]
            date_time = [item["dt_txt"] for item in filtered_data]

            # Create the temperature plot.
            figure = px.line(x=date_time, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            # figure.update_layout(yaxis=dict(tickmode='linear', tick0=0, dtick=10))
            figure.update_yaxes(range=[0, 2])
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            weather = [item["weather"][0]["main"] for item in filtered_data]
            img = [images[w] for w in weather]
            date_time = [item["dt_txt"] for item in filtered_data]
            st.image(img, width=115, caption=date_time)

    except KeyError:
        st.write(f'Sorry, the name of the city "{place}" does not exist.')

