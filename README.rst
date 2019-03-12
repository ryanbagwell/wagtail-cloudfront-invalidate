wagtail-cloudfront-invalidate
=============================

A Wagtail hook to invalidate a path when a page is updated

Installation
------------

::

    pip install wagtail-cloudfront-invalidate

Configuration
-------------

::

    INSTALLED_APPS = [
        'wagtail_cloudfront_invalidate'
    ]

    AWS_ACCESS_KEY_ID = '<your access key id>'

    AWS_SECRET_ACCESS_KEY = '<your secret key>'

    CLOUDFRONT_DISTRIBUTION_ID = '<your distribution id>'

    WAGTAIL_CLOUDFRONT_INVALIDATE_ENABLED = True #defaults to False
