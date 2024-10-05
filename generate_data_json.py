import pandas as pd

url_train_data = 'https://github.com/pukinidev/LabsBIData/blob/main/Lab1/202420_Laboratorio%201%20-%20Regresi%C3%B3n_train_data.csv?raw=true'

data_original = pd.read_csv(url_train_data, sep=',', encoding='UTF-8')

json_file_path = 'assets/data.json'
data_original.to_json(json_file_path, orient='records')

data_half = data_original.iloc[:len(data_original) // 2]

json_half_file_path = 'assets/data_half.json'
data_half.to_json(json_half_file_path, orient='records')

