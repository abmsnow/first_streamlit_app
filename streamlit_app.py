## First Excercise
import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorite')
streamlit.text('Omega 3 & Bluerberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## Importing pandas

import pandas

## We want pandas to read our CSV file from that S3 bucket so we use a pandas function called read_csv  to pull the data into a dataframe we'll call my_fruit_list. 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

## ask the streamlit library to display it on the page by typing:
streamlit.dataframe(my_fruit_list)
