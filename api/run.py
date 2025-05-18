from src import create_app
server = create_app()
if "__main__" == __name__:
    server.run(host="0.0.0.0",debug=True)