import pandas as pd
import numpy as np
import faiss
import sys
import requests
import time
import os
from textual_rep import create_textual_rep
from ollama_check import check_ollama_alive

#ollama checking
if not check_ollama_alive():
    sys.exit("run ollama before")
#

#load data
df = pd.read_csv("data/netflix_titles.csv")
df['textual_rep'] = df.apply(create_textual_rep, axis=1)
#

#embedding params
dim = 4096
X = np.zeros((len(df), dim), dtype="float32")
#

#embedding
for i, text in enumerate(df["textual_rep"]):
    try:
        if i % 100 == 0:
            print(f" {i} row processed")
            time.sleep(6)

        res = requests.post("http://localhost:11434/api/embeddings", json={
            "model": "llama3",
            "prompt": text
        })

        embedding = np.array(res.json()["embedding"]).astype("float32") #embeddign type match
        X[i] = embedding

    except Exception as e:
        print(f"error at ({i}): {e}")
        continue
#

#save embedding as index
np.save("data/embeddings.npy", X)

index = faiss.IndexFlatL2(dim)
index.add(X)
faiss.write_index(index, "data/index.faiss")
#

#checking
print("Embedding ve FAISS index ok")
