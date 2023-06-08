# LittleHelperPythonScripts
Here live some small custom Python scripts I wrote to solve everyday problems working with phylogenomic data. There are probably better options and more advanced programs for all these little helpers. However, often these programs simply do not do what I want them to do, or I am too lazy to figure out how they do it. Use these scripts at your own risk.

#### Simply git clone the directory:
`git clone https://github.com/TimBoeh/LittleHelperPythonScripts.git`
## 1. `rename_files.py` script
This tool changes the filenames in the current directory. It takes one mandatory and one optional argument. The first argument is the part of the filename you want to change or delete. The second is the new part to which you want to change the filename. If the second argument is not provided, the part of the filename you specified in the first argument is simply deleted. The `--help` flag or an unrecognized input will print a simple help text:
```
Usage: python rename_files.py [original_text] [new_text]
Arguments:
  [original_text]: Combination of letters and/or numbers within the file name to be changed (mandatory)
  [new_text]: Combination of letters and/or numbers to replace the original_text in the file name (optional)
```
Please be aware, the original file is not touched. Instead a copy of the original file with the modified file name is stored in a newly generated subfolder called **Renamed**.

<img width="110" src="https://raw.githubusercontent.com/TimBoeh/ LittleHelperPythonScripts/figs/rename_files_screenshot.png"/>


The simplest way, in my opionen, is to simpley specify an `alias` in you bashrc, like the following:
```
alias rename_files='python3 /home/user/YOUR/PATH/LittleHelperPythonScripts/rename_files/rename_files.py'
```
Afterwards run `source ~/.bachrc` and you can use the tool everywhere you need to.