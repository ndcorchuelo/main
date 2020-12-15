import pandas as pd
import pyodbc as conn_d
from common import config

parameters = config()['source']

class database:
    """ Connection class to source and target databases """

    def __init__(self):
        self.driver_source =   parameters['driver_source']
        self.database_source = parameters['database_source']
        self.host_source =     parameters['host_source']
        self.port_distination =parameters['port_distination']
        self.user_source =     parameters['user_source']
        self.password_source=  parameters['password_source']
        self.trusted_connection = parameters['trusted_connection']

    def __source__connect__(self):
        self.conn_source = conn_d.connect(
             Driver = self.driver_source
            ,Server = self.host_source
            ,Database = self.database_source
            ,user = self.user_source
            ,Trusted_Connection = self.trusted_connection
            ,password = self.password_source)
        self.cur_des = self.conn_source.cursor ()

    def __disconnect_source__(self):
        self.conn_source.close()

    def __execute__(self, sql):
        self.__source__connect__()
        #self.cur_des.execute(sql)
        dataframe = pd.read_sql_query(sql,self.conn_source)
        #self.cur_des.commit()
        self.__disconnect_source__()
        return dataframe