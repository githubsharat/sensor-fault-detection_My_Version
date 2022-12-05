from setuptools import find_packages, setup   


def get_requirements():
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    requirement_list = []


    HYPHEN_E_DOT = "-e ."
    with open("requirements.txt") as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
 
    name = "sensor",                   #           
    version = "0.0,1",                 # Any version no. Let's say 0.0.1
    author = "Sharat",                 # Author's name
    author_email = "test@test.com",    # Author's email
    packages = find_packages(),        # We will call a function find_packages. This will search for all packages within the project folder.
    #install_requires = ["pymongo==4.2.0"] # Here we write a list of libraries needed for this project. The libraries we mention in requirements.txt needs be mentioned here.
    install_requires = get_requirements()
)

