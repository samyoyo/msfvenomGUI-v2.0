try:
    import os
    print """
    {1} > Linux (Ubuntu and Debian-based)
    {2} > Linux (CentOS and RPM-based)
    """
    numper = input("Enter the numper >: ")
    if numper == 1:
        os.system("sudo apt-get install python-pyside")
        os.system("sudo apt-get install python-qt4")
    elif numper == 2:
        os.system("yum install python-pyside pyside-tools")
        os.system("yum install PyQt4")
except KeyboardInterrupt:
    print ("\t\tBye")
    