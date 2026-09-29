import os
from flask import Flask, request, render_template




def create_app():
    app = Flask(__name__)

    #16KB limit
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024

    @app.route('/intake', methods=['GET', 'POST'])
    def intake():
        # fixes startup issues
        message = None
        error = None

        if request.method == 'POST':
            user_input = request.form.get('intake', '').strip()

            # error handling
            if not user_input: # if no valid input
                error = "Please enter a message."
            elif len(user_input) > 500: # max 500 characters, shouldn't be possible
                error = "Message is too long, must be 500 characters or fewer."
            else: # if no errors
                message = user_input

        return render_template(
            'intake.html', message=message, error=error
            )

    return app
            
app = create_app()

if __name__ == "__main__":
    # runs in debug mode
    app.run(
        debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    )