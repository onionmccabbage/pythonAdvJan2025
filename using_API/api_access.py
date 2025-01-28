# NB the requests library wraps the older 'urllib3' library that is part of python
import requests
from random import randint

# remember - it is often a good idea to avoid putting anything in the global namespace
apiURL = 'https://nonsense.typicode.com/users'


def getUsers(n=1): # we should think about validating n
    '''fetch some user data from an API, allow the possibility of parameters'''
    global apiURL # we now have direct access to the apiUrl that was defined globally within this module
    # whenever we are dealing with i/o bound data, its a good idea to handle exceptions
    try:
        response = requests.get(f'{apiURL}/{n}') # here we make a request to the URL
        print(response.status_code) # 200 is good news, 404 means not found (but is not an error)
        print(response.raw) # or .text or .json or .html .xml etc.
        # grab the JSON from the response
        res_j = response.json() # the JSON text will be converted to a Python structure
        # return the JSON as a Python structure
        return res_j
    except Exception as err:
        print(f'There was a problem: {err}')
    finally:
        '''always runs, even if there is an exception'''
        # typically we write tidy-up code in the finally block
        print('all done')
    print('this always runs!! (unless there is a terminal exception)')

def randNum():
    '''return a random integer 1-10'''
    return randint(1,10)

def main():
    '''exercise the code'''
    n = randNum()
    r = getUsers(n)
    print(r, type(r))

if __name__ == '__main__':
    main()