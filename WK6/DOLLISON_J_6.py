
import calendar
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.stats import pearsonr
import pandas as pd

# Title and description
st.title("CIS 591: Individual Assignment - Web presentation")
st.header("Mini Business Case Study - Sales Analytics for EcoTrek Solutions.")
st.write("I am a new hire at EcoTrek Solutions, a U.S.-based company that specializes in eco-friendly travel accessories. \
As a business data analyst, my role involves analyzing sales trends and providing insights to help shape the company's \
marketing and production strategies.")
st.write("Satisfied with the analysis results, the manager asks me to put the visualizations on the web.")
st.write("Find my work below...")

# Load month names from calendar - shows for
months = []
for month_num in range(1, 13):
    months.append(calendar.month_name[month_num])

# Temperatures (°F)
temperature = [40, 45, 55, 65, 75, 85, 90, 88, 86, 80, 70, 60]

# GreenTote sales
green_tote = [
    87500, 100625, 115725, 132075, 148875, 164500,
    172725, 185800, 180900, 170000, 165000, 160000
]

# Create DataFrame 
df = pd.DataFrame({
    'month': months,
    'temp': temperature,
    'sales': green_tote
})

#display(df)

# Write our subheader for this section
st.subheader("GreenTote Unit Sales vs Temperature:")

# Fit the regression line
slope, intercept = np.polyfit(df['temp'], df['sales'], 1)
x_line = np.linspace(df['temp'].min(), df['temp'].max(), 100)
y_line = slope * x_line + intercept

# Compute Pearson correlation
r_value, p_value = pearsonr(df['temp'], df['sales'])

# Plot a scatter plot in ASU blackout colors!
fig = go.Figure()

# Scatter plot points
fig.add_trace(go.Scatter(
    x=df['temp'],
    y=df['sales'],
    mode='markers+text',
    text=df['month'],
    textposition='top center',
    name='Monthly Data',
    marker=dict(
        size=10,
        color='#8C1D40',  # ASU Maroon
        line=dict(width=2, color='#FFC627')  # ASU Gold border
    )
))

# Add the calculated regression trend line
fig.add_trace(go.Scatter(
    x=x_line,
    y=y_line,
    mode='lines',
    name='Trendline (Linear Regression)',
    line=dict(color='#FFC627', width=3, dash='dash')  # ASU Gold, dashed
))

# show pearson results
fig.add_annotation(
    xref='paper', yref='paper',
    x=0.01, y=0.95,
    text=f"Pearson r = {r_value:.3f}, p = {p_value:.6f}",
    showarrow=False,
    font=dict(size=14, color='#FFC627'),
    bgcolor="#8C1D40",
    bordercolor="#FFC627",
    borderwidth=1,
    borderpad=4
)

# add details and render
fig.update_layout(
    title='Green Tote Sales vs Temperature (with Trendline & Pearson Correlation)',
    xaxis_title='Temperature (°F)',
    yaxis_title='Green Tote Sales',
    height=600,
    paper_bgcolor='#191919',
    plot_bgcolor='#2E2E2E',
    font=dict(family='Arial', size=14, color='#FFC627'),
    title_font=dict(size=22, color='#8C1D40'),
    xaxis=dict(
        color='#FFC627',
        gridcolor='#444',
        zerolinecolor='#8C1D40',
    ),
    yaxis=dict(
        color='#FFC627',
        gridcolor='#444',
        zerolinecolor='#8C1D40',
    ),
    hovermode='closest'
)

#fig.show()
st.plotly_chart(fig)
df = pd.read_csv('DOLLISON_JOSHUA_sentiment.csv')
#df

# Write our subheader for this section
st.subheader("Categorical Comparison:")

sentiment_counts = df['sentiment'].value_counts().reindex(['positive', 'neutral', 'negative'], fill_value=0)
#display(sentiment_counts)

# Let's show the counts as bars
#   Since there are only 3 categories, we'll provide some custom indicator colors
bar = go.Bar(
    x=sentiment_counts.index,
    y=sentiment_counts.values,
    marker_color=['green', 'gray', 'red'],
    text=sentiment_counts.values,
    name="Counts"
)

# We'll show the percentages as a pie chart
pie = go.Pie(
    labels=sentiment_counts.index,
    values=sentiment_counts.values,
    marker=dict(colors=['green', 'gray', 'red']),
    textinfo='percent+label',
    hole=0.4,  # donut style
    name="Percents"
)

# Combine into subplots
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, specs=[[{'type':'xy'}, {'type':'domain'}]],
                    subplot_titles=(f'Sentiment Counts - {len(df)} Total Reviews', 'Sentiment Percentages')) # i include a total count here

fig.add_trace(bar, row=1, col=1)
fig.add_trace(pie, row=1, col=2)

fig.update_layout(
    title_text='Customer Sentiment - Categorical Comparison',
    plot_bgcolor='white',
    paper_bgcolor='white',
    showlegend=False
)

#fig.show()
st.plotly_chart(fig)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Write our subheader for this section
st.subheader("Sentiment - Review Deep Dive:")

# i created a custom function that i can call multiple times
def generateWordCloud(df, sentiment) :

    # pull the right text for the sentiment - concatenate the entire category into one big text string
    text = df[df['sentiment'] == sentiment]['review'].str.cat(sep=' ')
    
    # asu colors
    asu_cmap = LinearSegmentedColormap.from_list("asu_colors", ['#8C1D40', '#FFC627'])
    
    # Generate the Word Cloud
    wordcloud = WordCloud(width=1200, height=1200, background_color='white',
                         colormap=asu_cmap, contour_color='#8C1D40',
                            contour_width=2).generate(text)


    # Visualize the Word Cloud using Matplotlib
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title(
        f'Customer Reviews - {str.upper(sentiment)}',
        fontsize=20, fontweight='bold', loc='left'
    )

    st.pyplot(fig)

# loop through each unique sentiment in the df
for sentiment in df['sentiment'].unique() :
    generateWordCloud(df, sentiment)
