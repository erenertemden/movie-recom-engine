import pandas as pd
import numpy as np
import faiss
import requests
import time
import sys
import os

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

