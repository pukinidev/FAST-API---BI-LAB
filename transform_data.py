import pandas as pd

url_train_data = 'https://github.com/pukinidev/LabsBIData/blob/main/Lab1/202420_Laboratorio%201%20-%20Regresi%C3%B3n_train_data.csv?raw=true'

data_original = pd.read_csv(url_train_data, sep=',', encoding='UTF-8')

data_as_json = data_original.to_dict(orient='list')

json_file_path = 'assets/data.json'
data_original.to_json(json_file_path, orient='records')
