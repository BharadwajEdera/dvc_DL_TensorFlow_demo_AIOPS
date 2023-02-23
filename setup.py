from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='DVC DL-TF practise',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/BharadwajEdera/dvc_DL_TensorFlow_demo_AIOPS",
    author='Bharadwaja Edera',
    python_requires=">=3.7",
    install_requires=[
                'dvc',
                'matplotlib',
                'numpy',
                'pandas',
                'PyYAML',
                'tensorflow',
                'tqdm',
                'boto3'
    ]

)