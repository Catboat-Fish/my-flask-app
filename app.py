from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/intake', methods=['GET', 'POST'])
def intake():
    if request.method == 'POST':
        intake = request.form.get('intake') # takes intake from the page
        return f"Your input was the following: {intake}" # intake output
    return render_template('intake.html') # normal page

if __name__ == "__main__":
    app.run(debug=True)