#!/usr/bin/env python3

import jinja2
import yaml

template = jinja2.Template(open("README.md.j2", 'r').read())
profileData = yaml.load(open("profile.yaml", 'r'), Loader=yaml.FullLoader)
open("README.md",'w').write(template.render(profileData))
