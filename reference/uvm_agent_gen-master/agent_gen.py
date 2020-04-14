#!/usr/bin/env python
"""
Walk the template directory and spit out a matching set of files/directories rendered from the templates.
"""
import argparse
import os

from jinja2 import Template
from jinja2 import Environment, PackageLoader

import ConfigParser

# Unit testing
import unittest

# *****************************************************************************
# Agent Generator
# *****************************************************************************
def generate_agent (debug, agent_name, settings, dest_dir):
    """
    Walk the template directory and render any templates found into the destination directory
    """
    # Create the template rendering environment
    env = Environment(loader=PackageLoader('agent_gen', 'templates'))

    agent = {}


    agent['copyright'] = settings.get('Copyright', 'Copyright').split(r'\n')

    agent['author']  = settings.get('User', 'Name')
    agent['email']   = settings.get('User', 'Email')
    agent['href']    = settings.get('User', 'Website')
    agent['company'] = settings.get('User', 'Company')

    agent['name'] = agent_name

    # Create destination path if required
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")

    for dir, subdir_list, file_list in os.walk(template_path):
        if debug:
            print('In directory: %s' % dir)

        # Replicate any subdir structure into the destination
        try:
            temp, template_subdir = dir.split('templates/')
            if debug:
                print ('Dir to make: %s' % template_subdir)
            dest_path = os.path.join(dest_dir, template_subdir)
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
        except ValueError:
            # No subdir case
            continue

        # Now render any templates
        for fname in file_list:
            agent['file'] = os.path.splitext(fname)[0]
            if debug:
                print('\tFound File: %s' % fname)
            template = env.get_template(os.path.join(template_subdir, fname))
            rendered_template = template.render(agent=agent)

            dest_filename = agent_name + fname
            dest_filename = os.path.join(dest_path, dest_filename)
            if debug:
                print('\tCreating File: %s' % dest_filename)
            with open(dest_filename, 'w') as dp:
                dp.write(rendered_template)

def make_dir (dir_name, dest_dir):
    pass

# *****************************************************************************
# Unit Tests
# *****************************************************************************
class BasicTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_calc(self):
        pass
        # self.assertEqual(val, other_val)


# *****************************************************************************
# Program Flow
# *****************************************************************************
# -------------------------------------
# Parse the command line options
# -------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Agent Generator')
    parser.add_argument('-debug', action='store_true',
                       help='Print Debug Messages')
    parser.add_argument('--agent_name', action='store', required=True,
                       help='Agent Name')
    parser.add_argument('--dest', action='store', required=True,
                       help='Destination Directory for the rendered agent')
    args = parser.parse_args()

    # Get the Config
    settings = ConfigParser.ConfigParser()
    settings.read('agent_gen.cfg')

    # -------------------------------------
    # Actually do the work we intend to do here
    # -------------------------------------
    generate_agent(args.debug, args.agent_name, settings, args.dest)

# -------------------------------------
if __name__ == "__main__":
    main()


