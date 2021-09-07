# https://docs.streamlit.io/en/stable/getting_started.html
# https://docs.streamlit.io/en/stable/api.html
# https://www.openstreetmap.org/#map=8/-13.553/-39.298
# https://www.opencyclemap.org/
# https://www.cyclosm.org/#map=12/-12.9654/-38.3862/cyclosm
# https://www.bicyclenetwork.com.au/tips-resources/maps-and-rides/bike-trail-maps/
# FAZER CONSULTAS NO OPEN STREET MAP
#  CRIAR DATAFRAME E PLOTAR NO NOSSO MAPA

import numpy as np
import pandas as pd
import streamlit as st
import time

st.title("My first app")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data

# option = st.selectbox(
#     'Which number do you like best?',
#     df['first column'])

# 'You selected: ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected:', option


left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")
    st.echo("HELLO WORLD!")

expander = st.expander("FAQ")
expander.write(
    "Here you could put in some really, really long explanations...")
