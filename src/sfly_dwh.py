import time
import datetime
from datetime import timedelta

validVerb = { 'CUSTOMER': ['NEW', 'UPDATE'], 
              'SITE_VISIT': ['NEW'], 
              'IMAGE': ['UPLOAD'], 
              'ORDER': ['NEW', 'UPDATE'] }

validEventType = { 'type': ['CUSTOMER', 'ORDER', 'SITE_VISIT', 'IMAGE']}

validField = { 'CUSTOMER': ['type', 'verb', 'key', 'event_time', 'last_name', 'adr_city', 'adr_state' ],
               'SITE_VISIT': ['type', 'verb', 'key', 'event_time', 'customer_id', 'tags' ],
               'IMAGE': ['type', 'verb', 'key', 'event_time', 'customer_id', 'camera_make', 'camera_model' ],
               'ORDER': ['type', 'verb', 'key', 'event_time', 'customer_id', 'total_amount'] }

validReqField = { 'CUSTOMER': ['type', 'verb', 'key', 'event_time' ],
         'SITE_VISIT': ['type', 'verb', 'key', 'event_time', 'customer_id'],
         'IMAGE': ['type', 'verb', 'key', 'event_time', 'customer_id' ],
         'ORDER': ['type', 'verb', 'key', 'event_time', 'customer_id', 'total_amount'] }

def chkValidField(p):
    return set(validField[p['type']]).issuperset(p.keys())

def chkReqField(p):
    return all( bool(p[x]) for x in validReqField[p['type']] )

def chkValidVerb(p):
    return (p['verb'] in validVerb[p['type']])

def chkRec(e):
   v_valid = False
   if not chkValidField(e):
      print(e.keys(), '[Field is not valid]. As in', ValidField[e['type']])
   elif not chkReqField(e):
      print('One or more reqired field is missing or contains no values.')
   elif not chkValidVerb(e):
      print(e['verb'] + ' is not valid. Expect ', validVerb[e['type']] )
   else:
      v_valid = True
   return v_valid

def Ingest(e, D):
   if e['type'] in validEventType['type']:
      if chkRec(e):
         return D.append(e)
   else:
      print('Invalid Type: ', e['type'])

def convwk(ts):
    dts = datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fz")
    return  datetime.datetime.strftime(dts, "%Y%W")

def isInTally(p, pD):
    return [ pD.index(x) for x in pD if ((p[0] in x) & (p[1] in x)) ]

def isInSumTally(p, pD):
    return [ pD.index(x) for x in pD if (p[0] in x) ]

def setTally(p, pD):
    tmp = isInTally(p, pD)
    if len(tmp) == 0:
       pD.append(p)
    else:
       i=tmp[0]
       pD[i][2] = pD[i][2] + p[2]
       pD[i][3] = pD[i][3] + p[3]
    return pD
 
def sumTally(p, pD):
    tmp = isInSumTally(p, pD)
    if len(tmp) == 0:
       pD.append(p)
    else:
       i = tmp[0]
       pD[i][1] = pD[i][1] + p[1]
       pD[i][2] = pD[i][2] + p[2]
    return pD


def getLatestWeek(D):
    period = D[:]
    period.sort(key = lambda x: x[1], reverse=True)
    return period[0][1]


def getFirstWeek(wts):
    wts_date = datetime.datetime.strptime(str(wts)+'-0', "%Y%W-%w")
    return datetime.datetime.strftime(wts_date - timedelta(weeks=52), '%Y%W')

def getNameLTV(e, c):
    sfly_cust_lifespan=10
    res=[]
    for i in range(len(e)):
        res.append([ e[i][0], 
                     [ c[c.index(x)][1] for x in c if (e[i][0] in x) ][0],
                     e[i][2] * sfly_cust_lifespan ])
    return res



######################
### List tally format: 
### [customer_id, week_period (YYYYWK), sum_of_visit_per_week, sum_of_amount_per_Week ]
###
### List sumTally format: 
### [customer_id, sum_of_visit_per_52wk_period, sum_of_amount_per_52wk_period]
###
######################


def TopXSimpleLTVCustomers(x, D):
    tally=[]
    cust=[]
    for i in range(len(D)):
       if D[i]['type'] in ('CUSTOMER'):
          if D[i]['verb'] in ('NEW'):
             cust.append([ D[i]['key'], D[i]['last_name'] ]) 
       if D[i]['type'] in ('ORDER', 'SITE_VISIT'):
          cust_id = D[i]['customer_id'] 
          wk=convwk(D[i]['event_time'])
          if D[i]['type'] == 'ORDER':
             amt = float(D[i]['total_amount'].split()[0])
             visit = 0
          elif D[i]['type'] == 'SITE_VISIT':
             visit = 1
             amt = 0
          e = [ cust_id, wk, visit, amt ]
          tally = setTally(e, tally)
    topX=[]
    latest_week = getLatestWeek(tally)
    first_week = getFirstWeek(latest_week)
    for i in range(len(tally)):
       if tally[i][1] > first_week:
          e = [ tally[i][0], tally[i][2], tally[i][3] ]
          topX = sumTally(e, topX)
    topX.sort(key = lambda f : f[2], reverse = True)
#    print(getNameLTV(topX[:x], cust))
    return getNameLTV(topX[:x], cust)



