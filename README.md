# AT&T Legacy CRM - Desktop Automation (OCR)

### Descripción
Solución de automatización de procesos robóticos de escritorio diseñada para interactuar con sistemas CRM Legacy de AT&T que carecen de APIs o interfaces web accesibles. El sistema utiliza técnicas avanzadas de Visión Artificial para emular la interacción humana y extraer información crítica de la interfaz gráfica de usuario.

### Key Features
- **Computer Vision Pipeline:** Implementación de OCR con Tesseract Engine y pre-procesamiento de imágenes mediante OpenCV utilizando técnicas de escala de grises y umbralización binaria para maximizar la precisión de lectura.
- **Control de GUI de Alta Precisión:** Automatización de periféricos virtuales (mouse y teclado) mediante PyAutoGUI con lógica de coordenadas relativas para adaptabilidad.
- **Ejecución Multi-threading:** Gestión de estados y ciclos operativos en hilos de ejecución separados para evitar el bloqueo de la interfaz de usuario y permitir el monitoreo continuo.
- **Sincronización Cloud:** Persistencia automatizada de datos extraídos en bases de datos distribuidas mediante Google Sheets API.

### Stack
- Python
- OpenCV (Open Source Computer Vision Library)
- PyTesseract (OCR Engine)
- PyAutoGUI
- Threading Library