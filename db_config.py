from flask_mysqldb import MySQL

def init_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'password'  # replace with your MySQL password
    app.config['MYSQL_DB'] = 'studentdb'
    return MySQL(app)
