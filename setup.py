# coding: utf-8

"""
    Accounting API


    The version of the OpenAPI document: 7.3.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import find_packages, setup  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "accounting-sh"
VERSION = "0.3.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "requests >= 2.32.3",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Accounting API",
    author="STAN-TAB CORP. LTD",
    author_email="support@stantabcorp.com",
    url="",
    keywords=["OpenAPI", "Accounting API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description_content_type="text/markdown",
    long_description="""\
    ### Welcome to STAN-TAB CORP&#39;s Accounting Software API documentation.  This page contains the documentation and reference of the Accounting API.  &gt; **NEW**: You can now use this API by registering on https://my.stantabcorp.com !  **Status Page:** [https://status.stantabcorp.net/status/accounting](https://status.stantabcorp.net/status/accounting)  #### Rate limits  The API is rate-limited based on IP addresses. By default you can make 3 request every 180 seconds (3 minutes). If you need an higher limit, please contact us with the list of ip address to whitelist.  #### Audit  You can add an arbitrary comment to every request that will be logged by adding the: &#x60;X-Audit-Comment&#x60; header with the comment you want to add to your requests.  #### Good to know  The way this API is designed, some webhook event are sent before the event happened and may be fired even if the action failed.   Webhooks events may be sent out of order. 
    """,  # noqa: E501
)
