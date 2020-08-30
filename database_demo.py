import re
import pickle
import os

class DatabaseDemo:

    def __init__(self):
        self.query_table_list = []
        self.file_name = 'my_database'
        self.read_from_db()        

    def get_data(self,query):
        query_str = ".*" + query + ".*"
        query_regex = re.compile(query_str)
        result = list(filter(query_regex.match, self.query_table_list))
        if(len(result)<1):
            result = 'No recent matching query'
        return result

    def put_data(self,query):
        if(query not in self.query_table_list):
            self.query_table_list.append(query)
            self.write_to_db()
            self.read_from_db()

    def write_to_db(self):
        with open(self.file_name,'wb') as outfile:
            pickle.dump(self.query_table_list,outfile)

    def read_from_db(self):
        if(os.path.exists(self.file_name)):
            with open(self.file_name,'rb') as infile:
                self.query_table_list = pickle.load(infile)