import requests

if __name__ == "__main__":
    print('Request Version: '+ str(requests.__version__) +' \n')
    print('Google homepage: '+ str(requests.get("https://www.google.com").text)+'\n')
    python_script = requests.get(
        "https://raw.githubusercontent.com/Henry417E1610/cmput404_lab1/master/google.py")
    source_code = requests.get(
            'https://github.com/Henry417E1610/cmput404_lab1/blob/master/google.py'
        )
    print(
        'The source code of the python script from github is: '+str(source_code.text)+'\n'
    )
    print('Raw link: '+str(python_script.text) + '\n')
    
    with open('github_script.py', 'w') as doc:
        doc.write(python_script.text)
        doc.close()  
