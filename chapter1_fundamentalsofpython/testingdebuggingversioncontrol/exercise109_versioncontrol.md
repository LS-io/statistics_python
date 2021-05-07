### This is a simple exercise to walk you through the basics of creating and linking a repository, effectively using version control with Git and GitHub.

1. If you haven't already, register for a GitHub account on [GitHub](https://www.github.com/).

2. Go to https://git-scm.com/downloads and download the Git client software for your system and install it.
    
    This Git client will be communicating with the GitHub server. You know if your Git client is installed successfully, if you can run the `git` command in your Terminal:

    ```
    $ git 
    usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
    [--exec-path[=<path>]] [--html-path] [--man-path] [--infopath]
    [-p | --paginate | -P | --no-pager] [--no-replace-objects]
    [--bare]
    [--git-dir=<path>] [--work-tree=<path>]
    [--namespace=<name>]
    <command> [<args>]
    ```
    Otherwise, your system might need to reboot.

3. Let's start by applying version control to a simple project. First, create a dummy folder and generate a Jupyter notebook (or `.py` file in my case) and a test file named `input.txt` with the following content in it:
    ```
    1,1,1
    1,1,1
    ```

4. In the first cell of the Jupyter notebook (or in the beginning of your `.py` file), write a function called `add_elements()`, that takes two lists of numbers and ads them up element-wise. The function should return a list that consists of the element-wise sums; we can assume the two parameter lists are of the same length:
    ```
    def add_elements(a, b):
        result = []
        for item_a, item_b in zip(a, b):
            result.append(item_a + item_b)

        return result
    ```

5. In the next code cell, read in the `input.txt` file using a `with` stament and extract the last two lines of the file using the `readlines()` function and list indexing:
    ```
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    last_line1, last_line2 = lines[-2], lines[-1]
    ```
    Note that in the `open()` function, the second argument, 'r', specifies that we are reading the file, as opposed to writing to the file (that would be specified with 'w' or 'a')

6. In a new code cell (or line in the `.py` file), we convert these two strings of text input into lists of numbers, first using the `str.split()` function with the `','` argument to isolate the individual numbers in each line, and then the `map()` and `int()` functions to apply the conversion to integers element-wise:
    ```
    list1 = list(map(int, last_line1[: -1].split(',')))
    list2 = list(map(int, last_line2]: -1].split(',')))
    ```

7. In another new code cell (or line in the `.py` file), call `add_elements()` on `list1` and `list2`. Write the returned list to the same input file in a new line in the same **comma-separated values (CSV)** format:
    ```
    new_list = add_elements(list1, list2)

    with open('input.txt', 'a') as f:
        for i, item in enumerate(new_list):
            f.write(str(item))

            if i < len(new_list) - 1:
                f.write(',')
            else:
                f.write('\n')
    ```
    Here the 'a' argument specifies that we are writing to append a new line to the file, as opposed to reading (`'r'`) and overwriting (`'w'`) the file completely

8. Run the code cell and verify that the text file has been updated to the following:
    ```
    1,1,1
    1,1,1
    2,2,2
    ```

9. This is the current setup of our example project so far:
    * we have a text file and a Python script inside a folder
    * the script can alter the content of the text file when run
        * this setup is quite common in real-life situations:
            >you can have a data file that contains some information that you'd like to keep track of and a Python program that can read in that data and update it in some way (perhaps through a prespecified computation or adding new data that was collected externally).
    
    Now, let's implement version control in this example project

10. Go to your online GitHub account and click on the plus sign icon (+) in the top-right corner of the window, choose the `New repository` option

    Input a sample name for the new repository in the form and finalise the creation process. Copy the URL of this new repository

11. On your local machine, open the Terminal and navigate to the folder. Run the following command to initialize a local Git repository, which will be associated with our folder:
    ```
    $ git init
    ```

12. Still in the Terminal, run the following command to add everything in our project to Git and commit:
    ```
    git add .
    git commit -m [any message with double quotes]
    ```
    Instead of `git add .`, we can replace `.` with the names of the files that we want to register with Git. Useful for when we only want to register selected files as in contrast to every file in the folder.

13. We need to link our local repository to the online one that we have created (in step 10):
    ```
    git remote add origin [URL to GitHub repository]
    ```
    "origin" is simply a conventional nickname for the URL of the repository

14. Finally, upload the locally registered files to the online repository:
    ```
    git push origin master
    ```

15. Go to teh website of the online repository to confirm that the local files have been uploaded to GitHub

16. On our local computer, we run the script included in the Jupyter notebook (or `.py` file) and change the text file.

17. To commit the changes to the GitHub repository, we run the following commands:
    ```
    git add .
    git commit
    git push origin master
    ```

18. go to the online repository and refresh, to verify we have indeed uploaded the changes to GitHub.