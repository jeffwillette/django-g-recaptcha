from setuptools import setup

setup(name='django-g-recaptcha',
      version='0.2.3',
      description='Django view decorator to validate google recaptcha forms',
      url='https://github.com/deltaskelta/django-g-recaptcha',
      author='Jeff Willette',
      author_email='jrwillette88@gmail.com',
      keywords = ['django', 'recaptcha', 'catpcha', 'google'],
      packages = ['g_recaptcha'],
      include_package_data = True,
      install_requires = [
      	"Django>=1.8",
      	"funcsigs>=1.0.2",
      	"mock>=2.0.0",
      	"pbr>=1.10.0",
      	"six>=1.10.0",]
)

# The command to upload: python setup.py sdist upload -r pypi