from setuptools import setup
from djangochurch_docs_theme import __version__


setup(
    name='djangochurch-docs-theme',
    version=__version__,
    url='https://github.com/djangochurch/djangochurch_docs_theme/',
    license='MIT',
    author='Django Church',
    author_email='info@djangochurch.org',
    description='Django Church Sphinx theme.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['djangochurch_docs_theme'],
    package_data={'djangochurch_docs_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
