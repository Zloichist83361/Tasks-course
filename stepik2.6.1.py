day = int(input())
sup = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
for i in range(day):
  print(sup[i % len(sup)])