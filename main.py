import os
import pandas as pd
import numpy as np

def add_key(df):
    total_rows = len(df)
    percent_threshold = 10
    log_percent = total_rows // percent_threshold  # integer division
    cur_percent = 0
    print('Total rows: ' + str(total_rows))
    for index, row in df.iterrows():
        # log status
        if index % log_percent == 0:
            print('File at: ' + str(cur_percent) + '%')
            cur_percent += percent_threshold
        if pd.isnull(row['Full Name with Id']):
            if pd.isnull(row['Id']):
                row['key'] = ''
            elif pd.isnull(row['Full Name']):
                if pd.isnull(row['First Name']) and pd.isnull(row['Last Name']):
                    row['key'] = ''
                else:
                    df.at[index, 'key'] = (str(row['Id']) +
                                           str(row['First Name']) + str(row['Last Name'])).replace(" ", "").lower()
            else:
                df.at[index, 'key'] = (str(row['Id']) + str(row['Full Name'])).replace(" ", "").lower()
        else:
            df.at[index, 'key'] = (str(row['Full Name with Id'])).replace(" ", "").lower()

def step_files(directory, ordered_folder):
    #Define column order here
    column_order = ['DocName',
                'Full Name with Id',
                'Full Name',
                'First Name',
                'Middle Name',
                'Last Name',
                'Id',
                'DOB',
                'Full Address',
                'Address 1',
                'Address 2',
                'City',
                'State',
                'Zip Code',
                'SSN',
                'Clinic',
                'Doctor',
                'Medical',
                'Internal Note',
                'Comment 1',
                'Comment 2',
                'Diagnosis 1',
                'Diagnosis 2',
                'Deceased',
                'City State Zip',
                'Drivers']
    #for each csv in chosen folder
    i = 1
    for entry in os.scandir(directory):
        if (entry.path.endswith(".csv")
        and entry.is_file()):
            print('File processing:  ' + entry.path)
            # Read csv / tab-delimited in this example
            df = pd.read_csv(entry.path,
                             low_memory=False,
                             dtype={'Id': str}) #low memory=False sliences error related to Pandas having to guess data types

            #print(df)
            #We should add empty columns if they don't exist
            #df["key"] = df["key"].astype(str)

            for col in column_order:
                if col not in df.columns:
                    df[col] = np.nan
            #sets columnn order

            df = df[column_order]
            #df["Id"] = df["Id"].astype(round)
           # df["Full Name with Id"] = df["Full Name with Id"].astype(str)
           # df["First Name"] = df["First Name"].astype(str)
           # df["Last Name"] = df["First Name"].astype(str)
           # df["Full Name"] = df["Full Name"].astype(str)

            add_key(df)



           # df['xy'] =  df['Id'].astype(str) +   df['Full Name'].astype(str)
            #print(df)
            # Write csv / tab-delimited
            df.to_csv(ordered_folder + '\\ordered_excel' + str(i) + '.csv')
            print('File created:  ' + ordered_folder + '\\ordered_excel' + str(i) + '.csv')
            i += 1
            print('Files processed: ' + str(i - 1))


            # Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pd.set_option('precision', 0)
    main_folder = 'C:\\Users\\Justin Washburn\\Desktop\\excelOrder'
    ordered_folder = main_folder + '\\ordered_excel'
    try:
        os.mkdir(main_folder + '\\ordered_excel')
        print("Folder created at : " +  ordered_folder)
    except:
        print("Folder already exists - skipping creation")

    step_files(main_folder, ordered_folder)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
