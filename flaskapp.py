from flask import Flask, render_template
import random
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Generate some random data for the graph
    x = list(range(1, 11))
    y = [random.randint(1, 100) for _ in x]

    # Create a plot
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title('Random Data Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    graph_path = 'static/graph.png'
    plt.savefig(graph_path)
    plt.close()

    return f'''
    <html>
        <body>
            <h1>Graph Display</h1>
            <img src="{graph_path}" alt="Random Data Graph">
        </body>
    </html>
    '''

if __name__ == '__main__':
    # Make sure the "static" folder exists for saving the graph image
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
