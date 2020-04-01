from setuptools import setup

setup(
    name="ElectricidadRafa",
    version="1.0",
    author="Rafa",
    author_email="raguiarperez@danielcastelao.org",
    url="https://www.danielcastelao.org",
    license="GLP",
    platforms="Unix",
    clasifiers=["Development Status :: 3 - Alpha",
                "Environment :: Console",
                "Topic :: Software Development :: Libraries",
                "License :: OSI Aproved :: GNU General Public License",
                "Programming Language :: Python :: 3.4",
                "Operating System :: Linux Ubuntu"
                ],
    description="Proyecto DI",
    keywords="empaquetado instalador paquetes",
    packages=['proyecto'],
    #data_files=[('datos', ['dat/datos.txt'])],
    entry_points={'console_scripts': ['openProyect = proyecto.ElectricidadRafa: main', ], }
)