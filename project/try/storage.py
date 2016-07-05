#!/usr/bin/python2
import commands,os
import cgi
while True:
	commands.getstatusoutput("clear")
	commands.getstatusoutput("tput setaf 1")
	print "\t\t\t\tWelcome to Cloud"
	commands.getstatusoutput("tput setaf 0")
	print "\t\t\t\t----------------\n\n"
	print """
	Enter 2:For dynamic object storage
	Enter 3:For block storage
	Enter 4:Exit
	Enter 5:For iaas
	"""
	choice=raw_input()
	if (int)(choice) == 2:
		vall='13000'
		user=raw_input("Enter username: ")
		while ((int)(vall))>12288:
			vall=raw_input("Enter size not more than 12288 MB(in MB's): ")
		print commands.getstatusoutput("echo -e 'y\n'|sudo lvcreate --size "+vall+"M --name "+user+"lv staasvg")
		print commands.getstatusoutput("mkfs.ext4 /dev/staasvg/"+user+"lv")
		print commands.getstatusoutput("iptables -F")
		commands.getstatusoutput("chown test /dev/staasvg/"+user+"lv")
		commands.getstatusoutput("chmod 700 /dev/staasvg/"+user+"lv")
		commands.getstatusoutput("systemctl restart sshd")
		commands.getstatusoutput("clear")
		val='y'
		while ((int)(vall))<12288 and (val=='y'):
			val=raw_input("Storage created. Do you want to increase the size of drive?(y/n): ")
			if(val=='y'):
				val='13000'
				while ((int)(val))>(12288-(int)(vall)):
					val=raw_input("Enter the amount you want to extend in MB's(not more than "+(str)(12288-(int)(vall))+"MB): ")
				commands.getstatusoutput("lvextend --size +"+val+"M /dev/staasvg/"+user+"lv")
				commands.getstatusoutput("resize2fs /dev/staasvg/"+user+"lv")
				vall=(str)((int)(vall)+(int)(val))
				val='y'
	elif (int)(choice) == 3:
		vall='13000'
		user=raw_input("Enter username: ")
		while ((int)(vall))>12288:
			vall=raw_input("Enter size not more than 12288 MB(in MB's): ")
		commands.getstatusoutput("echo -e 'y\n'|lvcreate --size "+vall+"M --name "+user+"lv staasvg")
		f=open('/etc/tgt/conf.d/ayush.conf','w')
		f.write('<target cloud>\nbacking-store\t/dev/staasvg/'+user+'lv\n</target>\n')
		f.close()
		commands.getstatusoutput("iptables -F")
		commands.getstatusoutput("systemctl restart tgtd")
		commands.getstatusoutput("clear")
	elif (int)(choice) == 4:
		exit()
	elif (int)(choice) == 5:
		user=raw_input("Enter username: ")
		mem=raw_input("Enter memory(in MB's: ")
		cpu=raw_input("Enter no. of CPU cores: ")
		hd=raw_input("Enter size of hard disk(in GB's): ")
		commands.getstatusoutput("mkdir /iaas")
		commands.getstatusoutput("qemu-img create -f qcow2 /iaas/"+user+".qcow2 "+hd+"G")
		commands.getstatusoutput("virt-install --name "+user+" --memory "+mem+" --vcpus "+cpu+" --os-type linux --os-variant rhel7 --location ftp://192.168.70.131/rhel7/ --disk /iaas/"+user+".qcow2 --graphics vnc,port=6000,listen=0.0.0.0,password=pass --noautoconsole")
		commands.getstatusoutput("vncviewer 192.168.70.131:6000")
		commands.getstatusoutput("clear")
	elif (int)(choice) == 6:
		commands.getstatusoutput("systemctl restart sshd")
		commands.getstatusoutput("sshpass -p redhat ssh -X -l test 192.168.70.131 firefox")
		commands.getstatusoutput("clear")
