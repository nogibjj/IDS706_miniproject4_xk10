[![CI/CD Workflow](https://github.com/nogibjj/IDS706_miniproject4_xk10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_miniproject4_xk10/actions/workflows/cicd.yml)

## Github Actions Matrix Build for Multiple Python Versions
### Purpose:
This project is to establish a robust Github Actions workflow, desgined to faciliate automated testing across multiple Python versions. This is to ascertain the compatibility and reliability of the code in diverse environments. The deliverables are the presented Github repository, and a link demonstrating a successful execution of the Github Actions Matrix across at least three distinct Python versions.

### This repo contains:
1.`Makefile`: a makefile is a configuration file used in Unix-based systems for autmating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

Run make install, make test, make lint, make format:
![Screen Shot 2023-09-24 at 22 12 19](https://github.com/nogibjj/IDS706_miniproject4_xk10/assets/143849077/d14a3b2d-dbe7-43db-a60f-2b65ee9fcb66)

2. `requirments.txt`: this file is to specify the dependencies (libraries and packages) required to run the project.

3. `devcontainer` including a Dockerfile: the 'Dockerfile' within this folder specifies how the container should be built, and other settings in this directory may control development environment configurations.

4. `gitignore`: this file is used to specify which files or directories should be excluded from vrsion control when using Git.

5. `GitHubActions`: (.github/workflows) which contain configuration files for setting up automated build, test and format pipelines for the project.
Modify the Github actions to include testing for Python versions:
![Screen Shot 2023-09-24 at 22 15 04](https://github.com/nogibjj/IDS706_miniproject4_xk10/assets/143849077/bc5bb4cf-0d0b-45ac-a39a-467c293d6ae1)

7. `main.py`: This is the main Python script for the project. Modify it to implement the project's functionality.
Add check for versions of Python for different environment with main.py and test_main.py
![Screen Shot 2023-09-24 at 22 16 02](https://github.com/nogibjj/IDS706_miniproject4_xk10/assets/143849077/71b501f3-4db5-4ad5-b93c-e737c06b54af)

9. `test_main.py`: This is the unit testing script for the project. Write test cases to ensure the correctness of the code.

### Successful Github Action Matrix Run:
![Screen Shot 2023-09-24 at 22 17 36](https://github.com/nogibjj/IDS706_miniproject4_xk10/assets/143849077/049218de-e52e-46d8-9efc-c00d06df0b01)











