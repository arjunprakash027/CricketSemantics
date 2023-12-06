import numpy as np
import pandas as pd
from icecream import ic
import faiss
from faiss import read_index
from sentence_transformers import SentenceTransformer
encoder = SentenceTransformer('multi-qa-mpnet-base-dot-v1')
index = read_index("cricketSemanticSearch.index")
df = pd.read_csv("/mnt/d/projects/large_projects/CricketSemantics/cricket_data_scrapper/cricket_data.csv")

def search(text):
    search_text = text
    search_vector = encoder.encode(search_text)
    _vector = np.array([search_vector])
    faiss.normalize_L2(_vector)
    k = index.ntotal
    #ic(k)
    distances,ann = index.search(_vector,k=k)
    # ic(distances)
    # ic(ann[0][0:5])

    for x in ann[0][0:5]:
        ic({
            "commentry":df.iloc[x]['commentry'],
            "match":df.iloc[x]['match'],
            "ball":df.iloc[x]['ball']
        })

    results = pd.DataFrame({'distances': distances[0], 'ann': ann[0]})


if __name__ == '__main__':
    search(input("What do you wanna search?:"))