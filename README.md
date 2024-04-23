CCWC: Command Line Word Count Tool
CCWC is a command-line tool that provides word count statistics for a given file or standard input. It's a Python-based utility that mimics some functionalities of the classic Unix wc command, but with some additional features.

Features
CCWC can provide the following statistics:

Number of bytes (-c option)
Number of lines (-l option)
Number of words (-w option)
Number of characters (-m option)
If no option is provided, CCWC will output the number of lines, words, and bytes.

Usage
You can use CCWC in two ways:

Provide a filename as an argument:
```
ccwc filename.txt
```
txt
Pipe input from stdin:
```
cat filename.txt | ccwc
```
If no file is provided and there's no input from stdin, CCWC will print a help message and exit.

Installation
To install CCWC, you need to make the script executable and move it to a directory on your PATH. Here's how you can do it:
```
chmod +x ccwc.py
mv ccwc.py /usr/local/bin/ccwc
```

Now you can run CCWC from anywhere using the ccwc command.

Version
You can check the version of CCWC with the --version option:
```
ccwc --version
```
Help
To see a help message with a description of all options, use the -h or --help option:
```
ccwc --help
```
