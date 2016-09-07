from setuptools import setup

setup(name='django-g-recaptcha',
      version='0.1.7',
      description='Django view decorator to validate google recaptcha forms',
      url='https://github.com/deltaskelta/django-g-recaptcha',
      author='Jeff Willette',
      author_email='jrwillette88@gmail.com',
      keywords = ['django', 'recaptcha', 'catpcha', 'google'],
      packages = ['g_recaptcha',],
      include_package_data = True,
      install_requires = ["Django"]
)