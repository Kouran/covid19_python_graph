import requests
from numpy import *
from matplotlib.pyplot import *
import datetime


confirmed_serie=[]
death_serie=[]
recovered_serie=[]


def getStateStats(state):
    url="https://corona-stats.online/"+state+"?format=json"
    response=requests.get(url).json()
    return response


def getStateDaily(state, value):
    stats=getStateStats(state)
    return stats[0][value]


def generateGraph(state):
    daily_serie=getStateDaily(state,"confirmedByDay")
    death_serie=getStateDaily(state,"deathsByDay")
    recovered_serie=getStateDaily(state,"recoveredByDay")
    last_update=getStateDaily(state,"lastUpdated").split(".")[0].replace("T"," ")
    first_day=datetime.date.today() - datetime.timedelta(days=len(daily_serie)-1)
    
    t=array([first_day + datetime.timedelta(days=i) for i in range(len(daily_serie))])
    
    fig, ax = subplots(2, sharex=True, gridspec_kw={'hspace': 0})
    ax[0].plot(t, daily_serie, "b-")
    ax[1].plot(t, death_serie, "r-")
    ax[1].plot(t, recovered_serie, "g-")
    ax[0].set_xlim(first_day, datetime.datetime.now())
    fig.autofmt_xdate(bottom=0.2, rotation=30, ha='right', which='major')
    ax[0].legend(['Confirmed cases'])
    ax[1].legend(['Deaths','Recovers'])
    fig.suptitle("COVID-19 stats for "+state+" - "+last_update)
    savefig(state+'.png')
    return



