import mysql.connector  #class need method of mysql.connector


class UseDatabase:

    def __init__(self, config: dict) -> None:  #identify 'config'(dict) as self.configuration
        self.configuration = config    
    
    def __enter__(self) -> 'cursor':    #connecting & make cursor
        self.conn = mysql.connector.connect(**self.configuration)  
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:   #commit change & close cursor and connection
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


