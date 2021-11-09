import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gif_to_genga",
    version="0.1.0",
    author="MyFeminacyComplmentPlan",
    author_email="myfeminacycomplementplan@gmail.com",
    description="Create Anime-Gengas(key flames) by disassembling GIF file. Contributes to animation analysis of animators and creators.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MyFeminacyComplementPlan/gif_to_genga",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)


