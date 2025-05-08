import pandas as pd
from code.dataset import new_dataset
from code.preprocess import preprocess_text,clean_dataset
from code.model import model_evaluation 

def main():
    
    # Dataset
    df = pd.read_csv("D:/Misinformation detection project/Data/news_dataset.csv")
    #print(df.head())
     
    #EDA
    df = clean_dataset(df)

    # Preprocess 
    df['clean_text'] = df['Text'].apply(preprocess_text)

    # Model
    model_evaluation(df['clean_text'], df['label'])

if __name__ == "__main__":
    
    main()