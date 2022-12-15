import setuptools
import re
from pathlib import Path

package_name = "sense_t.daw.aa.supply_chain_api"
long_description = Path('README.md').read_text(encoding="utf-8")
version = re.search(
    r"__version__ = '([^']+)'",
    Path('src/sense_t/daw/aa/supply_chain_api/__init__.py').read_text(
        encoding="utf-8")).group(1)

setuptools.setup(
    name=package_name,
    version=version,
    author="Matthew Singline",
    author_email="matthew.singline@utas.edu.au",
    description="A simple api for the daw.aa supply chain project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=
    "https://bitbucket.org/sense-t/daw.aa.supply_chain_services/src/master/",
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_namespace_packages(where='src'),
    python_requires=">=3.6",
    # setup_requires=['setuptools_trial'],
    # test_suite="tests",
    tests_require=['aiosqlite', 'pytest', 'requests'],
    install_requires=[
        'asyncclick', 'pyyaml', 'fastapi', 'uvicorn[standard]', 'jsonschema',
        'pyjwt[crypto]', 'fastapi-utils'
    ],
    entry_points={
        'console_scripts': [
            'daw_aa_api = sense_t.daw.aa.supply_chain_api.cmd:cli',
        ],
    },
    include_package_data=True,
)
