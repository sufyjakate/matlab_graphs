import sqlite3, random
import matplotlib.pyplot as plt
import numpy as np
import re
plt.rcdefaults()
fig, ax = plt.subplots()
d = dict()
c = dict()

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
    c.execute('''select count(country) from prof_scherp group by country having (count(country)>1)''')
    tcpvalues = c.fetchall()
    tcpvalues = str(tcpvalues)
    tcpvalues = tcpvalues.replace(',','')
    tcpvalues = tcpvalues.replace('(','')
    tcpvalues = tcpvalues.replace(')','')
    tcpvalues = tcpvalues.replace("'",'')
    tcpvalues = tcpvalues.replace('[','')
    tcpvalues = tcpvalues.replace(']', '')
    tcpvalues = tcpvalues.split()
    #tcpvalues = np.array(tcpvalues)
    #print tcpvalues

    c.execute("select country from prof_scherp")
    country = c.fetchall()

    country = str(country)
    country = country.replace(',','')
    country = country.replace('(','')
    country = country.replace(')','')
    country = country.replace("'",'')
    country = country.replace("u'",'')
    country = country.split()
    #country = country.remove('u')
    #country = list(country)
    #print type(country)
    print country

    d = zip(country, tcpvalues)

    #print  d
    d = dict(d)
    #print d.values()
    #print type(d)

   # c.execute("select count(ID) from prof_scherp ")
   # udpvalues = c.fetchall()
   # udpvalues = np.array(udpvalues)
   # #print type(udpvalues)

    c.execute("select Gender from prof_scherp")
    gen = c.fetchall()
    gen = str(gen)
    gen = gen.replace(',','')
    gen = gen.replace("u'",'')
    gen = gen.replace("'",'')
    gen = gen.replace('(','')
    gen = gen.replace(')','')
    gen = gen.replace(']', '')
    gen = gen.replace('[', '')
    gen = gen.split()
    print gen

    c.execute("select count(Gender) from prof_scherp group by Gender having (count(Gender)>1)")
    cnt = c.fetchall()
    cnt = str(cnt)
    cnt = cnt.replace(',)','')
    cnt = cnt.replace('(','')
    cnt = cnt.replace(',','')
    cnt = cnt.replace(']','')
    cnt = cnt.replace('[','')
    cnt = cnt.split()
    print cnt

    c = zip(gen, cnt)
    #c = dict(c)
    print c

    plt.bar(range(len(d)), map(int,d.values()), align='center')
    plt.xticks(range(len(d)), d.keys())
    plt.tight_layout()
    plt.show()
    plt.bar(range(len(c)), map(int,c.values()), align='center')
    plt.xticks(range(len(c)), c.keys())
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()