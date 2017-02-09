'''
Created on May 30, 2016

@author: sufyjakate
'''

import sqlite3, random
import matplotlib.pyplot as plt


def main():
    x = {'UDP': 0, 'TCP': 0}
    # Creating and connecting the database
    conn = sqlite3.connect('matrix.db')
    c = conn.cursor()
    create(c)
    insert(x, c)
    conn.commit()
    plott(c)


def create(c):
    # creating the table
    try:
        c.execute(''' CREATE TABLE protocol(TYPE text, SIZE real)''')
    except:
        print "table already exist, so using previous one"


def insert(x, c):
    # Insert the rows of data
    for one in xrange(1000):
        a = x.keys()[random.randint(0, 1)]
        b = str(random.randint(1, 10000))
        c.execute("INSERT INTO protocol VALUES('" + a + "'," + b + ")")


def plott(c):
    # plotting the data
    c.execute("SELECT SIZE from protocol where TYPE = 'TCP'")
    tcpvalues = c.fetchall()

    c.execute("SELECT SIZE from protocol where TYPE = 'UDP'")
    udpvalues = c.fetchall()

    plt.plot(tcpvalues, label="TCP", color="red", alpha=0.7)
    plt.plot(udpvalues, label="UDP", color="blue", alpha=0.3)
    plt.ylabel("size")
    plt.xlabel("protocol")
    plt.autoscale(enable=True, axis='both', tight=None)
    legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('white')
    plt.show()
    print "Done with plot"


if __name__ == '__main__':
    main()