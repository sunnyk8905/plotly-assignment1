# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n56FUkCvTaHsZxyyou5QTiLZycfHcyGS
"""

Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
scatter plot for age and fare columns in the titanic dataset.

import seaborn as sns
import plotly.express as px


titanic_data = sns.load_dataset("titanic")


scatter_plot = px.scatter(titanic_data, x='age', y='fare', title='Scatter Plot of Age vs Fare')


scatter_plot.show()

Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express.

import plotly.express as px


tips_data = px.data.tips()


box_plot = px.box(tips_data, x='day', y='total_bill', title='Box Plot of Total Bill by Day')


box_plot.show()

Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
column with the color parameter.

import plotly.express as px


tips_data = px.data.tips()


histogram = px.histogram(tips_data, x='sex', y='total_bill', color='day', pattern_shape='smoker',
                         title='Histogram of Total Bill by Sex')


histogram.show()

Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
the color parameter.

import plotly.express as px


iris_data = px.data.iris()


scatter_matrix = px.scatter_matrix(iris_data, dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
                                   color="species", title="Scatter Matrix Plot of Iris Dataset")


scatter_matrix.show()

Q5. What is Distplot? Using Plotly express, plot a distplot.

Distplot (Distribution Plot) is a visualization tool used to display the distribution of a univariate (single variable) dataset. It combines a histogram
and a kernel density estimate plot to provide insights into the underlying distribution of the data.

import plotly.express as px


data = [0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9]


distplot = px.histogram(data, nbins=10, marginal="rug", title="Distplot Example")


distplot.show()