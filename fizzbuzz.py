while(1):
      num=eval(input("输入一个整数:"))
      if num%3==0 and num%5==0:
            print("fizz buzz")
      elif num%3==0:
            print("fizz")
      elif num%5==0:
            print("buzz")
      else:
            print(num)
