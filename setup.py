from setuptools import setup

setup(
    name="OctoPrint-XYZPosition",
    version="0.1",
    description="An OctoPrint plugin that provides real-time XYZ position data",
    author="JayG",
    author_email="jaygoswami1121@gmail.com",
    url="https://github.com/J-labG/OctoPrint-XYZPosition",
    license="AGPLv3",
    packages=["octoprint_xyzposition"],
    include_package_data=True,
    install_requires=["octoprint"],
    entry_points={
        "octoprint.plugin": [
            "xyz_position = octoprint_xyzposition"
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
