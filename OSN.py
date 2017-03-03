import sqlite3, random
import matplotlib.pyplot as plt
import re


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
    print tcpvalues

    c.execute("select count(ID) from prof_scherp ")
    udpvalues = c.fetchall()
    print udpvalues

    plt.plot(tcpvalues, label="Countries", color="blue", alpha=0.7)
    #plt.plot(udpvalues, label="Numbers of Users", color="blue", alpha=0.3)
    plt.ylabel("number of users")
    plt.xlabel("countries")
    plt.autoscale(enable=True, axis='both', tight=None)
    legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('white')
    plt.show()
    print "Done with plot"


if __name__ == '__main__':
    main()