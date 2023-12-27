rom setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='package-web-Analyze',
  version='0.0.1',
  author='st99-01-05',
  author_email='maaglebov@it.permkrai.ru',
  description='Analyze_web_source.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/st99-01-05/pstu_python2/tree/main/Итоговый',
  packages=find_packages(),
  install_requires=['requests>=2.25.1',
                    'googlesearch',
                    'fake_useragent>=1.4.0',
                    'beautifulsoup4',
                    'textblob',
                    'googletrans',
                    'nltk',
                    'matplotlib'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='Итоговый',
  project_urls={
    'GitHub': 'https://github.com/st99-01-05/pstu_python2/tree/main/Итоговый'
  },
  python_requires='>=3.8'
)
