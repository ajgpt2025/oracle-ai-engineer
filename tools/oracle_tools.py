import oracledb


class OracleDB:

    def __init__(self):

        self.connection = None

    def connect(
        self,
        user,
        password,
        host,
        port,
        service
    ):

        self.connection = oracledb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            service_name=service
        )

        return self.connection

    def execute(self, sql):

        cursor = self.connection.cursor()

        cursor.execute(sql)

        return cursor.fetchall()