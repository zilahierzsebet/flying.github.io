class Item:
    def __init__(self, carrier, carrier_name, airport, airport_name, arr_flights, arr_del15, arr_delay):
        self.cCode = carrier
        self.cName = carrier_name
        self.aCode = airport
        self.aName = airport_name
        self.flights = arr_flights
        self.delayed = arr_del15
        self.delayMinutes = arr_delay

class Carrier:
    delayedPercent = 0
    avgLate = 0

    def __init__(self, cCode, cName, flights, delayed, delayMinutes, aCode):
        self.cCode = cCode
        self.cName = cName
        self.flights = flights
        self.delayed = delayed
        self.delayedMinutes = delayMinutes
        #self.visited = set()
        self.visited = dict()
        #self.visited.add(aCode)
        self.visited[aCode] = 1

class Airport:
    def __init__(self, aCode, aName, flights):
        self.aCode = aCode
        self.aName = aName
        self.flights = flights


def Zero( value ):
    if value == '':
        return '0.0'
    else:
        return value

file = open('flights_new.csv', 'r')

line = file.readline()
line = file.readline().strip()


items = []
szum = 0
while line:
    datas = line.split(';')
    datas[6] = Zero(datas[6])
    datas[7] = Zero(datas[7])
    datas[15] = Zero(datas[15])
    items.append(Item(datas[2], datas[3], datas[4], datas[5],
                      round(float(datas[6])),
                      round(float(datas[7])),
                      round(float(datas[15]))))
    line = file.readline().strip()

file.close()

carriers = []
carrierDatas = []
for item in items:
    try:
        index = carriers.index(item.cName)
    except Exception:
        carriers.append(item.cName)
        carrierDatas.append(Carrier(item.cCode, item.cName, item.flights,
                                    item.delayed, item.delayMinutes, item.aCode))
    else:
        carrierDatas[index].flights += item.flights
        carrierDatas[index].delayed += item.delayed
        carrierDatas[index].delayedMinutes += item.delayMinutes
        carrierDatas[index].delayedPercent = carrierDatas[index].delayed / carrierDatas[index].flights * 100
        carrierDatas[index].avgLate = carrierDatas[index].delayedMinutes / carrierDatas[index].flights
        #carrierDatas[index].visited.add(item.aCode)
        if item.aCode in carrierDatas[index].visited:
            carrierDatas[index].visited[item.aCode] = carrierDatas[index].visited[item.aCode] + item.flights
        else:
            carrierDatas[index].visited[item.aCode] = item.flights

airports = []
airportDatas = []

for item in items:
    try:
        index = airports.index(item.aName)
    except Exception:
        airports.append(item.aName)
        airportDatas.append(Airport(item.aCode, item.aName, item.flights))
    else:
        airportDatas[index].flights += item.flights

print(len(items))
file = open('carriers.txt', 'w')
print('{0:4s} {1:*^30s}{2:>8}{3:>8}{4:>10} {5} {6:8} {7:16} {8:12} {9}'.format(
    'Code', 'Name of the Airline', 'Flights', 'Delayed', 'Minutes', 'Delayed %', 'Avg Minutes', 'Visited Airports',
    'Top Airport', 'How many'
))
file.write('{0:4s} {1:*^30s}{2:>8}{3:>8}{4:>10} {5} {6:8} {7:16} {8:12} {9}'.format(
    'Code', 'Name of the Airline', 'Flights', 'Delayed', 'Minutes', 'Delayed %', 'Avg Minutes', 'Visited Airports',
    'Top Airport', 'How many'
)+'\n')

for carrier in carrierDatas:
    max_value = max(carrier.visited.values())
    max_keys = [k for k, v in carrier.visited.items() if v == max_value]
    print('{0:>4s} {1:>30s}{2:8}{3:8}{4:10} {5:8.2f}% {6:>11.2f} {7:>16} {8:>11} {9:>9}'.format(
        carrier.cCode, carrier.cName, carrier.flights, carrier.delayed,
        carrier.delayedMinutes, carrier.delayedPercent,
        carrier.avgLate, len(carrier.visited), max_keys[0], max_value
    ))
    file.write('{0:>4s} {1:>30s}{2:8}{3:8}{4:10} {5:8.2f}% {6:>11.2f} {7:>16} {8:>11} {9:>9}'.format(
        carrier.cCode, carrier.cName, carrier.flights, carrier.delayed,
        carrier.delayedMinutes, carrier.delayedPercent,
        carrier.avgLate, len(carrier.visited), max_keys[0], max_value
    )+'\n')
file.close()

file = open('bestAvgLate.txt', 'w')
carrierDatas.sort(key=lambda x: x.avgLate, reverse=False)
file.write('{0:4s} {1:*^30s} {2:11}'.format('Code', 'Name of the Airline', 'Avg Minutes', )
           + '\n')
for i in range(0, 3):
    file.write('{0:4s} {1:30} {2:11.2f}'.format(carrierDatas[i].cCode, carrierDatas[i].cName,
                                         carrierDatas[i].avgLate) + '\n')
file.close()

print('{0:-^84}'.format('Airports'))

file = open('airports.txt', 'w')

airportDatas.sort(key=lambda x: x.flights, reverse=True)
file.write('{0:4} {1:*^70} {2:>7}'.format('Code', 'Airport', 'Flights') + '\n')
print('{0:4} {1:*^70} {2:>7}'.format('Code', 'Airport', 'Flights'))

for a in airportDatas:
    file.write('{0:4} {1:<70} {2:>7}'.format(a.aCode, a.aName, a.flights) + '\n')
    print('{0:4} {1:<70} {2:>7}'.format(a.aCode, a.aName, a.flights))

file.close()

file = open('bestTraffic.txt','w')
file.write('{0:4} {1:*^70} {2:>7}'.format('Code', 'Airport', 'Flights') + '\n')
for i in range(0, 3):
    file.write('{0:4} {1:<70} {2:>7}'.format(airportDatas[i].aCode,
                                             airportDatas[i].aName,
                                             airportDatas[i].flights) + '\n')
file.close()

file = open('carriers.json','w')

file.write("[\n")

for carrier in carrierDatas:
    max_value = max(carrier.visited.values())
    max_keys = [k for k, v in carrier.visited.items() if v == max_value]


    file.write('{ ')
    file.write('"code":"{0}", "name":"{1}", "flights":"{2}", "airNum":"{3}",   "delAvg":"{4:.2f}", "minAvg":"{5:.2f}", "topPort":"{6}"'.format(carrier.cCode,carrier.cName, carrier.flights,len(carrier.visited),carrier.delayedPercent, carrier.avgLate, max_keys[0]))
    file.write(' }, \n')
    file.write(line)

file.write("]")

file.close
