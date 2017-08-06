import json
import os
import time
import argparse
import sys

current_date = time.strftime("%d.%m.%Y_%H%M%S")
count = 0
log_file = '/var/www/syncs/logs/'+current_date+'.log'

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", default = "choose daily | weekly | monthly ", help="configuration file")
args = parser.parse_args()

os.system('tput clear')
print "### SyncS / Security Backup Tool ### "
print "developed by @jaccon | this is another Open Source script "
print('')

print( "Processing type...  {} ".format(
        args.type
        ))

config_file = 'config/'+args.type+'.json'

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
        sys.exit()
