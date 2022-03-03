import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

#with open('data.csv') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

#for row in csv_reader:
#        language_counter.update(response['LanguagesWorkedWith'].split(';'))
for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.tight_layout()

plt.title("Most popular languages")
plt.ylabel('Programming languages')
#plt.xlabel('Number of people who use')

plt.show()
#print(languages)
#print(popularity)
    #row = next(csv_reader)
    #print(row)
    #print(row['LanguagesWorkedWith'].split(';'))
