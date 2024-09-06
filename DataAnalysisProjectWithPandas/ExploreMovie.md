```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML
from wordcloud import WordCloud
pd.options.display.max_columns = 30
pd.options.display.float_format = '{:.2}'.format
df = pd.read_csv('movies_complete.csv', parse_dates=['release_date'])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>title</th>
      <th>tagline</th>
      <th>release_date</th>
      <th>genres</th>
      <th>belongs_to_collection</th>
      <th>original_language</th>
      <th>budget_musd</th>
      <th>revenue_musd</th>
      <th>production_companies</th>
      <th>production_countries</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>popularity</th>
      <th>runtime</th>
      <th>overview</th>
      <th>spoken_languages</th>
      <th>poster_path</th>
      <th>cast</th>
      <th>cast_size</th>
      <th>crew_size</th>
      <th>director</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>862</td>
      <td>Toy Story</td>
      <td>NaN</td>
      <td>1995-10-30</td>
      <td>Animation|Comedy|Family</td>
      <td>Toy Story Collection</td>
      <td>en</td>
      <td>3e+01</td>
      <td>3.7e+02</td>
      <td>Pixar Animation Studios</td>
      <td>United States of America</td>
      <td>5.4e+03</td>
      <td>7.7</td>
      <td>2.2e+01</td>
      <td>8.1e+01</td>
      <td>Led by Woody, Andy's toys live happily in his ...</td>
      <td>English</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//uXDf...</td>
      <td>Tom Hanks|Tim Allen|Don Rickles|Jim Varney|Wal...</td>
      <td>13</td>
      <td>106</td>
      <td>John Lasseter</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8844</td>
      <td>Jumanji</td>
      <td>Roll the dice and unleash the excitement!</td>
      <td>1995-12-15</td>
      <td>Adventure|Fantasy|Family</td>
      <td>NaN</td>
      <td>en</td>
      <td>6.5e+01</td>
      <td>2.6e+02</td>
      <td>TriStar Pictures|Teitler Film|Interscope Commu...</td>
      <td>United States of America</td>
      <td>2.4e+03</td>
      <td>6.9</td>
      <td>1.7e+01</td>
      <td>1e+02</td>
      <td>When siblings Judy and Peter discover an encha...</td>
      <td>English|Français</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//vgpX...</td>
      <td>Robin Williams|Jonathan Hyde|Kirsten Dunst|Bra...</td>
      <td>26</td>
      <td>16</td>
      <td>Joe Johnston</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15602</td>
      <td>Grumpier Old Men</td>
      <td>Still Yelling. Still Fighting. Still Ready for...</td>
      <td>1995-12-22</td>
      <td>Romance|Comedy</td>
      <td>Grumpy Old Men Collection</td>
      <td>en</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Warner Bros.|Lancaster Gate</td>
      <td>United States of America</td>
      <td>9.2e+01</td>
      <td>6.5</td>
      <td>1.2e+01</td>
      <td>1e+02</td>
      <td>A family wedding reignites the ancient feud be...</td>
      <td>English</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//1FSX...</td>
      <td>Walter Matthau|Jack Lemmon|Ann-Margret|Sophia ...</td>
      <td>7</td>
      <td>4</td>
      <td>Howard Deutch</td>
    </tr>
    <tr>
      <th>3</th>
      <td>31357</td>
      <td>Waiting to Exhale</td>
      <td>Friends are the people who let you be yourself...</td>
      <td>1995-12-22</td>
      <td>Comedy|Drama|Romance</td>
      <td>NaN</td>
      <td>en</td>
      <td>1.6e+01</td>
      <td>8.1e+01</td>
      <td>Twentieth Century Fox Film Corporation</td>
      <td>United States of America</td>
      <td>3.4e+01</td>
      <td>6.1</td>
      <td>3.9</td>
      <td>1.3e+02</td>
      <td>Cheated on, mistreated and stepped on, the wom...</td>
      <td>English</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//4wjG...</td>
      <td>Whitney Houston|Angela Bassett|Loretta Devine|...</td>
      <td>10</td>
      <td>10</td>
      <td>Forest Whitaker</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11862</td>
      <td>Father of the Bride Part II</td>
      <td>Just When His World Is Back To Normal... He's ...</td>
      <td>1995-02-10</td>
      <td>Comedy</td>
      <td>Father of the Bride Collection</td>
      <td>en</td>
      <td>NaN</td>
      <td>7.7e+01</td>
      <td>Sandollar Productions|Touchstone Pictures</td>
      <td>United States of America</td>
      <td>1.7e+02</td>
      <td>5.7</td>
      <td>8.4</td>
      <td>1.1e+02</td>
      <td>Just when George Banks has recovered from his ...</td>
      <td>English</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//lf9R...</td>
      <td>Steve Martin|Diane Keaton|Martin Short|Kimberl...</td>
      <td>12</td>
      <td>7</td>
      <td>Charles Shyer</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>44686</th>
      <td>439050</td>
      <td>Subdue</td>
      <td>Rising and falling between a man and woman</td>
      <td>NaT</td>
      <td>Drama|Family</td>
      <td>NaN</td>
      <td>fa</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Iran</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.072</td>
      <td>9e+01</td>
      <td>Rising and falling between a man and woman.</td>
      <td>فارسی</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//pfC8...</td>
      <td>Leila Hatami|Kourosh Tahami|Elham Korda</td>
      <td>3</td>
      <td>9</td>
      <td>Hamid Nematollah</td>
    </tr>
    <tr>
      <th>44687</th>
      <td>111109</td>
      <td>Century of Birthing</td>
      <td>NaN</td>
      <td>2011-11-17</td>
      <td>Drama</td>
      <td>NaN</td>
      <td>tl</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sine Olivia</td>
      <td>Philippines</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>0.18</td>
      <td>3.6e+02</td>
      <td>An artist struggles to finish his work while a...</td>
      <td>NaN</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//xZkm...</td>
      <td>Angel Aquino|Perry Dizon|Hazel Orencio|Joel To...</td>
      <td>11</td>
      <td>6</td>
      <td>Lav Diaz</td>
    </tr>
    <tr>
      <th>44688</th>
      <td>67758</td>
      <td>Betrayal</td>
      <td>A deadly game of wits.</td>
      <td>2003-08-01</td>
      <td>Action|Drama|Thriller</td>
      <td>NaN</td>
      <td>en</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>American World Pictures</td>
      <td>United States of America</td>
      <td>6.0</td>
      <td>3.8</td>
      <td>0.9</td>
      <td>9e+01</td>
      <td>When one of her hits goes wrong, a professiona...</td>
      <td>English</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//eGga...</td>
      <td>Erika Eleniak|Adam Baldwin|Julie du Page|James...</td>
      <td>15</td>
      <td>5</td>
      <td>Mark L. Lester</td>
    </tr>
    <tr>
      <th>44689</th>
      <td>227506</td>
      <td>Satan Triumphant</td>
      <td>NaN</td>
      <td>1917-10-21</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>en</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Yermoliev</td>
      <td>Russia</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.0035</td>
      <td>8.7e+01</td>
      <td>In a small town live two brothers, one a minis...</td>
      <td>NaN</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//aorB...</td>
      <td>Iwan Mosschuchin|Nathalie Lissenko|Pavel Pavlo...</td>
      <td>5</td>
      <td>2</td>
      <td>Yakov Protazanov</td>
    </tr>
    <tr>
      <th>44690</th>
      <td>461257</td>
      <td>Queerama</td>
      <td>NaN</td>
      <td>2017-06-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>en</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.16</td>
      <td>7.5e+01</td>
      <td>50 years after decriminalisation of homosexual...</td>
      <td>English</td>
      <td>&lt;img src='http://image.tmdb.org/t/p/w185//oxFE...</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>Daisy Asquith</td>
    </tr>
  </tbody>
</table>
<p>44691 rows × 22 columns</p>
</div>




```python

```
