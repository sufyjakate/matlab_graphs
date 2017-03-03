import sqlite3, random
import matplotlib.pyplot as plt
import numpy as np
import re
plt.rcdefaults()
fig, ax = plt.subplots()

def main():
    #x = {'UDP': 0, 'TCP': 0}
    # Creating and connecting the database
    conn = sqlite3.connect('prof_scherp.db')
    c = conn.cursor()
    #create(c)
    #conn.commit()
    plott(c)


def plott(c):
    # plotting the data
    c.execute('''select count(country) from prof_scherp group by country having (count(country)>0)''')
    tcpvalues = c.fetchall()
    print type(tcpvalues)

    c.execute("select country from prof_scherp")
    country = c.fetchall()
    print country

    c.execute("select count(ID) from prof_scherp ")
    udpvalues = c.fetchall()
    udpvalues = np.array(udpvalues)
    print udpvalues

    y_pos = np.arange(len(country))

    ax.barh(y_pos, 3000 , align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(country)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('number of people')
    ax.set_title('Demographic Analysis - Country Wise')

    plt.show()

if __name__ == '__main__':
    main()