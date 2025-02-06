# import
from colorama import Fore
import os
import socket
import requests

# title screen
print( Fore.RED + "░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ ")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ")
print("░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░   ")
print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░ ")
input("~Press enter to start packaging:")
os.system('cls' if os.name == 'nt' else 'clear')

# warning
print(Fore.GREEN + "                         __    _                                   ")
print("                    _wro        scroo                              ")
print("                 _dP                 9m_                           ")
print("               _#P                     9#_                         ")
print("              d#@                       9#m                        ")
print("             d##                         ###                       ")
print("            J###                         ###L                      ")
print("            {###K                       J###K                      ")
print("            ]####K      ___aaa___      J####F                      ")
print("        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  ")
print("     _g##############mZ_         __g##############m_               ")
print("   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             ")
print("  a###            ,Z #####@   ###### hg            M##m            ")
print(" J#@              0L   *##     ##@   J#              *#K           ")
print(" #                `#     _gmwgm_~    dF               `#_          ")
print("7F                  #_   ]#####F   _dK                 JE          ")
print("]                    *m__ ##### __g@                    F          ")
print("                        PJ#####LP                                  ")
print(" `                       0######_                      '           ")
print("                       _0########_                                 ")  
print("     .               _d#####^#####m__              ,               ")
print("      o*w_________am#####Pi   ~9#####mw_________w*o                ")  
print("          hh9@#####@Mhh           hhP@#####@Mhh                    ")
print("\nThis project was created by https://github.com/untitled-guy under the GPLv3 License")
input("\nWARNING: By using Project Package, you agree that you will only use Project Package for\nEthical hacking only, you are responsible for any damage caused by using the program. ")

# main menu
def menu():    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ")
    print("░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░   ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░ |by untitled-guy")
    print("_____________________________________________________________________________________________|https://github.com/untitled-guy")
    print("(1).IP loggers      (4).Google Dork        (7).See your ip address                          ")
    print("(2).Image search    (5).Account viewer     (8).OSINT framework       ~(License: GPLv3)~     ")
    print("(3).Privacy tools   (6).Account searcher                                                    ")                                                                                          
    print("____________________________________________________________________________________________")          
    opt=input("~~~Option:")
    if opt == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~IP loggers~")
        print("- Grabify: https://grabify.link/")
        print("- Ip Logger: https://iplogger.org/")
        input("Press enter to go back: ")
        menu()
    if opt == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~Image search~")
        print("- They see your photos: https://theyseeyourphotos.com/")
        print("- Google Images: https://images.google.com/")
        print("- Bing images: https://www.bing.com/images?brdr=1")
        print("- Yahoo images: https://images.search.yahoo.com/?guccounter=1")
        print("- Tin Eye: https://tineye.com/")
        print("- PimEyes: https://pimeyes.com/en")
        print("- Yandex images: https://www.yandex.com/images")
        input("Press enter to go back: ")
        menu()
    if opt == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~Privacy tools~")
        print("- Tor Browser: https://www.torproject.org/")
        print("- Tails: https://tails.net/")
        print("- Proton VPN: https://protonvpn.com/")
        print("- Proton Mail: https://proton.me/mail ")
        print("- Graphene OS: https://grapheneos.org/")
        print("- Qubes OS: https://www.qubes-os.org/")
        input("Press enter to go back: ")
        menu()
    if opt == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~Google dork~")
        print("- Google dork cheatsheet: https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06")
        print("- List of search engines: https://en.wikipedia.org/wiki/List_of_search_engines")
        print("Tip: Try hacking multiple search engines for different results.")
        input("Press enter to go back: ")
        menu()
    if opt == "8":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~OSINT framework~")
        print("- https://osintframework.com/")
        input("Press enter to go back: ")
        menu()
    if opt == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~Account searcher~")
        print("- WhatsMyName: https://whatsmyname.app/")
        print("- Namech_k: https://namechk.com/")
        print("- namecheckr: https://www.namecheckr.com/")
        print("- usersearch: https://usersearch.org/results_normal.php")
        print("- ThatsThem: https://thatsthem.com/")
        print("- Name CHECKUP: https://namecheckup.com/")
        print("- Instant username search: https://instantusername.com/?q=biden")
        print("- Names Directory: https://namesdir.com/")
        input("Press enter to go back: ")
        menu()
    if opt == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~Account viewer~")
        print("- Instagram Infact: https://inflact.com/instagram-viewer/profile/?profile=")
        print("- Facebook social searcher:  https://www.social-searcher.com/facebook-search/")
        print("- Reddit metis: https://redditmetis.com/#")
        input("Press enter to go back: ")
        menu()
    if opt == "7":
        # show ip address
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~IP address~")
        def get_local_ip():
            """Get local IP address"""
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip

        def get_public_ip():
            """Get public IP address"""
            try:
                response = requests.get('https://api.ipify.org')
                return response.text
            except requests.exceptions.RequestException as e:
                return "Failed to retrieve public IP address"

        def main():
            print("- Local IP Address:", get_local_ip())
            print("- Public IP Address:", get_public_ip())

        if __name__ == "__main__":
            main()
        input("Press enter to go back: ")
        menu()
menu()
                                                                                  
