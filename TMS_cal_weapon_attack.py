def cal_weapon_atk(p):
  plus_atk = int(sum_atk/50+1)
  a = p + plus_atk
  return a
while(True):
  level = input("請輸入武器等級(160or200)按0結束:")
  if level == '0':
    break
  ori = int(input("請輸入武器原始(魔法)攻擊力(白字):"))
  b , v , x , r , g = map(int, input("請輸入衝捲張數，依序為b,v,x,r,g:").split())
  sum_atk = ori + b*14 + v*13 + x*12 + r*10 +g*9
  star = int(input("請輸入星力數:"))
  if level == '160':
    for i in range(1,star+1):
      if(i<=15):
        sum_atk = cal_weapon_atk(sum_atk)
      elif(i == 16):
        sum_atk = sum_atk + 9
      elif(i == 17):
        sum_atk = sum_atk + 9
      elif(i == 18):
        sum_atk = sum_atk + 10
      elif(i == 19):
        sum_atk = sum_atk + 11
      elif(i == 20):
        sum_atk = sum_atk + 12
      elif(i == 21):
        sum_atk = sum_atk + 13
      elif(i == 22):
        sum_atk = sum_atk + 14
      elif(i == 23):
        sum_atk = sum_atk + 32
  elif level == '200':
    for i in range(1, star+1):
      if(i <= 15):
        sum_atk = cal_weapon_atk(sum_atk)
      elif(i == 16):
        sum_atk = sum_atk + 13
      elif(i == 17):
        sum_atk = sum_atk + 13
      elif(i == 18):
        sum_atk = sum_atk + 14
      elif(i == 19):
        sum_atk = sum_atk + 14
      elif(i == 20):
        sum_atk = sum_atk + 15
      elif(i == 21):
        sum_atk = sum_atk + 16
      elif(i == 22):
        sum_atk = sum_atk + 17
      elif(i == 23):
        sum_atk = sum_atk + 34
  else:
    print("還沒做。")
  sum_atk = sum_atk - ori
  print("最右邊藍字(魔法)攻擊力加成應為: "+str(sum_atk))
  print('\n')


