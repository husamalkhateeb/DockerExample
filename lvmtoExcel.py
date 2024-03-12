import sys
import os
import pandas as pd

def split_and_combine(input_file):
    data = pd.read_csv(input_file, sep="	", header=None)
    data.columns = ["sensorNumber", "data"]
    print(data)

    columns_full = ['Sensor_0', 'Data']

    for i in range (80):
        columns_full[0] = 'Sensor_' + str(i)
        columns_full[1] = 'Data_' + str(i)
        sensor = data[data['sensorNumber'] == i]
        sensor = sensor.dropna(axis=1)
        nparray = sensor.to_numpy()
        newDF = pd.DataFrame(nparray, columns=columns_full)
        newDF.to_csv(columns_full[0] + '.csv', index = False)
    
    dataframes = []

    # loop through each file
    for i in range(80):
        file_name = f"Sensor_{i}.csv"
        df = pd.read_csv(file_name)
        df.rename(columns={"Sensor_{}".format(i): "Sensor", "Data_{}".format(i): "Data"}, inplace=True)
        dataframes.append(df)

    # concatenate all DataFrames vertically
    result = pd.concat(dataframes, axis=1)
    result.to_csv("result.csv", index=False)
    pass

if __name__ == "__main__":
    input_file = sys.argv[1]


    split_and_combine(input_file)
