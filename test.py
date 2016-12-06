#!/usr/bin/python

import os, time
import sys, commands


#step1 = commands.getoutput('ssh root@192.168.11.250 source /root/keystonerc_admin; openstack server create --image 5ec80645-b747-4115-80dc-9928c62ccdb8 --nic net-id=b25eb748-9995-48b6-8f8b-5727fefaead6 --flavor m1.small --availability-zone nova ncktest')
step1 = commands.getoutput('ssh root@192.168.11.250 sh /tmp/test2.sh')
step2 = commands.getoutput('ssh root@192.168.11.250 sh /tmp/test3.sh').split('=')[1]
#step2 = commands.getoutput('ssh root@192.168.11.250 sh /tmp/test3.sh')
time.sleep(50)


step3 = commands.getoutput('ssh -oStrictHostKeyChecking=no -i /tmp/adminkp1.pem centos@{} hostname'.format(step2))
step4 = commands.getoutput('ssh centos@{} -i /tmp/adminkp1.pem /sbin/ifconfig'.format(step2))
step = commands.getoutput('ping -c 10 {}'.format(step2))
step5 = commands.getoutput("step2 >> /tmp/jenkins_logs.txt")
step6 = commands.getoutput("step3 >> /tmp/jenkins_logs.txt")
step7 = commands.getoutput("step4 >> /tmp/jenkins_logs.txt")
time.sleep(10)

step8 = commands.getoutput('ssh root@192.168.11.250 sh /tmp/test4.sh')
print "IP : ",step2 
print "Hostname : ",step3
print "IFCONFIG OUTPUT : ",step4


