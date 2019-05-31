# File      : main.py
# NIM/Nama  : 13517141/Tasya Lailinissa Diandraputri

import scraper

print('          _   _                              _                 _                      _    ')
print('         | |_| |__   ___ _ __ ___  _   _ ___(_) ___ _ __   ___| |___      _____  _ __| | __')
print("         | __| '_ \ / _ \ '_ ` _ \| | | / __| |/ __| '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ /")
print('         | |_| | | |  __/ | | | | | |_| \__ \ | (__| | | |  __/ |_ \ V  V / (_) | |  |   < ')
print('          \__|_| |_|\___|_| |_| |_|\__,_|___/_|\___|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\'')
print(' ,-----.,--.                      ,--.       ,---.                              ,--.                ')
print("'  .--./|  ,---.  ,--,--.,--.--.,-'  '-.    '   .-'  ,---.,--.--. ,--,--. ,---. `--',--,--,  ,---.  ")
print("|  |    |  .-.  |' ,-.  ||  .--''-.  .-'    `.  `-. | .--'|  .--'' ,-.  || .-. |,--.|      \| .-. | ")
print("'  '--'\|  | |  |\ '-'  ||  |     |  |      .-'    |\ `--.|  |   \ '-'  || '-' '|  ||  ||  |' '-' ' ")
print(" `-----'`--' `--' `--`--'`--'     `--'      `-----'  `---'`--'    `--`--'|  |-' `--'`--''--'.`-  /  ")
print("                                                                         `--'               `---'   ")
print()

chart = input('Chart link: ')

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) ApplexWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
f = 'Tasya Lailinissa Diandraputri/13517141@std.stei.itb.ac.id'

try:
    if chart.startswith('https://themusicnetwork.com/charts/issues/'):
        data = scraper.scrapeChart(chart, ua, f)
        file = input('Output file (without extention): ')
        scraper.writeDict(file + '.json', data)
        print('Data succesfully saved in data/' + file + '.json')
    else: # not chart.startswith('https://themusicnetwork.com/charts/issues/')
        print('No data found')
except requests.exceptions.RequestException as e:
    print(e)
