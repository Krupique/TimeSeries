import statsmodels.api as sm

class Preditor:
    
    
    def __init__(self, df, x, periodiocity):
        # Cria o Modelo SARIMA
        self.modelo = sm.tsa.statespace.SARIMAX(df[x],
                                                order = (1, 2, 1),
                                                #seasonal_order = (2, 1, 0, 15),
                                                seasonal_order = (2, 1, 0, int(periodiocity)),
                                                enforce_stationarity = False,
                                                enforce_invertibility = False)

        # Treinamento (Fit) do modelo
        self.modelo_fit = self.modelo.fit()


    
    def predict(self, period = 7):
        fc = self.modelo_fit.forecast(steps=period)


        return fc