door_locked = True
alarm_active = True

if door_locked:
    print('Дверь заперта')
    alarm_active = False
else:
    print('Дверь не заперта')
    alarm_active = True

if alarm_active:
    print('Сигнализация включена')
else:
    print('Сигнализация выключена')