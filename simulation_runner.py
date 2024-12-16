import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Create an array of years and health data
years = np.arange(0, 21)  # 0 to 20 years
health_data = 100 - (years * 2)  # Decreasing health over time

# Create an animated line plot
fig = go.Figure(
    go.Scatter(
        x=years,
        y=health_data,
        mode='lines+markers',
        marker=dict(color='red'),
        line=dict(color='blue'),
    )
)

# Set up the animation frame (display health change over time)
fig.update_layout(
    title='Health Over Time',
    xaxis_title='Year',
    yaxis_title='Health (%)',
    updatemenus=[dict(
        type="buttons",
        showactive=False,
        buttons=[dict(
            label="Play",
            method="animate",
            args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)]
        )]
    )],
    sliders=[dict(
        steps=[dict(
            args=[[f'frame_{i}'], dict(mode='immediate', frame=dict(duration=300, redraw=True))],
            label=str(year),
            method='animate'
        ) for i, year in enumerate(years)]
    )]
)

# Display the figure in Streamlit
st.plotly_chart(fig)
