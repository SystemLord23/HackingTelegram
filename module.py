
import os

yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
red = "\033[91m"
banner = lgreen+''' 

      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\\`
             ''``
 _____    _        _   _            _
|_   _|__| | ___  | | | | __ _  ___| | __
  | |/ _ \ |/ _ \ | |_| |/ _` |/ __| |/ /
  | |  __/ |  __/ |  _  | (_| | (__|   <
  |_|\___|_|\___| |_| |_|\__,_|\___|_|\_\

  V 10.3.0	     By Anonymous Hackers
'''+clear

def cls():
    os.system('cls' if os.name=='nt' else 'clear')