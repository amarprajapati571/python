from setuptools import setup

setup(
    name='pubnub',
    version='4.0.0.beta2',
    description='PubNub Real-time push service in the cloud',
    author='PubNub',
    author_email='support@pubnub.com',
    url='http://pubnub.com',
    modules=['pubnub'],
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    install_requires=[
        'pycryptodomex>=3.3',
        'requests>=2.4',
        'six>=1.10'
    ],
    zip_safe=False,
)
