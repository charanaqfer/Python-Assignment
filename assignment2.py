import csv
import unittest
class Format:
    def __init__(self,name) -> None:
        self.name=name
class CSV(Format):
    def __init__(self, name,filename,delimiter) -> None:
        super().__init__(name)
        self.filename=filename
        self.delimiter=delimiter
        self.validity_check=self.check()
    def check(self):
        file_type=self.name.split('.')
        if len(file_type)>1 and file_type[-1]=='csv':
            try:
                with open(self.filename, 'r', newline='') as csvfile:
                    csv_reader = csv.reader(csvfile, delimiter=self.delimiter)

                    # Get the header to determine the number of columns
                    self.header = next(csv_reader)
                    expected_columns = len(self.header)
                    self.row_count=0
                    # Check if every row has the same number of columns as the header
                    for row in csv_reader:
                        if len(row) != expected_columns:
                            # print(f"Error: Inconsistent number of columns in the CSV file.")
                            return False
                        self.row_count+=1
                    # If no exception is raised and every row has the same number of columns, consider the CSV file valid
                    return True
            except (csv.Error, FileNotFoundError) as e:
                print(f"Error reading CSV file: {e}")
                return False
        return False    
    def isvalid(self):
        if self.validity_check:
            print("valid csv file")
            return True
        else:
            print("Not valid csv file")
            return False
    def get_header(self):
        if self.validity_check:
            print(f"Header:{self.header}")
            return self.header
        else:
            print("Invalid csv")
            return False
    def get_row_count(self):
        if self.validity_check:
            print(f"num of rows:{self.row_count}")
            return self.row_count
        else:
            print("Invalid csv")
            return False


class UnitTestClass(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.path1='/Users/charankumarrampelli/Python_assignment/assgn2.csv'
        self.path2='/Users/charankumarrampelli/Python_assignment/assgn2_invalid.csv'
        self.file1=CSV('assign2.csv',self.path1,',') # True
        self.file2=CSV('assgn2.csv',self.path2,',')# False
        self.file3=CSV('assgn2.csv',self.path2,';')#False
        self.file4=CSV('assgn2.txt',self.path1,';')#False
        self.file5=CSV('assgn2.csv',self.path1,';')#True
    
    def test_isvalid(self):
        # result=self.file1.isvalid()
        # print(result)
        self.assertTrue(self.file1.isvalid())
        self.assertFalse(self.file2.isvalid())

    def test_get_header(self):
        self.assertEqual(self.file1.get_header(),['Name','Age','Score','Grade'])
        self.assertEqual(self.file5.get_header(),['Name,Age,Score,Grade'])

    def test_get_row_count(self):
        self.assertEqual(self.file1.get_row_count(),10)
        self.assertEqual(self.file5.get_row_count(),10)
if __name__=='__main__':
    unittest.main()