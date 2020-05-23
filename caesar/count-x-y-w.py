# Számoljuk össze (egy megírt program segítségével) hányszor szerepel a szövegben az X, Y és # W karakter. 
# Az eredmény: X_száma + Y_száma - W_száma

with open('count-x-y-w.txt') as file:
  x =  y = w = 0
  for line in file:
    for char in line:
      if char == 'X':
        x += 1
      elif char == 'Y':
        y += 1
      elif char == 'W':
        w += 1

print(x + y - w) 
