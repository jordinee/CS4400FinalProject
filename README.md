# CS4400FinalProject
How did I match my entities?

1.	read all the files in as dataframes
2.	turned model number columns into list so I can index them
3.	matched the model numbers between both tables
4.	cleared out empty columns (‘nan’)
5.	got the index of the matched model numbers for each table
6.	made the left’s index and right’s index into a tuple
7.	combined all the tuples, so I now have a list of the matched model numbers
8.	made sure all of the parts of the list were integers
9.	cleaned the train column by getting out only the matches
10.	compared my list to the train table, thus removing the similarities in them
11.	made the cleaned list into a dataframe 
12.	exported my dataframe to a csv file

Final Code: solutio.py
Final Output: myoutput.csv
