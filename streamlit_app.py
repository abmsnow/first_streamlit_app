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

##  We want the customer to be able to choose the fruits by name!!
my_fruit_list = my_fruit_list.set_index('Fruit')

## Add a user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies.
## Let's put a pick list here so they can pick the fruit they want to include 
## We'll ask our app to put the list of selected fruits into a variable called fruits_selected. 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

##Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set (and assign that data to a variable called fruits_to_show). 
fruits_to_show = my_fruit_list.loc[fruits_selected]

##Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page
 ## Display the table on the page.
streamlit.dataframe(fruits_to_show)
