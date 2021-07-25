# SqlLoadFileIterate
Orders and attempts to create new key format for given folder of csv files.

## Imports
  ```
pip install pandas
  ```

## Requirements before run
1. Update folder location containing csv files:
  ```
  main_folder = 'C:\\Users\\Justin Washburn\\Desktop\\excelOrder'
   
```

## Considerations
1. Files are processed one at a time. If an issue is encountered on the 101st file, the previous 100 files will have been created in the subfolder. If you rerun the program the counter will start at 1 and reprocess all of the previous csvs. If you encounter an error on the 101st file: 
    - Remove the already processed files (the unordered, raw csv files) from your processing folder so they are not reprocessed.
    - Update the counter in the program so it does not rewrite the existing ordered csvs:
      ```
         i = 1 # could be changed to i = 101

      ```
