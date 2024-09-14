light_status = True  # свет включён
ac_status = False  # кондиционер выключен
li = lambda a: 'Да' if a else 'Нет'
print(f'Свет включён: {li(light_status)}')
print(f'Кондиционер включён: {li(ac_status)}')
