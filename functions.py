# main colors
import os
import time
import threading
import shutil

def clear():
    os.system("cls")

def center(text):
    width = shutil.get_terminal_size().columns
    return text.center(width)


main = "\033[38;2;193;44;196m" # text
warn = "\033[38;2;255;46;99m" # danger 
reset = "\033[0m" # back to white

def retardprint(warnornah, content):
    if warnornah == True:
        print(f"{warn}{content}{reset}")
    else:
        print(f"{main}{content}{reset}")

def retardinput(warnornah, content):
    if warnornah == True:
        return input(f"{warn}{content}{reset}")
    else:
        return input(f"{main}{content}{reset}")

def pause():
    os.system("pause")

def banner(e):
    thumb = '''

                                          :     
                    ,;L.                 t#,    
                  f#i EW:        ,ft    ;##W.   
                .E#t  E##;       t#E   :#L:WE   
  :KW,      L  i#W,   E###t      t#E  .KG  ,#D  
   ,#W:   ,KG L#D.    E#fE#f     t#E  EE    ;#f 
    ;#W. jWi:K#Wfff;  E#t D#G    t#E f#.     t#i
     i#KED. i##WLLLLt E#t  f#E.  t#E :#G     GK 
      L#W.   .E#L     E#t   t#K: t#E  ;#L   LW. 
    .GKj#K.    f#E:   E#t    ;#W,t#E   t#f f#:  
   iWf  i#K.    ,WW;  E#t     :K#D#E    f#D#;   
  LK:    t#E     .D#; E#t      .E##E     G#t    
  i       tDj      tt ..         G#E      t     
                                  fE            
                                   ,            

Best used in fullscreen (F11 in CMD/Terminal)

Made by Arran (github: Epicinver)
Feel free to check out some other shit i made



    '''
    return thumb


def warning():
        thumb = '''

                                                
                                          :     
                    ,;L.                 t#,    
                  f#i EW:        ,ft    ;##W.   
                .E#t  E##;       t#E   :#L:WE   
  :KW,      L  i#W,   E###t      t#E  .KG  ,#D  
   ,#W:   ,KG L#D.    E#fE#f     t#E  EE    ;#f 
    ;#W. jWi:K#Wfff;  E#t D#G    t#E f#.     t#i
     i#KED. i##WLLLLt E#t  f#E.  t#E :#G     GK 
      L#W.   .E#L     E#t   t#K: t#E  ;#L   LW. 
    .GKj#K.    f#E:   E#t    ;#W,t#E   t#f f#:  
   iWf  i#K.    ,WW;  E#t     :K#D#E    f#D#;   
  LK:    t#E     .D#; E#t      .E##E     G#t    
  i       tDj      tt ..         G#E      t     
                                  fE            
                                   ,            

        '''
        for line in thumb.splitlines():
            retardprint(True, line)
        retardprint(True, "This function may be dangerous. Press enter to continue.")
        input()
