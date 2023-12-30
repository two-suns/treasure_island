def start_adventure():
    print("Welcome to Sudden Death Island!")
    print('''
       ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
      ''')
    print("Your mission is to find the treasure...")
    print("but beware, death is around every corner!")
    print("\n")
    print('''
           mm###########mmm
        m####################m
      m#####`"#m m###"""'######m
     ######*"  "   "   "mm#######
   m####"  ,             m"#######m
  m#### m*" ,'  ;     ,   "########m
  ####### m*   m  |#m  ;  m ########
 |######### mm#  |####  #m##########|
  ###########|  |######m############
  "##########|  |##################"
   "#########  |## /##############"
     ########|  # |/ m###########
      "#######      ###########"
        """"""       """""""""
      ''')

    # Chapter 1: The Mysterious Arrival
    print('''Zandar washes up onto a deserted island. His eyes flutter open. He's on a beach, but how did he get here? The last thing he remembers is his ship being swallowed by a monstrous storm. He slowly stands, brushing sand off his tattered clothes. In front of him lies a dense jungle; behind, the endless ocean. A wooden sign catches his eye. It reads: "Welcome to Sudden Death Island. Beware the choices you make. Treasure beyond measure may be found by one brave, cunning, and lucky enough to succeed. Will Zandar accept the challenge? Does he explore the jungle or wait for rescue on the beach?''')
    choice = input("Type 'jungle' to enter the jungle or 'wait' to wait for rescue: ").lower()

    if choice == "jungle":
        chapter2()
    elif choice == "wait":
        chapter3()
    else:
        print("Invalid choice. Please type 'explore' or 'wait'.")
        start_adventure()

start_adventure()