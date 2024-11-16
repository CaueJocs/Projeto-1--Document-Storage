import psycopg2
#Arquivo para poder fazer o connect no banco.

def connection():
    conn = psycopg2.connect(database = "defaultdb", 
                            user = "cauejaco", 
                            host= 'proj-banco-9834.7tc.aws-eu-central-1.cockroachlabs.cloud',
                            password = "OeJU0OabjaNUp-4QwYRkmw",
                            port = 26257)
    return conn

