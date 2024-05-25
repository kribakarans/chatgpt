#!/bin/env python3

import os
import json

html_dir = 'html'
files = sorted([f for f in os.listdir(html_dir) if f.endswith('.html')])

with open('files.js', 'w') as f:
    f.write('const files = ' + json.dumps(files) + ';')
