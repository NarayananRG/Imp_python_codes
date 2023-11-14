import pandas as pd
import os
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
from matplotlib import pyplot as plt
import seaborn as sns
import emoji
from collections import Counter

pd.set_option('display.max_columns', None)

os.chdir(r'C:\Users\laksrgan\OneDrive - Keysight Technologies\Recordings\New folder')

comm = pd.read_csv('UScomments.csv', delimiter=',', on_bad_lines='skip', nrows=1000)
comm.dropna(axis=0, inplace=True)

# sentiment analysis
comm['polarity'] = comm['comment_text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# wordcloud chart
comm_pos = comm[comm['polarity'] == 1]
comm_neg = comm[comm['polarity'] == -1]
comm_str_pos = ''.join(comm_pos['comment_text'])
comm_str_neg = ''.join(comm_neg['comment_text'])
wordcloud_pos = WordCloud(stopwords=set(STOPWORDS)).generate(comm_str_pos)
#plt.imshow(wordcloud_pos, interpolation='bilinear')
wordcloud_pos.to_file('wordcloud_pos.png')
wordcloud_neg = WordCloud(stopwords=set(STOPWORDS)).generate(comm_str_neg)
#plt.imshow(wordcloud_neg, interpolation='bilinear')
wordcloud_neg.to_file('wordcloud_neg.png')


# emoji analysis
lst=[]
for x in comm['comment_text']:
    for i in x:
        if x in emoji.EMOJI_DATA:
            lst.append(x)



a=Counter(lst)
coll=['count']

df=pd.DataFrame.from_dict(a, orient='index', columns=coll)
df=df.reset_index()

sns.barplot(x='index',y='count',data=df)


#collect multiple files

os.chdir(r'C:\Users\laksrgan\OneDrive - Keysight Technologies\Recordings\New folder\additional_data')
files=os.listdir()

df1=pd.DataFrame()
for i in files:
    if i.endswith('.csv'):
        try:
            df=pd.read_csv(i,encoding='utf-8')
            df1=pd.concat([df,df1],axis=0)
        except UnicodeDecodeError:
            print(f'file error {i}')
            df = pd.read_csv(i, encoding='latin-1')
            df1=pd.concat([df,df1],axis=0)

df1.drop_duplicates(inplace=True)

#Read Json files
json_df=pd.read_json('CA_category_id.json')
final_df=pd.DataFrame()
for i in json_df['items']:
    df_jn = pd.json_normalize(i)
    norm_df=pd.DataFrame(df_jn)
    final_df=pd.concat([final_df,norm_df],axis=0)
print(df1.columns)
df1.to_csv('df1.csv')
final_df['id']=final_df['id'].astype('int64')
print(final_df.columns)
final_df.to_csv('final_csv.csv')
#merged_df=df1.merge(final_df,right_on='id',left_on='category_id',how='left')
#print(merged_df['snippet.title'].value_counts())
#merged_df=merged_df.rename({'snippet.title':'category_name'})
#print(merged_df.columns)
#merged_df.to_csv('merged_df.csv')
#merged_df.drop(['kind', 'etag', 'id',
#       'snippet.channelId', 'snippet.title', 'snippet.assignable'],axis=1,inplace=True)

#sns.boxplot(x='category_name',y='likes',data=merged_df, hue='category_name')
#plt.xticks(rotation='vertical')
#plt.show()

