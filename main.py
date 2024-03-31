from flask import Flask, request, jsonify
import pyvibe as pv

app = Flask(__name__)

@app.route('/')
def index():
    page = pv.Page('Home')

    page.navbar = pv.Navbar(
        title='My PyVibe test',
        logo='https://www.getautismactive.com/wp-content/uploads/'
             '2021/01/Test-Logo-Circle-black-transparent.png',
    )
    page.add_header('My PyVibe test page')
    page.add_text(value="Here's simple PyVibe + Flask test page")
    page.add_link(
        text='Heres a link, where you can see more',
        url='https://www.pycob.com'
    )
    page.add_divider()

    page.add_header('A sample of code', size=2)
    with page.add_card() as card:
        card.add_code(
            value = """\nimport pyvibe as pv\n\npage = pv.Page()\npage.add_header("Welcome to PyVibe!")\npage.add_text("PyVibe is an open source Python library for creating UI components for web apps without the need to write HTML code.")""",
            header = 'Simple app example'
        )

        card.add_alert(text="Isn't it pretty?", badge="INFO", color="indigo")

    page.add_divider()

    page.add_header('A sample form', size=2)

    marks = [
        {'value': '1', 'label': '1/5'},
        {'value': '2', 'label': '2/5'},
        {'value': '3', 'label': '3/5'},
        {'value': '4', 'label': '4/5'},
        {'value': '5', 'label': '5/5'}
    ]

    with page.add_card() as card:
        card.add_header("PyVibe Survey Form Example", size=2)

        with card.add_form(method='POST', action="/save_opinion") as form:
            form.add_formtext(
                label="Name", name="name", placeholder="Enter your name"
            )
            form.add_formemail(
                label="Email", name="email", placeholder="Enter your email"
            )
            form.add_formselect(
                label='Select your mark', name='mark', options=marks
            )
            form.add_formtextarea(
                label="Message", name="message",
                placeholder="Enter your opinion please"
            )
            form.add_formhidden(
                name='token', value='2a5c7c8vn39vc96v0t67y334rrv'
            )
            form.add_formsubmit(label="Send")

    page.add_divider()

    page.add_header('A sample list', size=2)

    page.add_image(
        url='https://upload.wikimedia.org/wikipedia/'
            'uk/b/b1/Mortal_Kombat_Logo.svg',
        alt='MK logo', classes = 'w-20'
    )

    page.add_alert(
        text="Here's only some of the characters...", badge='Warning',
        color='orange'
    )

    test_list = page.add_list()
    test_items = ['Sub-Zero', 'Sonya', 'Jax', 'Johnny Cage']

    for item in test_items:
        test_list.add_listitem(value=item)

    page.add_divider()

    page.footer = pv.Footer(
        title='Test footer',
        logo='https://www.getautismactive.com/wp-content/uploads/'
             '2021/01/Test-Logo-Circle-black-transparent.png',
        link='/'
    )
    
    return page.to_html()

@app.route('/save_opinion', methods=['POST'])
def save_opinion():
    name = request.form['name']
    email = request.form['email']
    opinion = request.form['message']
    mark = request.form['mark']
    token = request.form['token']

    return jsonify(
        {
            'status': 200, 'message': 'OK', 'token': token,
            'payload': {
                'name': name, 'email': email, 'opinion': opinion, 'mark': mark
            },
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
