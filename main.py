from flask import Flask, request, jsonify
import pyvibe as pv

app = Flask(__name__)

@app.route('/')
def index():
    page = pv.Page('Home')

    page.navbar = pv.Navbar(
        title='My PyVibe test',
        logo='https://m.media-amazon.com/images/W/MEDIAX_792452-T1/images/I/'
        '61yLqkmcN9L._SL1500_.jpg',
    )
    page.add_header('My PyVibe test page')
    page.add_text(value = "Here's simple PyVibe + Flask test page")
    page.add_link(text = 'Heres a link, where you can see more', url = 'https://www.pycob.com')
    page.add_divider()

    page.add_header('A sample of code', size=2)
    with page.add_card() as card:
        card.add_code(
            value = """\nimport pyvibe as pv\n\npage = pv.Page()\npage.add_header("Welcome to PyVibe!")\npage.add_text("PyVibe is an open source Python library for creating UI components for web apps without the need to write HTML code.")
            """,
            header = 'Simple app example'
        )

        card.add_alert(text = "Isn't it pretty?", badge="INFO", color="indigo")

    page.add_divider()

    page.add_header('A sample form', size=2)

    with page.add_card() as card:
        card.add_header("PyVibe Survey Form Example", size=2)

        with card.add_form(method='POST', action="/save_opionion") as form:
            form.add_formtext(label="Name", name="name", placeholder="Enter your name")
            form.add_formemail(label="Email", name="email", placeholder="Enter your email")
            form.add_formtextarea(label="Message", name="message", placeholder="Enter your opinion please")
            form.add_formsubmit(label="Send")

    page.add_divider()

    page.footer = pv.Footer(
        title='Test footer',
        logo='https://m.media-amazon.com/images/W/MEDIAX_792452-T1/images/I/'
        '61yLqkmcN9L._SL1500_.jpg',
        link='/'
    )
    
    return page.to_html()

@app.route('/save_opionion', methods=['POST'])
def save_opionion():
    name = request.form['name']
    email = request.form['email']
    opinion = request.form['message']

    return jsonify({'status': 200, 'message': 'OK', 'payload': {'name': name, 'email': email, 'opinion': opinion}})

if __name__ == '__main__':
    app.run(debug=True)
