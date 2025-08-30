# MSSP Alert Top 250 Scraper (2024) con Playwright



![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)
![Scraping](https://img.shields.io/badge/Data-Scraping-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)


---

📝 Descripción

Este proyecto es un web scraper en Python que utiliza Playwright para extraer la lista completa de las Top 250 MSSPs (Managed Security Service Providers) 2024 publicada en MSSP Alert.
El script navega por las 26 páginas del ranking y guarda la información en un archivo CSV estructurado con las siguientes columnas:

🏆 Rank

🏢 Nombre de la empresa

🔗 URL

🌍 Ubicación

📝 Descripción


Resultado: msspalert_top250_2024.csv

---

⚡ Instalación y uso

# Clonar el repo
git clone https://github.com/TU_USUARIO/msspalert-scraper.git
cd msspalert-scraper

# Crear entorno virtual
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

# Instalar dependencias
pip install playwright

# Instalar navegadores de Playwright
playwright install

# Ejecutar el scraper
python msspalert_scrappingPlaywright.py


---

📂 Archivos principales

msspalert_scrappingPlaywright.py → Script del scraper.

msspalert_top250_2024.csv → Salida con los datos estructurados.



---

📜 Licencia

Mi proyecto está bajo la licencia MIT – libre para uso y modificación.
