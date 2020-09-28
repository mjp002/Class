import os
import time

source = ['/Users/moonj/Github/Class']

target_dir = '/Users/moonj/Github/Class/backup'


target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.esists(target_dir):
    os.mkdir(target_dir)


zip_comman = "zip -r {0} {1}".format(target,' '.join(source))

print ("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')



help(int)
