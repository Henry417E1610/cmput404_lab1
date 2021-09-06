import requests, sys

if __name__ == "__main__":
    sys.stdout.write(f'Request Version: {requests.__version__} \n')
    sys.stdout.write(
        f'Google homepage: {requests.get("https://www.google.com").text}')
    python_script = requests.get(
        "https://raw.githubusercontent.com/Henry417E1610/cmput404_lab1/master/google.py")
    source_code = requests.get(
            'https://github.com/Henry417E1610/cmput404_lab1/blob/master/google.py'
        )
    sys.stdout.write(
        f'The source code of the python script from github is: {source_code.text}\n'
    )
    sys.stdout.write(f'Raw link: {python_script.text}\n')
    
    with open('github_script.py', 'w') as doc:
        doc.write(python_script.text)
        doc.close()  