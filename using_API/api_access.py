# NB the requests library wraps the older 'urllib3' library that is part of python
import requests

# remember - it is often a good idea to avoid putting anything in the global namespace
apiURL = 'https://jsonplaceholder.typicode.com/users'


def getUsers():
    '''fetch some user data from an API, allow the possibility of parameters'''
    global apiURL # we now have direct access to the apiUrl that was defined globally within this module
    # whenever we are dealing with i/o bound data, its a good idea to handle exceptions
    try:
        response = requests.get(apiURL) # here we make a request to the URL
        print(response.status_code)
        print(response.raw) # or .text or .json or .html .xml etc.
        # grab the JSON from the response
        res_j = response.json() # the JSON text will be converted to a Python structure
        # return the JSON as a Python structure
        return res_j
    except Exception as err:
        print(f'There was a problem: {err}')
    finally:
        '''always runs, even if there is an exception'''


def main():
    '''exercise the code'''
    r = getUsers()
    print(r, type(r))

if __name__ == '__main__':
    main()