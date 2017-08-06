import json
import os
import time

current_date = time.strftime("%d.%m.%Y_%H%M%S")
count = 0
log_file = '/var/www/syncs/logs/'+current_date+'.log'
config_file = 'config.json'

os.system('tput clear')
print "SyncS - Security Backup Tool"
print('')
with open(config_file) as json_file:  
    data = json.load(json_file)
    for p in data['sites']:
        count=count+1
        print count
        print('site: ' + p['website'])
        print('source: ' + p['from'])
        print('destination: ' + p['to'])
        print ('')
        print ('backup in progress.... please waiting....')
        print ('')
        print ('')
        # execute command
        os.system('rsync -Cravz --progress --delete-excluded '+p['from']+' '+p['to']+' --log-file='+log_file)
        print('')
