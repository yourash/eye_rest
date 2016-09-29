import subprocess
import time

#Time in minutes when u see notification
repeat_time=20
#Time in seconds for your rest
rest_time=20

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def main():
	working_repeat_time=repeat_time*60
	working_time=0
	you_are_working=True
	while True:	
		if you_are_working:
			time.sleep(working_repeat_time)
			working_time+=working_repeat_time
			sendmessage('You are working '+str(working_time)+' minutes time to have 20 sec rest!')
			you_are_working=False
		else:
			time.sleep(rest_time)
			sendmessage('20 second passed! Good luck with your work')
			you_are_working=True

if __name__ == '__main__':
	main()