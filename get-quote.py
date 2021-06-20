def main():
  import random
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last= 13
  print(quotes[0,last])

if __name__== "__main__":
  main()
