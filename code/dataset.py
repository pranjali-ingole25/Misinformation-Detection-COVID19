import pandas as pd 

df1  = pd.read_csv("D:/Misinformation detection project/Data/fakeNews.csv")
df2  = pd.read_csv("D:/Misinformation detection project/Data/trueNews.csv")

def new_dataset():
    if 'Binary Label' in df1.columns and 'Label' in df2.columns:
         df1['label'] = df1['Binary Label'] 
         df2['label'] = df2['Label'] 

    df1.drop(columns=['Link','Country','Explanation','Origin', 'Origin_URL', 'Fact_checked_by','Poynter_Label','Binary Label'], inplace=True)
    df2.drop(columns=['Link','Username','Publisher','Label'],inplace=True)

    df1 = df1[['Date Posted', 'Text', 'Region', 'label']]
    df2 = df2[['Date Posted', 'Text', 'Region', 'label']]

    combined_df = pd.concat([df1,df2]).sample(frac=1, random_state=42).reset_index(drop=True)

    combined_df.to_csv('D:/Misinformation detection project/Data/news_dataset.csv', index=False )
