from setuptools import setup

setup(
    name="django-mixin",
    version="1.0.0",
    description="Reusable, generic mixins for Django",
    long_description="Mixins to add easy functionality to Django class-based views, forms, and models.",
    keywords="django, views, forms, mixins",
    author="Kenneth Love <kenneth@brack3t.com>, Chris Jones <chris@brack3t.com>, Kalinin Dmitry <kalinin.mitko@gmail.com>",
    author_email="kalinin.mitko@gmail.com",
    url="https://github.com/null-none/django-mixin/",
    license="BSD",
    packages=["mixin"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0"
    ],
    install_requires=[
        "Django>=1.11.0",
        "six"
    ],
)
