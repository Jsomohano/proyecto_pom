# Proyecto de Automatización con Selenium y Pytest

Este proyecto implementa pruebas automatizadas usando Selenium, Pytest y el patrón Page Object Model (POM). Incluye integración con Allure para reportes y logging centralizado.

## Requisitos

- Python 3.8 o superior
- Google Chrome (para pruebas con ChromeDriver)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd proyecto_POM
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Mac/Linux:
   source .venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

```
proyecto_POM/
│
├── pages/           # Clases Page Object Model
├── test/            # Tests automatizados
├── utils/           # Utilidades (logger, helpers, etc.)
├── requirements.txt
└── README.md
```

## Ejecución de Pruebas

Ejecuta todos los tests:
```bash
pytest
```

Ejecuta solo los tests marcados como "smoke":
```bash
pytest -m "smoke"
```

## Reportes Allure

1. Ejecuta las pruebas generando resultados para Allure:
   ```bash
   pytest --alluredir=allure-results
   ```

2. Visualiza el reporte:
   ```bash
   allure serve allure-results
   ```

## Logging

Los logs se integran en los reportes de Allure y también pueden verse en consola.

---

**¡Contribuciones y sugerencias son bienvenidas!**