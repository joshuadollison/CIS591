
# Your Code Starts Here

# make modifications to the code above to show a web page with the title "CIS 591 Web App Assignment"
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Title and description
st.title("CIS 591 Web App Assignment 5")
st.write("This web page is for the last assignment.")

# Example visualization: Sample Data provided in the code
st.write("Visualization Example 1:")

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 22]

# Create the Line Chart
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers', name='Line'))

# Customize the layout
fig.update_layout(title='Example',
                  xaxis_title='X Axis',
                  yaxis_title='Y Axis')

st.plotly_chart(fig)

# Example visualization: Load data from the file

# Load dataset directly
data_file = "Assignment 2_PastYearSales.csv"  # Specify the path to your data file
data = pd.read_csv(data_file, encoding='latin-1')
print(data.head())

dmonth = data['Month']
dsales = data['Sales (# of units)']

# Display the dataset
st.write("Dataset Preview:")
st.dataframe(data.head())

st.write("Monthly Sales in the Past Year:")
# Create the Line Chart
fig = go.Figure(data=go.Scatter(x= dmonth, y= dsales, mode='lines+markers', name='Line'))
# Customize the layout
fig.update_layout(title='Simple Line Chart',
                  xaxis_title='Month',
                  yaxis_title='Number of units sold')

st.plotly_chart(fig)


# make modifications to the code above to show a pie chart
# Create the Pie Chart
# Create the Pie Chart
fig = go.Figure(data=[
    go.Pie(
        labels=dmonth, 
        values=dsales,
        textinfo='percent+label',
        hole=0.4,  # donut style
        name="Pie"
)])

# Customize the layout
fig.update_layout(title='Simple Pie Chart')

st.plotly_chart(fig)

# Your Code Ends Here
