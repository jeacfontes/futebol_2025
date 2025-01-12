import pandas as pd
import streamlit as st
import csv

st.set_page_config(layout="wide")

df = pd.read_csv("Matches.csv", sep=",", decimal=".")
df