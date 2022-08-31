from datetime import datetime, timedelta
from operator import itemgetter

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

schedule = """Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-24:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 00:00-23:59
Mon 05:00-13:00
Mon 15:00-21:00"""

def Mayor_descanso(schedule):
    meetings = schedule.splitlines()

    meetings_by_days = {}
    for item in meetings:
        index = days.index(item[0:3])
        start = item[4:9]
        end = item[10:15]
        if(index not in meetings_by_days.keys()):
            meetings_by_days[index] = [[start, end]]
        else:
            meetings_by_days[index].append([start, end])

    meetings_by_days = dict(sorted(meetings_by_days.items()))

    format = '%H:%M'
    hora_inicial =  datetime.strptime('0:00', format)
    descanso_mayor = datetime.strptime('0:00', format)
    
    for value in meetings_by_days.values():
        value = (sorted(value, key=itemgetter(0)))
        print(value)
        for item in value:
            if item[1] == '24:00':
                item[1] = '00:00'
            descanso  = datetime.strptime(item[0], format) - hora_inicial
            if descanso.days == -1:
                descanso = descanso + timedelta(days=1)
            descanso = datetime.strptime(str(descanso)[:-3], format)
            if descanso > descanso_mayor:
                descanso_mayor = descanso
                
            hora_inicial = datetime.strptime(item[1], format)

    descanso  = datetime.strptime('00:00', format) - hora_inicial
    if descanso.days == -1:
        descanso = descanso + timedelta(days=1)    
    descanso = datetime.strptime(str(descanso)[:-3], format)

    if descanso > descanso_mayor:
            descanso_mayor = descanso
    
    return str(descanso_mayor)[10:16]

print(Mayor_descanso(schedule))


            


