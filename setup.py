import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LRFGuideMe',
      version='2.0.0',
      description=('A docassemble extension.'),
      long_description='#Authors\r\n\r\nThis project originally was called SuffolkLITLab/docassemble-HousingGuide, owned by Quinten Steenhuis, quinten@lemmalegal.com, designed and written as a student project by Michael Buccino and Melanie Kaufman. \r\n\r\nWe inherited the 0.10 version of that project, and on 7/29/2020 moved it to a new location under this new project name, as we continue to adapt it for implementation on the Massachusetts Legal Resource Finder.\r\n\r\nRochelle Hahn\r\nGordon Shaw\r\nCaroline Robinson\r\nPurple Sky\r\n\r\n=============================================\r\nMajor revisions:\r\nVersion 2.0.0 - added the Spanish translation in Nov. 2022.',
      long_description_content_type='text/markdown',
      author='Team Effort',
      author_email='rhahn@mlri.org',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LRFGuideMe/', package='docassemble.LRFGuideMe'),
     )

