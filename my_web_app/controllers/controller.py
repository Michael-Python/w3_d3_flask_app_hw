from app import app
@app.route ('/') #ADDED
def greet(name): #ADDED
    return f"Hello, {name}!" #ADDED