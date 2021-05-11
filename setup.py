import shutil

from setuptools import find_packages, setup
from pathlib import Path

here = Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="yt_keeper",
    version="0.0.2",
    packages=find_packages(),
    author="Jakub Kazimierczak",
    description="A packaging example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    license='MIT',
    install_requires=["youtube-dl", "pyyaml", "pydantic"],
    entry_points={
        "console_scripts": [
            "yt_keeper=yt_keeper.__main__:main",
        ],
    },
)

# Config copying
src = here / 'yt_keeper' / 'config.yml'
dst = Path.home() / '.config' / 'yt_keeper' / 'config.yml'

dst.parent.mkdir(parents=True, exist_ok=True)
if not dst.exists():
    shutil.copyfile(src, dst)
