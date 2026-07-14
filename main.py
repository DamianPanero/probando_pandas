import pandas as pd
from fastapi import FastAPI,HTTPException,Query

#instancia app
app=FastAPI()

#cargar el CSV
df=pd.read_csv("reactivos.csv")

#ENDPOINTS
#leer todos los reactivos
@app.get('/reactivos')
def get_reactivos():
    return df.to_dict(orient="records")

#filtrar reactivos por experimento
@app.get('/reactivos/filtrado')
def get_reactivo_por_exp(experimento_id:int=Query(...)):
    filtrado=df[df["experimento_id"]==experimento_id]
    if filtrado.empty:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron reactivos"
        )
    return filtrado.to_dict(orient="records")

#obtener un resumen de la cant de ml por experimento
@app.get('/reactivos/resumen')
def get_resumen():
    resumen=df.groupby("experimento_id")["cantidad_ml"].sum()
    if resumen.empty:
        raise HTTPException(
            status_code=404,
            detail="no hay datos cargados"
            )
    return resumen.reset_index().to_dict(orient="records")

#estadisticas
@app.get('/reactivos/estadisticas') #este me da internal error al correrlo
def estadisticas():
    return {
        "promedio_ml_por_exp":df.groupby("experimento_id")["cantidad_ml"].mean().reset_index().to_dict(orient="records"), #lo cambié
        "max_mililitros":int(df["cantidad_ml"].max()),
        "min_mililitros":int(df["cantidad_ml"].min()),
        "cantidad_elementos":len(df)
    }

#buscar por nombre exacto
@app.get('/reactivos/buscar')
def buscar_por_nombre(nombre:str=Query(...)):
    resultado=df[df["nombre"].str.lower()==nombre.lower()] 
    if resultado.empty:
        raise HTTPException(
            status_code=404,
            detail=f"no se encuentra el reactivo de nombre {nombre}"
        )
    return resultado.to_dict(orient="records")

#ordenar por mililitros
@app.get('/reactivos/ordenar')
def ordenar_por_ml():
    ordenado=df.sort_values("cantidad_ml",ascending=False)
    return ordenado.to_dict(orient="records")

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,port=8000,reload=True)
