import requests, sys

if __name__ == "__main__":
    sys.stdout.write(f'Request Version: {requests.__version__} \n')
    sys.stdout.write(
        f'Google homepage: {requests.get("https://www.google.com").text}')