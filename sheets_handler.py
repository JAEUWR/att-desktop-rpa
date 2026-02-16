import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()

class SheetsHandler:
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('GOOGLE_CREDS_PATH'), scope)
        client = gspread.authorize(creds)
        
        # Apertura de hojas específicas
        self.hoja_cliente = client.open_by_key(os.getenv('CLIENT_SHEET_KEY')).worksheet("MAQUINA 3")
        self.hoja_global = client.open_by_key(os.getenv('GLOBAL_SHEET_KEY')).worksheet("COZUMEL3")

    def obtener_siguiente_numero(self):
        """Busca el primer número sin estatus en la hoja del cliente."""
        datos = self.hoja_cliente.get_all_records()
        for row in datos:
            if str(row.get("ESTATUS", "")).strip() == "":
                return row.get("NUMERO")
        return None

    def marcar_revisado(self, numero):
        """Marca el número como revisado en la hoja del cliente."""
        datos = self.hoja_cliente.get_all_records()
        for index, row in enumerate(datos):
            if str(row.get("NUMERO")) == str(numero) and str(row.get("ESTATUS", "")).strip() == "":
                self.hoja_cliente.update_cell(index + 2, 7, "REVISADO")
                break

    def enviar_a_global(self, datos_ocr, numero):
        """Sincroniza los datos extraídos con la hoja global y actualiza cliente."""
        # Formato de fila para la hoja global
        fila = [numero] + [datos_ocr.get(campo, "") for campo in datos_ocr if campo != "Numero"]
        self.hoja_global.append_row(fila)
        
        # Actualizar los datos también en la hoja del cliente
        datos_cliente = self.hoja_cliente.get_all_records()
        for index, row in enumerate(datos_cliente):
            if str(row.get("NUMERO")) == str(numero):
                for i, valor in enumerate(fila):
                    self.hoja_cliente.update_cell(index + 2, i + 1, valor)
                break