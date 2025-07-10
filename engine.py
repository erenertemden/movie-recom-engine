import pandas as pd
#from textual_rep import 
import numpy as np
import faiss
import requests
import time
from ollama_check import check_ollama_alive
import sys
import os

if not check_ollama_alive():
    sys.exit("run ollama before")


df = pd.read_csv("netflix_titles.csv")
#print(df)


# every row should be represented as multiline string
def create_textual_rep(row):
  def safe_str(val):
        return str(val).strip() if pd.notna(val) else "Not Provided"

  textual_rep = f"""Type: {safe_str(row['type'])}
Title: {safe_str(row['title'])}
Director: {safe_str(row['director'])}
Cast: {safe_str(row['cast'])}
Released: {safe_str(row['release_year'])}
Genres: {safe_str(row['listed_in'])}
Description: {safe_str(row['description'])}
"""
  return textual_rep




#check total number of row number just in case
#print(len(df))
#print(create_textual_rep(df.iloc[0]))
