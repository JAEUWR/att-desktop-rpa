import time
import pyautogui as pg
import pyperclip

class CRMController:
    @staticmethod
    def buscar_numero(numero):
        """Secuencia de búsqueda en el CRM."""
        pyperclip.copy(numero)
        time.sleep(1)
        pg.click(708, 118)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')
        time.sleep(10)
        pg.click(807, 140)
        time.sleep(1)
        pg.click(933, 141)
        time.sleep(0.5)
        pg.doubleClick(70, 268)
        time.sleep(9)
        pg.press('enter')
        pg.click(799, 472)
        time.sleep(3)

    @staticmethod
    def limpiar_y_resetear():
        """Secuencia completa de limpieza de pantalla tras procesar."""
        pg.click(1416, 140)
        time.sleep(1)
        pg.click(1416, 140)
        time.sleep(1)
        pg.press('enter')
        time.sleep(1)
        pg.press('right')
        time.sleep(1)
        pg.press('enter')
        pg.click(1416, 140)
        time.sleep(1)
        pg.click(1416, 140)
        time.sleep(1)
        pg.press('enter')
        time.sleep(1)