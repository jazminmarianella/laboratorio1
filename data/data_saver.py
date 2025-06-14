

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decouple import config

class DataSaver:
    def __init__(self):
        user = config('DB_USER')
        password = config('DB_PASS')
        host = config('DB_HOST')
        port = config('DB_PORT')
        database = config('DB_NAME')

        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(url)

    def guardar_dataframe(self, df, nombre_tabla):
        if df is None:
            print("No se puede guardar un Dataframe vacio para la tabla {nombre_tabla}")
            return
        if not isinstance(df, pd.DataFrame):
            print(f"El objeto proporcionado no es un DataFrame: {type(df)}")
            return
        
        try:
            df.to_sql(
                name=nombre_tabla,
                con=self.engine,
                if_exists='replace',  # Cambiar a 'append' para agregar datos a una tabla que ya existe
                index=False,
            )
        except SQLAlchemyError as e:
            print(f"Error al guardar el DataFrame en la base de datos: {e}")
            return
