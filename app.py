from flask import Flask, render_template, send_from_directory, abort
import json
import os
from datetime import datetime

app = Flask(__name__)

def load_projects():
    try:
        with open(os.path.join(app.root_path, 'data', 'projects.json'), 'r') as f:
            projects = json.load(f)
        return projects
    except Exception as e:
        print(f"Error loading projects.json: {e}")
        return []

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = load_projects()
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    projects = load_projects()
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        abort(404)
    return render_template('project.html', project=project)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/resume/download')
def download_resume():
    try:
        return send_from_directory('static', 'resume.pdf', as_attachment=True)
    except Exception:
        abort(404)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
