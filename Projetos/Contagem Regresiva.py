import time
import emoji

print ('Contagem regressiva')
emoji_fogos = emoji.emojize(":fireworks:")
for contador in range(10,0,-1):
  time.sleep(1)
  print(contador)
print(emoji_fogos)
