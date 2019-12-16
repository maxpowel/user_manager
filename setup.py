from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
  name='user_manager',
  packages=['user_manager'],
  version='2.2',
  description='Minimal user manager interface',
  author='Alvaro Garcia Gomez',
  author_email='maxpowel@gmail.com',
  url='https://github.com/maxpowel/user_manager',
  download_url='https://github.com/maxpowel/user_manager/archive/master.zip',
  keywords=['user', 'manager'],
  classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System', 'Topic :: Utilities'],
  install_requires=install_requires
)
