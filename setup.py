from setuptools import setup

setup(name='django-g-recaptcha',
      version='0.1.4',
      description='Django view decorator to validate google recaptcha forms',
      url='https://bitbucket.org/deltaskelta/django-g-recaptcha-validate/overview',
      author='Jeff Willette',
      author_email='jrwillette88@gmail.com',
      keywords = ['django', 'recaptcha', 'catpcha'],
      packages = ['g_recaptcha',],
      include_package_data = True,
      install_requires = ["Django"]
)