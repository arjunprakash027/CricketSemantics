# CricketSemantics
CricketSemantics is a NLP project that includes
- A Cricket commentary dataset and scrapping engine to scrape data from cricbuzz
- A Semantic Search Engine built using SentenceTransformers and FAISS.

## Data Scrapping 

- Scrapped Data from cricbuzz 
- Used Scrapy to scrape the data
- Data [here](https://github.com/arjunprakash027/CricketSemantics/blob/main/cricket_data_scrapper/cricket_data.csv)
- full blog on how to do this [here](https://medium.com/@arjunprakash027/scrapping-cricket-data-using-scrapy-9a58d7eeb13b)

## Commentary Search Engine

- Index file is [here](https://github.com/arjunprakash027/CricketSemantics/blob/main/search_engine/cricketSemanticSearch.index)
- Training [code](https://github.com/arjunprakash027/CricketSemantics/blob/main/search_engine/semantic_engine.ipynb)

### How to run locally.

- Download this repo into your local system

-Then
 ```python
 pip install -r requirements.txt
 ```

 -Then go to your commandline or terminal
 ```shell
 python3 semanticSearchCricket.py
 ```

 ### Examples

![image](https://github.com/arjunprakash027/CricketSemantics/assets/72484657/8c4e5289-11d2-4390-ad66-901a2fd378e4)
