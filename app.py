from flask import Flask, render_template, send_file, request, jsonify
import webbrowser
from animation_model import generate_animation_gif, update_robot_position

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/current_status')
def current_status():
    return render_template('current_status.html')

@app.route('/get_animation_gif')
def get_animation_gif():
    try:
        image_path = generate_animation_gif()
        return send_file(image_path, 
                        mimetype='image/png',
                        cache_timeout=0,
                        as_attachment=False)
    except Exception as e:
        print(f"Error generating image: {e}")
        return "Error generating image", 500

@app.route('/move_robot', methods=['POST'])
def move_robot():
    try:
        data = request.get_json()
        direction = data.get('direction', '')
        update_robot_position(direction)
        return jsonify({"status": "success"})
    except Exception as e:
        print(f"Error moving robot: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    webbrowser.open("http://localhost:5000")
    app.run(debug=True)
