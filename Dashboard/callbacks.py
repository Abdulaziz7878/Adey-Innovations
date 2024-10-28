import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

from app_instance import app  # Import the app instance
from app import app

# Load and preprocess data
df = pd.read_csv('C:/Users/Abdulaziz/Desktop/10 Academy/Adey Innovations/Data/preprocessed.csv')

# Populate dropdown options on initial load
@app.callback(
    [
        Output('age-dropdown', 'options'),
        Output('age-dropdown', 'value'),
        Output('class-dropdown', 'options'),
        Output('class-dropdown', 'value'),
    ],
    [Input('age-dropdown', 'options')]  # Trigger once on load
)
def set_dropdown_options(_):
    age = sorted(df['age'].unique())
    clas = sorted(df['class'].unique(), key=lambda x: pd.to_datetime(x, format='%B').clas)
    age_options = [{'label': age, 'value': year} for year in age]
    class_options = [{'label': clas, 'value': month} for month in clas]
    return age_options, age[0], class_options, clas[0]

# Update summary statistics
@app.callback(
    [
        Output('average-age', 'children'),
        Output('average-class', 'children'),
    ],
    [Input('age-dropdown', 'value'),
     Input('class-dropdown', 'value')]
)
def update_summary(selected_age, selected_class):
    filtered_df = df[(df['age'] == selected_age) & (df['class'] == selected_class)]
    avg_age = filtered_df['Temperature'].mean()
    avg_class = filtered_df['Humidity'].mean()
    return (
        f"{avg_age:.2f}",
        f"{avg_class:.2f}"
    )

# Update Temperature Over Time Graph
# @app.callback(
#     Output('temperature-over-time', 'figure'),
#     [Input('year-dropdown', 'value'),
#      Input('month-dropdown', 'value')]
# )
# def update_temperature_chart(selected_year, selected_month):
#     filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
#     fig = px.line(filtered_df, x='Date', y='Temperature',
#                   title=f'Temperature Over Time in {selected_month} {selected_year}')
#     fig.update_layout(xaxis_title='Date', yaxis_title='Temperature (°C)')
#     return fig

# # Update Humidity Over Time Graph
# @app.callback(
#     Output('humidity-over-time', 'figure'),
#     [Input('year-dropdown', 'value'),
#      Input('month-dropdown', 'value')]
# )
# def update_humidity_chart(selected_year, selected_month):
#     filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
#     fig = px.line(filtered_df, x='Date', y='Humidity',
#                   title=f'Humidity Over Time in {selected_month} {selected_year}')
#     fig.update_layout(xaxis_title='Date', yaxis_title='Humidity (%)')
#     return fig

# # Update Weather Condition Pie Chart
# @app.callback(
#     Output('weather-condition-pie', 'figure'),
#     [Input('year-dropdown', 'value'),
#      Input('month-dropdown', 'value')]
# )
# def update_weather_condition_pie(selected_year, selected_month):
#     filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
#     condition_counts = filtered_df['Summary'].value_counts().reset_index()
#     condition_counts.columns = ['Summary', 'Count']
#     fig = px.pie(condition_counts, names='Summary', values='Count',
#                  title=f'Weather Conditions in {selected_month} {selected_year}')
#     return fig

# # Update Wind Speed Distribution
# @app.callback(
#     Output('windspeed-distribution', 'figure'),
#     [Input('year-dropdown', 'value'),
#      Input('month-dropdown', 'value')]
# )
# def update_windspeed_distribution(selected_year, selected_month):
#     filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
#     fig = px.histogram(filtered_df, x='WindSpeed', nbins=20,
#                        title=f'Wind Speed Distribution in {selected_month} {selected_year}')
#     fig.update_layout(xaxis_title='Wind Speed (km/h)', yaxis_title='Frequency')
#     return fig