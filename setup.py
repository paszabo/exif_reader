from distutils.core import setup

with open('requirements.txt') as require_fp:
    requirements = require_fp.readlines()

with open('README.md') as readme_fp:
    readme = readme_fp.read()

with open('LICENSE.txt') as license_fp:
    license = license_fp.read()


setup(
    name='ExifReader',
    version='0.0.1',
    packages=['exif_reader'],
    license=license,
    long_description=readme,
    install_requires=requirements,
    description='Read EXIF data from a JPG',
    entry_points={
        'console_scripts': [
            'read_exif = exif_reader.scripts.read_exif:main',
        ],
    },
)
