from setuptools import setup,find_packages

def get_requirement()->list[str]:
    requirements_list=list[str]=[]
    
    
    return requirements_list




setup(
    name='sensor',
    author='Aayush',
    author_email='ayushkumarash@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirement()#['pymongo']
  

)