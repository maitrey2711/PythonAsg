import pandas as pd
words = []
n = int(input())
for i in range(n):
  s = input()
  words.append(s)
  df = pd.value_counts(words)
  print(len(set(words)))
  print(df.values)
