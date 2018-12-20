def replaceLetters(str):
  str = str.replace("Aa", "")
  str = str.replace("aA", "")
  str = str.replace("Bb", "")
  str = str.replace("bB", "")
  str = str.replace("cC", "")
  str = str.replace("Cc", "")
  str = str.replace("dD", "")
  str = str.replace("Dd", "")
  str = str.replace("eE", "")
  str = str.replace("Ee", "")
  str = str.replace("fF", "")
  str = str.replace("Ff", "")
  str = str.replace("gG", "")
  str = str.replace("Gg", "")
  str = str.replace("hH", "")
  str = str.replace("Hh", "")
  str = str.replace("iI", "")
  str = str.replace("Ii", "")
  str = str.replace("jJ", "")
  str = str.replace("Jj", "")
  str = str.replace("kK", "")
  str = str.replace("Kk", "")
  str = str.replace("lL", "")
  str = str.replace("Ll", "")
  str = str.replace("mM", "")
  str = str.replace("Mm", "")
  str = str.replace("nN", "")
  str = str.replace("Nn", "")
  str = str.replace("oO", "")
  str = str.replace("Oo", "")
  str = str.replace("pP", "")
  str = str.replace("Pp", "")
  str = str.replace("qQ", "")
  str = str.replace("Qq", "")
  str = str.replace("rR", "")
  str = str.replace("Rr", "")
  str = str.replace("sS", "")
  str = str.replace("Ss", "")
  str = str.replace("tT", "")
  str = str.replace("Tt", "")
  str = str.replace("uU", "")
  str = str.replace("Uu", "")
  str = str.replace("vV", "")
  str = str.replace("Vv", "")
  str = str.replace("Ww", "")
  str = str.replace("wW", "")
  str = str.replace("xX", "")
  str = str.replace("Xx", "")
  str = str.replace("yY", "")
  str = str.replace("Yy", "")
  str = str.replace("zZ", "")
  str = str.replace("Zz", "")

  str = "".join(str.split()) #remove white spaces

  return str

def removeLetter(str, letter):
  #remove letter and compare
  small = letter.lower()
  big = letter.upper()
  str = str.replace(small, "")
  str = str.replace(big, "")
  str = "".join(str.split())
  return str

def fullyReact(str):
  str_len = len(str)


  print(len(str))
  prev_len = len(str)

  str = replaceLetters(str)

  print(len(str))

  post_len = len(str)

  while(True):
    if(prev_len > post_len):
      prev_len = post_len
      str = replaceLetters(str)
      post_len = len(str)

    else:
      # print("post_len", post_len)
      # print('str ', str)
      print("stopping")
      break

  print("post_len", post_len)
  return post_len

def start():
  abc = 'abcdefghijklmnopqrstuvwxyz'
  inputs = ""
  with open('./day5-input.txt') as f:
    inputs = f.readlines()

  print(len(inputs[0]))

  str = inputs[0]
  dict = {}
  # str_a = removeLetter(str, "a")
  # print(str_a)
  for i in range(0, len(abc)):
    letter = abc[i]
    len_letter = fullyReact(removeLetter(str, letter))
    dict[letter] = len_letter

  print(dict)

start()
