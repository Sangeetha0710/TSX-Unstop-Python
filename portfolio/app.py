from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', name="Sangeetha K", intro="Passionate software developer with a strong foundation in Python, web technologies, and a drive to build innovative and impactful digital solutions.")

@app.route('/projects')
def projects():
    project_list = [
        {"name": "Dormigo", "description": "A full-stack accommodation booking platform connecting users and property owners with secure rental agreements and verification systems."},
        {"name": "Sepsis Detector", "description": "A machine learning project designed to predict the likelihood of sepsis in patients using clinical data."},
        {"name": "Destination Duo", "description": "A wheelchair-accessible route planning app that guides users through ramps, paths, and public transport connectivity."},
        {"name": "Tic-Tac-Toe", "description": "A fun and interactive browser-based game implemented using HTML, CSS, and JavaScript."},
        {"name": "Stopwatch", "description": "A functional and stylish stopwatch web app with start, stop, and reset capabilities."},
        {"name": "Portfolio", "description": "My personal responsive portfolio built with Flask and styled professionally to showcase my journey and skills."}
    ]
    return render_template('projects.html', projects=project_list)

@app.route('/internships')
def internships():
    internships = [
        {"company": "Prodigy Infotech", "role": "Web Developer Intern", "description": "Built responsive web applications, enhanced UI/UX design, and contributed to real-time collaborative projects."},
        {"company": "Techsonix Solutions", "role": "Python Developer Intern", "description": "Worked on automation scripts, handled backend API logic, and collaborated in team sprints."}
    ]
    return render_template('internships.html', internships=internships)

@app.route('/skills')
def skills():
    skills = ["Python", "Flask", "HTML5", "CSS3", "JavaScript", "Bootstrap", "Firebase", "MySQL", "Git", "Figma", "Responsive Design", "Problem Solving", "Team Collaboration"]
    return render_template('skills.html', skills=skills)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash('Message sent successfully!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)