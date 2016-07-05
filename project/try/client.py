#!/usr/bin/python2
commands.getstatusoutput(yum install fuse-sshfs)
commands.getstatusoutput(systemctl restart sshd)
commands.getstatusoutput(mkdir /media/user)
