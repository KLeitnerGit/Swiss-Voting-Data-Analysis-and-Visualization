#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[2]:


import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from base64 import b64encode
import io

# Read and preprocess data
df2 = pd.read_csv("SuissVotes_EN.csv")
df2 = df2.drop('Unnamed: 0', axis=1)
df2 = df2.drop(columns=['titel_kurz_e'])

# Analysis
most_supported = df2['volkja-proz'].quantile(0.95)
least_supported = df2['volkja-proz'].quantile(0.05)
filtered_df_most = df2[df2['volkja-proz'] >= most_supported].sort_values(by='volkja-proz', ascending=False)
filtered_df_least = df2[df2['volkja-proz'] <= least_supported].sort_values(by='volkja-proz')

# Generate ordered lists for most and least supported votes in HTML format
votes_list_most_html = "<ol style='margin-top: 20px;'>"
for index, row in filtered_df_most.iterrows():
    votes_list_most_html += f"<li><a href='{row['swissvoteslink']}' target='_blank'>{row['titel EN']} ({row['year']}): {row['volkja-proz']}% Yes votes</a></li>"
votes_list_most_html += "</ol>"

votes_list_least_html = "<ol style='margin-top: 20px;'>"
for index, row in filtered_df_least.iterrows():
    votes_list_least_html += f"<li><a href='{row['swissvoteslink']}' target='_blank'>{row['titel EN']} ({row['year']}): {row['volkja-proz']}% Yes votes</a></li>"
votes_list_least_html += "</ol>"

# Create an interactive scatter plot
fig = px.scatter(
    df2[(df2['volkja-proz'] >= most_supported) | (df2['volkja-proz'] <= least_supported)],
    x='year',
    y='volkja-proz',
    color='ja-lager',
    color_continuous_scale='BrBG',
    labels={'year': 'Year', 'ja-lager': 'Yes camp', 'titel EN': 'Title', 'volkja-proz':'Percentage of yes-votes'},
    title='Most and least supported Swiss votes over time (95%- and 5%-quantile)',
    hover_data=['titel EN', 'swissvoteslink'],
)

# Generate ordered lists for most and least supported votes
votes_list_most = html.Ol([
    html.Li(html.A(f"{row['titel EN']} ({row['year']}): {row['volkja-proz']}% Yes votes",
                   href=row['swissvoteslink'], target="_blank"))
    for index, row in filtered_df_most.iterrows()
], style={'margin-top': '20px'})

votes_list_least = html.Ol([
    html.Li(html.A(f"{row['titel EN']} ({row['year']}): {row['volkja-proz']}% Yes votes",
                   href=row['swissvoteslink'], target="_blank"))
    for index, row in filtered_df_least.iterrows()
], style={'margin-top': '20px'})

# Custom text to include
custom_text = """
<h1>Swiss Voting Data Analysis and Visualization (1848-2023)</h1>
<p>This interactive graph allows you to explore extreme Swiss voting results over the years. It emphasizes the 95th and 5th quantiles of voting data to highlight the most and least supported votes over time, in relationship to the sum of the voter shares of all parties that recommended their voters to vote "Yes" ("yes camp") represented by the color of the points.</p>

<p>One interesting extreme example is "Der Beschluss für den Einbau von Luftschutzräumen" ("The decision for the installation of air raid shelters") in 1952: Although the "yes camp" counts for around 60%, it received only 15.9% popular acceptance. Finally, the highest popular acceptance (94%) was received by the Constitutional basis for a one-time war tax in 1915, while the lowest popular acceptance (2.7%) was received by the Grain precaution initiative in 1929.</p>

<p>The data used for this purpose comes from the University of Bern. The Année Politique Suisse, based there, maintains a comprehensive dataset (Swissvotes) on all votes that have taken place since the founding of the modern federal state in 1848. <a href='https://swissvotes.ch/page/dataset' target='_blank'>Access the Swissvotes dataset here</a>.</p>
"""

# Dash app
app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1("Swiss Voting Data Analysis and Visualization (1848-2023)"),
    dcc.Markdown(custom_text),
    dcc.Graph(id="graph", figure=fig),
    html.H2("Most Supported Votes"),
    dcc.Markdown(votes_list_most_html),
    html.H2("Least Supported Votes"),
    dcc.Markdown(votes_list_least_html)
])

if __name__ == '__main__':
    app.run_server(debug=False)



# In[ ]:




