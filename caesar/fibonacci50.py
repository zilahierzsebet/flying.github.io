# Az ötvenedik fibonacci szám legmagasabb helyiértékű számjegye kivonva a legkisebb
# helyiértéküből. Ha a nulladik: 0, az első: 1.

def fibonacciRek(x):
  if x == 0 or x == 1:
    return x
  else:
    return (fibonacciRek(x-1) + fibonacciRek(x-2))

def fibonacciLin(x):
  Fib = 0
  prev = 1
  next = 0
  for i in range(0, x):
    next = Fib + prev
    prev = Fib
    Fib = next

  return str(Fib)

strFib = fibonacciLin(50)
print(int(strFib[-1]) - int(strFib[0]))
