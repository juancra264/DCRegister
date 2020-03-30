from app import create_app

# Setup Flask-Script with command line commands
app = create_app()

if __name__ == "__main__":
    app.run()
