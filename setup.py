from setuptools import setup, find_packages

version = __import__('sendsms').__version__

setup(
    name="django-sendsms",
    version=version,
    url='http://github.com/bopo/django-sendsms',
    license='BSD',
    platforms=['OS Independent'],
    description="A simple API to send SMS messages.",
    long_description=open('README.rst').read(),
    author='Stefan Foulis',
    author_email='ibopo@126.com',
    maintainer='Stefan Foulis',
    maintainer_email='ibopo@126.com',
    packages=find_packages(),
    include_package_data=True,
    extras_require = {
      'esendex': ['requests'],
      'twilio': ['twilio'],
      'smssluzbacz': ['smssluzbacz-api']
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
