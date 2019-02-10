[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Instagram Sub Bot Remover
Python Script for detecting and blocking Instagram Sub Bots



### Why Removing Sub Bots?

Instagram new algorithm favors user engagement over other factors for presenting your contents to your followers<sup>[1](#insta-new-alg)</sup><br/>This means if your followers engagement with your contents are low (i.e. less than 10% of your followers like your posts), Instagram ML algorithms identify you as a spammer and prevent your content from getting enough user reach and impression<br/>
Sub Bots engagement rate is zero because they usually lack the the abillity to like your posts or post a comment so they signal instagram to mark you as spammer.<br/>
By removing sub bots, your content will reach much higher engagment rates over time.<br/>

### How this script works?

I have implemented two methods for removing sub bots:
#### Unsupervised
In *Bot* directory, *find_and_block.py* automatically finds sub bots and blocks them.

#### Supervised
In *Assistant* directory, there are 2 scripts.<br/>
*find.py* finds sub bots, then saves them to *Data/BlackList.csv* and *Data/WhiteList.csv*
<br/>*block.py* then reads Data files and block users<br/>You can check algorithms output in Data csv files.<br/>

### Does this script work?

You can checkout algorithm precision in the following table. Results are dervied from running scripts on [my personal Instagram Account](https://instagram.com/soheyl_daliraan)

Algorithm | Precision
------------ | -------------
Unsupervised | 73%
Supervised | 86%

\* In *Unsupervised* script there is an stochastic module which identify subs as bots based on follower to following ratio so precision is affected by this module.


### Run!

First change *configuration.json* file. If you want to save data files to default path, leave *whitelist_path* and *blacklist_path* unchanged.<br/>
Then select one of *Bot* (for *Supervised*) or *Assistent* (for *Unsupervised*) method.

<a name="insta-new-alg">1</a>: [How Instagram’s algorithm works](https://techcrunch.com/2018/06/01/how-instagram-feed-works/)