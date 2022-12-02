n = int(input('Задайте список из N элементов: ')) 
def sequence(n):
  return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))