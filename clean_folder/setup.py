import setuptools

if __name__ =='__main__':
    setuptools.setup(name = 'hw7',
                     version = '0.0.1',
                     description = "Sorting the files",
                     url = 'https://github.com/pm012/HW7',
                     author = 'Serhii',
                     author_email = 'john.doe@gmail.com',
                     license='MIT',
                     packages=setuptools.find_namespace_packages(),
                     entry_points={'console_scripts': ['clean-folder=clean_folder.clean:start']}
    )

