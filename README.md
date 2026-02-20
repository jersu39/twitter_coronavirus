# Coronavirus Twitter Analysis

This project used data from all geotagged tweets in 2020 to look at the social media impact of Covid-19. Geotagged tweets make up about 2% of all tweets, resulting in a dataset of about 1.1 billion tweets sent in 2020.

First, a list of hashtags related to Covid-19 was created, most in English with one hashtag for Korean, Chinese, and Japanese each:

- #코로나바이러스
- #コロナウイルス
- #冠状病毒
- #covid2019
- #covid-2019
- #covid19
- #covid-19
- #coronavirus
- #corona
- #virus
- #flu
- #sick
- #cough
- #sneeze
- #hospital
- #nurse
- #doctor

From the tweets, all tweets containing these hashtags were extracted. Then for each day in 2020, two files were created. One file counted how many tweets from each country contained a certain hashtag, and the other file counted how many tweets in each language contained a certain hashtag.

First, another pair of files were created summing these counts for country and language across all of 2020. Then the top 10 countries/languages were plotted with 'matplotlib' for '#coronavirus'.

<img src=img/country_corona.png width=100% />

<img src=img/lang_corona.png width=100% />

Then, the same was plotted for '#코로나바이러스'.

<img src=img/country_kr.png width=100% />

<img src=img/lang_kr.png width=100% />

Last, the files organized by day were used to plot the trends over 2020 of how many tweets each day contained each hashtag.

<img src=img/alt_reduce.png width=100% />

This makes sense, considering there is a sudden spike in hashtag mentions around March.
