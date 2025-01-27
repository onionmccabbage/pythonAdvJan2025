# here we check that the 'requests' library is working
# we may need to install the requests library (it is not part of the python standard library)
# python -m ensurepip
# then
# pip install requests
# or
# python -m pip install requests
import requests

# a method to grab remote API data
def getData():
    '''fetch some data from an API'''
    results = requests.get('https://jsonplaceholder.typicode.com/posts/77')
    # we have a response object
    data = results.json() # thsi API returns JSON data
    return data

if __name__ == '__main__':
    d = getData()
    print(d) # some text
