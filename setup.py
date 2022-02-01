import io
import os

from setuptools import find_packages, setup

VERSION = '0.1.0a'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

with io.open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sqlalchemy-es',
    description=('SQLAlchemy dialect for Elasticsearch with write operations support'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'sqlalchemy.dialects': [
            'elasticsearch = sqlalchemy.dialects.es:ESHTTPDialect',
            'elasticsearch.http = sqlalchemy.dialects.es:ESHTTPDialect',
            'elasticsearch.https = sqlalchemy.dialects.es:ESHTTPSDialect',
            'elasticsearch.aws = sqlalchemy.dialects.es.aws:ESHTTPDialect',
            'elasticsearch.aws.http = sqlalchemy.dialects.es.aws:ESHTTPDialect',
            'elasticsearch.aws.https = sqlalchemy.dialects.es.aws:ESHTTPSDialect',
        ]
    },
    install_requires=['elasticsearch>7, <7.14', 'packaging>=21.0, <22.0', 'sqlalchemy'],
    extras_require={'opendistro': ['requests_aws4auth', 'boto3']},
    # author='',
    # author_email='',
    url='https://github.com/usalko',
    download_url='https://github.com/usalko/elasticsearch-es/releases/tag/'
    + VERSION,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    tests_require=['nose>=1.0'],
    test_suite='nose.collector',
)
