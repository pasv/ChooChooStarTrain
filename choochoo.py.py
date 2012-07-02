##
## SC2 Assistant
## -features: Beeps when larva injects are needed 
## 
## 
##
## Todo, 
## -add a Gtk window showing APM over an average of a minute in a large font for other screen, 
## -package it up in py2exe
## 
import winsound
import SendKeys # optional but fun for {BACKSPACE}6v -> *click*
import _winreg
import os,sys
import time
import subprocess
import win32api, win32con

startupapps=["C:\Program Files (x86)\StarCraft II\StarCraft II.exe", \
 "C:\Program Files (x86)\Razer\Synapse\RzSynapse.exe", \
 "C:\Program Files (x86)\SplitMediaLabs\XSplit\Cultures\XSplit.Core.exe", \
 os.path.expanduser("~\Sc2gears\Sc2gears.exe"), \
 "C:\Program Files (x86)\Winamp\winamp.exe"]

# change as needed
larvasound="C:\Program Files (x86)\OpenOffice.org 3\Basis\share\gallery\sounds\strom.wav"
key=_winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "SOFTWARE\Razer\Starcraft2")
injects = 0
auto_inject = False
protoss_experiment = False
num_of_base = 5 # fuck yes, we're zerg.
sound = True

if(protoss_experiment):
 monitored_value = "ChronoBoostExpired"
else:
 monitored_value = "AdditionalLarvaBirthed"

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def StartUp():
 if(_winreg.QueryValueEx(key, "StartModule")[0]==1): # if in game, no need to launch friends
  return
 for app in startupapps:
  print "Launching " + app + "..."
  subprocess.Popen([app])

StartUp()

while(1):
 time.sleep(.01)
 if(_winreg.QueryValueEx(key, "StartModule")[0]==0):
  injects = 0
 if(_winreg.QueryValueEx(key, monitored_value)[0]==1):
  if(sound == True):
   winsound.PlaySound(larvasound, winsound.SND_FILENAME)
  injects += 1
  print str(injects) + " inject cycles so far this game, not too shabby"
  if(auto_inject == True):
   for n in range(num_of_base):
    SendKeys.SendKeys("{BACKSPACE}6v")
    click(960, 540)
    time.sleep(0.1)
    # perhaps it would be better here to set a temporary camera location before going into the loop then return to it and the selection
   SendKeys.SendKeys("00")
