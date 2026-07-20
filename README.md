**API REST para consulta y análisis de reactivos químicos. Procesa datos desde un archivo CSV usando Pandas y los expone como endpoints JSON**

### Tecnologías
- Python 3.11
- FastAPI
- Pandas
- Uvicorn

### ENDPOINTS
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/reactivos` | Lista todos los reactivos |
| GET | `/reactivos/filtrar` | Filtra por experimento |
| GET | `/reactivos/resumen` | Suma de mililitros por experimento |
| GET | `/reactivos/estadísticas` | Promedio, máximo, mínimo de mililitros |
| GET | `/reactivos/buscar?nombre=HCL` | Búsqueda por nombre exacto |
| GET | `/reactivos/ordenar` | Ordena por cantidad de mililitros

### Cómo correrlo
<!-- clonar el repositorio -->
git clone https://github.com/DamianPanero/probando_pandas
<!-- crear entorno virtual e instalar dependencias -->
pip install -r requeriments.txt
<!-- correr la app -->
uvicorn main:app --reload

### Estructura
├── main.py            # endpoints y lógica principal
├── reactivos.csv      # datos de ejemplo
├── requirements.txt   # dependencias
├── Dockerfile
└── docker-compose.yml