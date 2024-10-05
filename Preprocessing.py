from sklearn.base import BaseEstimator, TransformerMixin

def calcular_valores_atipicos(data, columna):
    q1 = data[columna].quantile(0.25)
    q3 = data[columna].quantile(0.75)
    iqr = q3 - q1

    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)

    va_df = data.loc[(data[columna] > limite_superior) |
                     (data[columna] < limite_inferior)]
    return va_df


class Preprocessing(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X['Duracion_KTAS_Min'] = X['Duracion_KTAS_Min'].apply(
            lambda x: float(str(x).replace(',', '.')))

        X.loc[X.Modo_Llegada.isin([6, 7]), 'Modo_Llegada'] = 5

        columnas_atipicas = ['Duracion_Estancia_Min', 'DBP', 'HR', 'SBP']
        indices_a_eliminar = set()

        for columna in columnas_atipicas:
            atipicos = calcular_valores_atipicos(X, columna)
            indices_a_eliminar = indices_a_eliminar.union(atipicos.index)

        indices_a_eliminar = indices_a_eliminar.intersection(X.index)
        X.drop(indices_a_eliminar, inplace=True)

        features = ["Grupo", "Sexo", "Modo_Llegada", "Lesion", "Estado_Mental",
                    "KTAS_experto", "Duracion_KTAS_Min", "Edad", "Duracion_Estancia_Min"]
        X.drop_duplicates(features, inplace=True)
        X.dropna(subset=features, inplace=True)

        col_to_delete = ["Queja_Principal", "Diagnostico_En_Urgencias", "Disposicion",
                         "Grupo_De_Error", "Error_Triaje", "SBP", "RR", "Dolor",
                         "DBP", "HR", "BT", "Saturacion", "KTAS_enfermera", "dolor_NRS"]
        X.drop(col_to_delete, axis=1, inplace=True)
        return X