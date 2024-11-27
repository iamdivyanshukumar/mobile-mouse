from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Serve the frontend HTML
@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is in the templates folder

# Handle mouse movement
@socketio.on('move_mouse')
def handle_move_mouse(data):
    # Data contains the scaled X and Y position of the mouse
    print(f"Mouse moved to: x={data['x']}, y={data['y']}")
    # You can implement logic to move the actual system mouse here if needed

# Handle scrolling
@socketio.on('scroll')
def handle_scroll(data):
    # Data contains the scroll deltaY value
    print(f"Scrolling: deltaY={data['deltaY']}")
    # You can implement custom scroll behavior here, such as simulating a browser scroll action

# Handle left and right click
@socketio.on('click')
def handle_click(data):
    # Data contains the mouse position and the button clicked (left or right)
    print(f"Mouse click at: x={data['x']}, y={data['y']} with button={data['button']}")
    # You can simulate the click or trigger specific events based on the button and coordinates

if __name__ == '__main__':
    # Run the app on localhost with debugging enabled
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
