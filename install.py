try:
    import os
    print """
    {1} > Linux (Ubuntu and Debian-based)
    {2} > Linux (CentOS and RPM-based)
    """
    number = input("Enter the number >: ")
    if number == 1:
        os.system("sudo apt-get install python-pyside")
        os.system("sudo apt-get install python-qt4")
        os.system("mkdir /opt/msfvenomGUI")
        os.system("cp msfvenomGUIv2.0.py /opt/msfvenomGUI/")
        os.system("chmod +x msfvenomGUI")
        os.system("cp msfvenomGUI /usr/bin/")
        print("write in Terminal =>> msfvenomGUI")
    elif number == 2:
        os.system("yum install python-pyside pyside-tools")
        os.system("yum install PyQt4")
        os.system("mkdir /opt/msfvenomGUI")
        os.system("cp msfvenomGUIv2.0.py /opt/msfvenomGUI/")
        os.system("chmod +x msfvenomGUI")
        os.system("cp msfvenomGUI /usr/bin/")
        print("write in Terminal =>> msfvenomGUI")
except KeyboardInterrupt:
    print ("\t\tBye")

    
