# Keressük ki a file-ban a Z karakter után következő számjegy karatereket és az átlaguknak # # vegyük az egész részét.

with open('after-z.txt') as file:
  after = []
  for line in file:
    line = line.strip()
    for i in range(0, len(line)):
      if (line[i] == 'Z') and (i < len(line)-1) and (ord(line[i+1]) <= 57):
        after.append(ord(line[i+1])-48)

  print(sum(after) // len(after))