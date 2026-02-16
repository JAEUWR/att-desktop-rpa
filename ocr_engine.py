import cv2
import numpy as np
import pyautogui as pg
import pytesseract
import os
from dotenv import load_dotenv

load_dotenv()

class OCREngine:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_PATH')
        # Regiones definidas en el script original
        self.regiones = {
            "Fecha efectiva": (286, 440, 120, 17),
            "Fecha Inicio Plan": (630, 546, 161, 17),
            "Híbrido": (997, 167, 170, 17),
            "Aceleración": (1086, 600, 183, 17),
            "Saldo al Corte": (517, 64, 67, 15),
        }

    def _capturar_pantalla(self, region):
        """Captura la región y la prepara para el OCR."""
        screenshot = pg.screenshot(region=region)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        return img

    def extraer_datos(self):
        """Extrae el texto de todas las regiones."""
        datos = {}
        for campo, region in self.regiones.items():
            img = self._capturar_pantalla(region)
            texto = pytesseract.image_to_string(img, lang='eng')
            datos[campo] = texto.strip()
        return datos