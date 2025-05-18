from src import create_app
server = create_app()
if "__main__" == __name__:
    server.run(debug=True)