# AT&T Legacy CRM - Desktop Automation (OCR) 

### Descripción
Solución RPA de escritorio diseñada para interactuar con CRMs heredados (Legacy) que no poseen API o interfaz web accesible. Utiliza técnicas de Visión Artificial para la extracción de datos sensibles de clientes.

### Key Features
- **Computer Vision:** Implementación de OCR con **Tesseract** y pre-procesamiento de imágenes con **OpenCV** (Grayscale & Thresholding).
- **GUI Control:** Automatización precisa de mouse y teclado mediante PyAutoGUI.
- **Multi-threading:** Manejo de estados de ejecución en hilos separados para mantener la capacidad de respuesta del bot.
- **Data Sync:** Sincronización automática de resultados con bases de datos en la nube.

### Stack
- Python
- OpenCV / PyTesseract
- PyAutoGUI
- Threading