def swapCase(s):
  output=''
  for char in s:
    if (char.isupper() == True):
      output += (char.lower())
      elif (char.islower() == True):
        output += (char.upper())
        else:
          output += char
          return output
        print(swapCase("Pythonist 2"))
