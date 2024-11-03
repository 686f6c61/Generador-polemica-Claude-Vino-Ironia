from flask import Flask, render_template, request
from argument_generator import ChristmasArgumentGenerator

app = Flask(__name__)
argument_generator = ChristmasArgumentGenerator()

@app.route('/', methods=['GET', 'POST'])
def index():
    argument_data = None
    if request.method == 'POST':
        target_person = request.form.get('target_person', '')
        topic = request.form.get('topic', '')
        intensity = request.form.get('intensity', 'moderada')
        position = request.form.get('position', 'favor')
        argument_data = argument_generator.generate_argument(target_person, topic, intensity, position)
    return render_template('index.html', argument_data=argument_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
