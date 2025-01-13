import pandas as pd
import streamlit as st
import csv

st.set_page_config(layout="wide")

matches = pd.read_csv("Matches.csv", sep=",", decimal=".")
ratings = pd.read_csv("EloRatings.csv", sep=",", decimal=".")

matches
ratings