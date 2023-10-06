# 0x02. Shell, I/O Redirections and filters project #
This project is an introduction to the Linux concept of input/output redirections across files using different Linux commands. The commands introduced or used in more depth in this project are: 
- `echo`
- `cat`
- `head`
- `tail`
- `find`
- `wc`
- `sort`
- `uniq`
- `grep`
- `tr`
- `rev`
- `cut`

I used the above commands to write bash scripts to perform the functions as described below.

## Scripts ##
- [0-hello_world](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/0-hello_world) prints `Hello, World`, followed by a new line to the standard output.
- [1-confused_smiley](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/1-confused_smiley) displays a confused smiley `"(Ôo)'`.
- [2-hellofile](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/2-hellofile) displays the contents of the `/etc/passwd` file.
- [3-twofiles](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/3-twofiles) displays the contents of the two files `/etc/passwd` and `/etc/hosts`
- [4-lastlines](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/4-lastlines) displays the last 10 lines of the file `/etc/passwd`
- [5-firstlines](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/5-firstlines) displays the first 10 lines of the file `/etc/passwd`
- [6-third_line](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/6-third_line) dispays the the third line of the file `iacta`
- [7-file](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/7-file) creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` followed by a new line
- [8-cwd_state](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/8-cwd_state) writes the result of the command `ls -la` into the file `ls_cwd_content`
- [9-duplicate_last_line](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/9-duplicate_last_line) duplicates the last line of the file `iacta`
- [10-no_more_js](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/10-no_more_js) deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders
- [11-directories](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/11-directories) counts the number of directories and sub-directories in the current directory
- [12-newest_files](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/12-newest_files) displays the 10 newest files in the current directory
- [13-unique](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/13-unique) takes a list of words as input and prints only words that appear exactly once. The output is sorted
- [14-findthatword](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/14-findthatword) displays lines containing the pattern `root` from the file `/etc/passwd`
- [15-countthatword](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/15-countthatword) displays the number of lines that contain the pattern `bin` in the file `/etc/passwd`
- [16-whatsnext](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/16-whatsnext) displays lines containing the pattern `root` and 3 lines after them in the file `/etc/passwd`
- [17-hidethisword](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/17-hidethisword) displays all the lines in the file `/etc/passwd` that do not contain the pattern `bin`
- [18-letteronly](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/18-letteronly) displays all lines of the file `/etc/ssh/sshd_config` starting with a letter
- [19-AZ](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/19-AZ) replaces all characters `A` and `c` from an input to `Z` and `e` respectively
- [20-hiago](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/20-hiago) removes all letters `c` and `C` from an input
- [21-reverse](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/21-reverse) reverses an input string passed to it
- [22-users_and_homes](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/22-users_and_homes) displays all users and their home directories, sorted by users. Recieves its input from the `/etc/passwd/` file

## Advanced Scripts ##

- [100-empty_casks](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/100-empty_casks) finds all empty files and directories in the current directory and all sub-directories.
	* Only the names of the files and directories should be displayed (not the entire path)
	* Hidden files should be listed
	* One file name per line
	* The listing should end with a new line
	* `basename`, `grep`, `egrep`, `fgrep` or `rgrep` are not allowed for this task

- [101-gifs](https://github.com/Madu-f0r0/alx-system_engineering-devops/blob/master/0x02-shell_redirections/101-gifs) lists all the files with a `.gif` extension in the current directory and all its sub-directories.
	* Hidden files should be listed
	* Only regular files (not directories) should be listed
	* The names of the files should be displayed without their extensions
	* The files should be sorted by byte values, but case-insensitive
	* One file name per line
	* The listing should end with a new line
	* `basename`, `grep`, `egrep`, `fgrep`, and `rgrep` are not allowed for this script

## Author ##
Daniel Herbert
