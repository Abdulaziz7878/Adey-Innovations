import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

from app_instance import app  # Import the app instance
from app import app

# Load and preprocess data
df = pd.read_csv('C:/Users/Abdulaziz/Desktop/10 Academy/Adey Innovations/Dashboard/weather_data.csv')

# Populate dropdown options on initial load
@app.callback(
    [
        Output('year-dropdown', 'options'),
        Output('year-dropdown', 'value'),
        Output('month-dropdown', 'options'),
        Output('month-dropdown', 'value'),
    ],
    [Input('year-dropdown', 'options')]  # Trigger once on load
)
def set_dropdown_options(_):
    years = sorted(df['Year'].unique())
    months = sorted(df['Month'].unique(), key=lambda x: pd.to_datetime(x, format='%B').month)
    year_options = [{'label': year, 'value': year} for year in years]
    month_options = [{'label': month, 'value': month} for month in months]
    return year_options, years[0], month_options, months[0]

# Update summary statistics
@app.callback(
    [
        Output('average-temperature', 'children'),
        Output('average-humidity', 'children'),
        Output('average-windspeed', 'children'),
    ],
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_summary(selected_year, selected_month):
    filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
    avg_temp = filtered_df['Temperature'].mean()
    avg_humidity = filtered_df['Humidity'].mean()
    avg_windspeed = filtered_df['WindSpeed'].mean()
    return (
        f"{avg_temp:.2f}",
        f"{avg_humidity:.2f}",
        f"{avg_windspeed:.2f}"
    )

# Update Temperature Over Time Graph
@app.callback(
    Output('temperature-over-time', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_temperature_chart(selected_year, selected_month):
    filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
    fig = px.line(filtered_df, x='Date', y='Temperature',
                  title=f'Temperature Over Time in {selected_month} {selected_year}')
    fig.update_layout(xaxis_title='Date', yaxis_title='Temperature (°C)')
    return fig

# Update Humidity Over Time Graph
@app.callback(
    Output('humidity-over-time', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_humidity_chart(selected_year, selected_month):
    filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
    fig = px.line(filtered_df, x='Date', y='Humidity',
                  title=f'Humidity Over Time in {selected_month} {selected_year}')
    fig.update_layout(xaxis_title='Date', yaxis_title='Humidity (%)')
    return fig

# Update Weather Condition Pie Chart
@app.callback(
    Output('weather-condition-pie', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_weather_condition_pie(selected_year, selected_month):
    filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
    condition_counts = filtered_df['Summary'].value_counts().reset_index()
    condition_counts.columns = ['Summary', 'Count']
    fig = px.pie(condition_counts, names='Summary', values='Count',
                 title=f'Weather Conditions in {selected_month} {selected_year}')
    return fig

# Update Wind Speed Distribution
@app.callback(
    Output('windspeed-distribution', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_windspeed_distribution(selected_year, selected_month):
    filtered_df = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]
    fig = px.histogram(filtered_df, x='WindSpeed', nbins=20,
                       title=f'Wind Speed Distribution in {selected_month} {selected_year}')
    fig.update_layout(xaxis_title='Wind Speed (km/h)', yaxis_title='Frequency')
    return fig