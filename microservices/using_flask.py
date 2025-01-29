# we may need to pip install flask
from flask import Flask

def main():
    # some, data we may need
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    ) 
    ''' here we start a simple flask server'''
    app = Flask(__name__)
    # we declare routes
    @app.route('/')
    def root():
        return 'Welcome to this Flask server'
    @app.route('/about')
    def about():
        return 'info about stuff'
    @app.route('/data')
    def data():
        '''here we might grab some data from API, DB, file....'''
        response = '''<h2>Data Results</h2>
        <p>Interesting data retrieved...<p>
        '''
        for c in creatures_t:
            response += f'<li>{c["creature"]}<li>'
        return response 
    
    # we need to start our server
    app.run()


if __name__ == '__main__':
    main()