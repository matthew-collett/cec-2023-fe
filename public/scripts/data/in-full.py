import pandas as pd
import os
import json
import sys

def out(string: str) -> None:
    print(string)
    sys.stdout.flush()

table1 = "/Users/matthewcollett/Documents/Node/cec-2023-fe/public/scripts/data/table1.csv"
table2 = "/Users/matthewcollett/Documents/Node/cec-2023-fe/public/scripts/data/table2.csv"
table3 = "/Users/matthewcollett/Documents/Node/cec-2023-fe/public/scripts/data/table3.csv"

csv_files = [table1, table2, table3]
df_dict = {}

temp_csv_file = "temp.csv"
for csv_file in csv_files:
    with open(csv_file, 'r') as input_file, open(temp_csv_file, 'w') as output_file:
        data = input_file.read()
        data = data.replace(',', '')
        output_file.write(data)

    df = pd.read_csv(temp_csv_file, delimiter='|', skiprows=[0])
    df_dict[csv_file] = df

    # Delete temp file
    os.remove(temp_csv_file)

data1 = df_dict[table1]
data2 = df_dict[table2]
data3 = df_dict[table3]

conversionsCalc = {"second": 1/360,
                "minute": 1/60,
                "day": 24,
                "week": 168,
                "month": 722.4, 
                "year": 8760,
                "inch":  0.0254,
                "mile": 1609.34,
                "foot": 0.3048,
                "yard:": 0.9144,
                "kilometer": 1000,
                "milimeter": 0.001,
                "metric_ton": 1000,
                "pound": 0.453592,
                "gram": 0.001,
                "ton": 1000,
                "ounce": 0.0283495,
                "gallon": 0.00378541,
                "pint": 0.000473176,
                "cubic_centimeter": 0.000001,
                "cubic_centimeter": 0.0283168,
                "liter": 0.001, 
                "joule": 0.001, #energy
                }

length = ["inch","mile","foot","yard:","kilometer","milimeter"] #meter
time = ["second","minute","day","week","month", "year"] #hour
weight = ["metric_ton","pound","gram","ton","ounce"] #kg
volume = ["gallon","pint","cubic_centimeter","cubic_centimeter","liter"] # cubic meter
energy = ["joule"] # kj

def convert_units(df):
    conversionsCalc = {"second": 1 / 360,
                       "minute": 1 / 60,
                       "day": 24,
                       "week": 168,
                       "month": 722.4,
                       "year": 8760,
                       "inch": 0.0254,
                       "mile": 1609.34,
                       "foot": 0.3048,
                       "yard:": 0.9144,
                       "kilometer": 1000,
                       "milimeter": 0.001,
                       "metric_ton": 1000,
                       "pound": 0.453592,
                       "gram": 0.001,
                       "ton": 1000,
                       "ounce": 0.0283495,
                       "gallon": 0.00378541,
                       "pint": 0.000473176,
                       "cubic_centimeter": 0.000001,
                       "cubic_centimeter": 0.0283168,
                       "liter": 0.001,
                       "joule": 0.001,  # energy
                       }

    length = ["inch", "mile", "foot", "yard:", "kilometer", "milimeter"]  # meter
    time = ["second", "minute", "day", "week", "month", "year"]  # hour
    weight = ["metric_ton", "pound", "gram", "ton", "ounce"]  # kg
    volume = ["gallon", "pint", "cubic_centimeter", "cubic_centimeter", "liter"]  # cubic meter
    energy = ["joule"]  # kj

    for index, row in df.iterrows():
        if row['Unit'] in length:
            key = row['Unit']
            df.loc[index, 'Unit'] = 'meter'
        elif row['Unit'] in time:
            key = row['Unit']
            df.loc[index, 'Unit'] = 'hour'
        elif row['Unit'] in weight:
            key = row['Unit']
            df.loc[index, 'Unit'] = 'kilogram'
        elif row['Unit'] in volume:
            key = row['Unit']
            df.loc[index, 'Unit'] = 'cubic_meter'
        elif row['Unit'] in energy:
            key = row['Unit']
            df.loc[index, 'Unit'] = 'kilojoule'

        df.loc[index, 'Quantity'] = row['Quantity'] * conversionsCalc[key]

# Load .CSV
temp_csv_file = "temp.csv"
for csv_file in csv_files:
    with open(csv_file, 'r') as input_file, open(temp_csv_file, 'w') as output_file:
        data = input_file.read()
        data = data.replace(',', '')
        output_file.write(data)

    df = pd.read_csv(temp_csv_file, delimiter='|', skiprows=[0])
    df_dict[csv_file] = df
    # Delete temp file
    os.remove(temp_csv_file)


data1 = df_dict[table1]
data2 = df_dict[table2]
data3 = df_dict[table3]
data4 = pd.read_csv("/Users/matthewcollett/Documents/Node/cec-2023-fe/public/scripts/data/my_dataframe2.csv", delimiter=',')
data4 = data4.dropna()  # removes blank rows

data3sorted = data3.sort_values(["Resource", "Quantity"], ascending=[False, False])
data3sorted.to_csv('/Users/matthewcollett/Documents/Node/cec-2023-fe/public/scripts/data/my_dataframe.csv', index=False)

# Converts units to be standardized
convert_units(data1)
convert_units(data4)
convert_units(data3sorted)

# List of unique resource names
unique_resources = []
for value in data3sorted.iloc[:, 1].unique():
    unique_resources.append(value)

data4saved = data4
country_list = []  # saves list of countries
quantity_value_list = []  # quantity of donation
donation_value_list = []  # cost of donation


resource_cost_per_unit = data1['Total Value ($CAD)'] / data1['Quantity']
resource_cost_per_unit = resource_cost_per_unit.tolist()
resource_names_for_cost = data1.iloc[:, 0].tolist()

for resource_type in unique_resources:
    data4temp = data4saved

    # Loops through and allocates funds while tracking remaining resources available
    temp1 = 0  # Just for printing
    index1 = 0  # Index to delete rows after resource request allocated
    while not data4temp.empty:
        quantity_value = round(data4temp.iloc[0]['Quantity'])
        # access value
        total_resource_val_to_allocate = round(data1.loc[data1['Resource'] == resource_type, 'Quantity'].values[0])
        # update value
        if total_resource_val_to_allocate >= quantity_value:
            data1.loc[data1['Resource'] == resource_type, 'Quantity'] = (total_resource_val_to_allocate - quantity_value)
            quantity_value_list.append(quantity_value)
            index2 = resource_names_for_cost.index(resource_type)
            resource_cost = resource_cost_per_unit[index2]
            donation_value = quantity_value * resource_cost
            donation_value_list.append(donation_value)
        # Remove rows with the country in data4saved
        country = data4temp.iloc[0]['Country']
        country_list.append(country)
        data4temp = data4temp[data4temp['Country'] != country]
        data4saved = data4saved[data4saved['Country'] != country]
        temp1 = temp1 + quantity_value
        index1 = index1+1

donation_value_list = [round(i, 2) for i in donation_value_list]
# Write to .JSON for website
table_data = []
for i in range(len(country_list)):
    table_data.append([country_list[i], quantity_value_list[i], donation_value_list[i]])

data = {'tableHeader': ['Country', 'Resources By Sector', 'Money Received'], 'tableData': table_data}


if __name__ == '__main__':
    out(json.dumps(data))
