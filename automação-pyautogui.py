import pyautogui as pa
import time
pa.alert('programa entrando em execução, não faça  nada')
time.sleep(3)
pa.press('winleft')
time.sleep(5)
pa.write('firefox')
time.sleep(3)
pa.press('enter')
time.sleep(3)
pa.write('https://drive.google.com/drive/u/1/')
time.sleep(3)
pa.press('enter')
time.sleep(10)
#entrar na area de trabalho usando um atalho com o hotkey
pa.hotkey('winleft','d')
#vai para  o arquivo seleciona  e arrasta para 
pa.moveTo(1306, 42)
time.sleep(2)
pa.mouseDown(1306,42)
pa.moveTo(737,451)
time.sleep(2)
pa.hotkey('winleft','d')
time.sleep(2)
pa.mouseUp(737,451)
time.sleep(2)

pa.alert('o codigo foi executado')

