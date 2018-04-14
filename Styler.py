# http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# ^^^ for color list

from colorama import Fore as fg
from colorama import Back as bg
from colorama import Style, init

# Color: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

END = Style.RESET_ALL + fg.RESET + bg.RESET
ENDL = END + "\n"

Style.BOLD = "\033[1m"
Style.ITALIC = "\033[3m"
Style.UNDERLINE = "\033[4m"
Style.STRIKE = "\033[9m"

Style.BOLD2 = bg.RED
Style.ITALIC2 = fg.MAGENTA
Style.UNDERLINE2 = fg.RED
Style.STRIKE2 = Style.DIM + fg.BLACK + bg.BLACK

# string repeat
def sRep(char, times):
   string = ""
   for i in range(0, times):
      string += char
   return string

class Styler:
   def __init__(self, styling = 'auto'):
      self.baseH = Style.BRIGHT + bg.WHITE + fg.BLUE

      self.styling = styling
      if (styling == 'auto'):
         self.baseH += Style.BOLD

      init()
      

   def h1(self, msg =""):
      form = self.baseH 
      sep = sRep(" ", 8) 
      h = sep + msg + sep 
      line = sRep("*", len(h))
      return form + line + ENDL + form + h + ENDL + form + line + END
   
   def h2(self, msg =""): 
      form = self.baseH + Style.NORMAL
      sep = sRep(" ", 6) 
      h = sep + msg + sep 
      line = sRep("=", len(h))
      return form + line + ENDL + form + h + ENDL + form + line + END
   
   def h3(self, msg =""): 
      form = self.baseH + Style.DIM
      sep = sRep(" ", 4) 
      h = sep + msg + sep 
      line = sRep("+", len(h))
      return form + line + ENDL + form + h + ENDL + form + line + END
   
   def h4(self, msg =""): 
      form = self.baseH + fg.MAGENTA
      sep = sRep(" ", 4) 
      h = sep + msg + sep 
      line = sRep("-", len(h))
      return form + line + ENDL + form + h + ENDL + form + line + END
   
   def h5(self, msg =""): 
      form = self.baseH + fg.MAGENTA + Style.NORMAL
      sep = sRep(" ", 2) 
      h = sep + msg + sep 
      line = sRep("-", len(h))
      return form + line + ENDL + form + h + ENDL + form + line + END
   
   def h6(self, msg =""): 
      form = self.baseH + fg.MAGENTA + Style.DIM
      sep = " " 
      h = sep + msg + sep 
      line = sRep("-", len(h))
      return form + line + ENDL + form + h + ENDL + form + line + END
   

   def b(self, msg =""):
      if (self.styling == 'auto'): 
         return Style.BOLD + msg + END
      else:
         return Style.BOLD2 + msg + END
      
   def i(self, msg =""):
      if (self.styling == 'auto'): 
         return Style.ITALIC + msg + END
      else:
         return Style.ITALIC2 + msg + END
      
   def u(self, msg =""):
      if (self.styling == 'auto'): 
         return Style.UNDERLINE + msg + END
      else:
         return Style.UNDERLINE2 + msg + END

   
   def strike(self, msg =""):
      if (self.styling == 'auto'): 
         return Style.STRIKE + msg + END
      else:
         return Style.STRIKE2 + msg + END
   
   def line(self, length = 80, char = "-"):
      return sRep(char, length)


if __name__ == "__main__":
   S = Styler()

   print(S.h1("This is an H1 tag"))
   print(S.h2("This is an H2 tag"))
   print(S.h3("This is an H3 tag"))
   print(S.h4("This is an H4 tag"))
   print(S.h5("This is an H5 tag"))
   print(S.h6("This is an H6 tag"))

   print(S.b("This is bold"))
   print(S.i("This is italic"))
   print(S.u("This is underlined"))
   print(S.strike("This is stricken through"))
   print("This is normal")

   S = Styler(styling='other')

   print(S.h1("This is an H1 tag"))
   print(S.h2("This is an H2 tag"))
   print(S.h3("This is an H3 tag"))
   print(S.h4("This is an H4 tag"))
   print(S.h5("This is an H5 tag"))
   print(S.h6("This is an H6 tag"))

   print(S.b("This is bold"))
   print(S.i("This is italic"))
   print(S.u("This is underlined"))
   print(S.strike("This is stricken through"))
   print("This is normal")
