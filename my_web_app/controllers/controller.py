from app import app
@app.route ('/<name>') #ADDED
def greet(name): #ADDED
    return f"Hi {name}!" #ADDED