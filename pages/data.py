# imports
import streamlit as st
import pandas as pd


def write():
    """Used to write the page in the app.py file"""
    st.title('Data Description')
    st.write("""
   this page shows the data for project
   we have train data, store data, test data and submission data .
    """)
    na_value=['',' ','nan','Nan','NaN','na', '<Na>']
    train = pd.read_csv('src/data/train.csv', na_values=na_value)
    store = pd.read_csv('src/data/store.csv', na_values=na_value)

    full_train = pd.merge(left = train, right = store, how = 'inner', left_on = 'Store', right_on = 'Store')
    full_train = full_train.set_index('Store')
    st.write('---')
    st.write(' Stores Data')
    st.write(store)
    st.write('---')
    st.write('Sample historical data including Sales and Customers')
    st.write(train)
    st.write('---')
    st.write('Sample training data containing the input features')
    st.write(full_train)