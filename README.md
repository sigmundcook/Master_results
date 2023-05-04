# Master_results
Scripts which were used to extract data from students exam submissions during 2021 and 2022 exams

In order to run the scripts, the user must run the extract python files in their respective folder. This ensures that the code in the csv files are extracted to the correct folders and that the unittests can locate the files correctly.

After extracting, run the test file in their respective folders to perform unittests on the newly created python files. In some cases the students python files will ask the user for inputs, this can be skipped by pressing enter, as the inputs are already defined by the test. This could in the future be solved by creating mock input which will automatically much user input in python, but is not time beneficial to implement as the tests only need to be run one time to gather the data, and the amount of times the user is asked for input is not large. 

The tests need to be ran in linux as the script uses os functions in order to time out the test if a student has written code that contains an infinite loop.

The data jupyter notebook is used to gather the data from the log files and summarises and groups the data into logical groups which have been used in the tables of the raport.
