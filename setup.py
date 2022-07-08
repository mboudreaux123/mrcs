import os, subprocess, platform

CURRENT_DIR = os.getcwd()
AUTOSTART = "autostart.sh"
SERVICE_DIR = "/etc/systemd/system"
SERVICE_FILE = "robot.service"
SERVICE = ("[Unit]\n" +
           "After=network.service\n" +
           "Description=Start\n"+
           "\n"+
           "[Service]\n"+
           "Type=simple\n"+
           "ExecStart=" + CURRENT_DIR + "/" + AUTOSTART + "\n"
           "\n"+
           "[Install]\n"+
           "WantedBy=multi-user.target\n")

## Check if system is running linux
if platform.system() == "Linux":
    ## Create robot.service service file in the service dir
    file = open(SERVICE_DIR + "/" + SERVICE_FILE, "w")
    file.write(SERVICE)
    file.close()

    ## Start the service immediately and at boot
    subprocess.run(["sudo", "systemctl", "enable", "--now", SERVICE_FILE])
else:
    print("This script is for Linux only.")
