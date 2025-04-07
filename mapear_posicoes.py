import pyautogui
import time

print("Posicione o mouse sobre o elemento e aguarde 2 segundos...")
print("Pressione Ctrl+C no terminal para parar")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição atual: X={x} Y={y}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nCaptura de posições encerrada")