import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()
fig, ax = plt.subplots()

conn = sqlite3.connect('prof_scherp.db')
c = conn.cursor()

c.execute('''SELECT count(country) FROM prof_scherp GROUP BY country HAVING (count(country)>1) ''')
data = c.fetchall()
df = pd.DataFrame(data)
print df

c.execute("SELECT country FROM prof_scherp GROUP BY country")
country = c.fetchall()
cf = pd.DataFrame(country)
print cf

ax = df.plot(kind='bar',title="Demographic Analysis", figsize=(15, 10), legend=False, fontsize=12)
ax.set_xlabel("country", fontsize=15)
ax.set_ylabel("no. of users", fontsize=15)
plt.show()
