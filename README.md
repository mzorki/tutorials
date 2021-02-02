# tutorials

**tutorials** is a collection of tutorials and code examples for working with Chinese language. <br>
At this point, in contains: <br>
* Tokenization: a file on tokenizing Chinese language (including Old and Medieval Chinese) with different tools

## Installation & running

The tutorials are written with Google Colab in .ipynb format.
This means, that there are two ways to run them.

1. the default one: copy the contents of this repository as a separate folder to your Google Drive account and open notebooks with Google Colab (right click -> "Open with" -> "Google Colaboratory")
2. if already familiar with Jupyter Notebooks, use them to run from computer. <br>
In this case, skip the steps with mounting Google Drive and install all the required libraries from the command line. <br>
  * Examples of parts to remove:
```python
from google.colab import drive
drive.mount('/gdrive', force_remount=True)

project_dir = "/gdrive/My Drive/My_folder/" 
#move to the working directory 
%cd {project_dir} 

!pip install pyhanlp
!pip install udkanbun
```
  * If the file imports a local module that is **not** inside the same folder, it might be necessary to change the code according to this template: <br>
  Find this code...
  
```python
from helper import dict_tokenizer as dt
```
  ...and replace it with this (where './helper' is the relative path to the folder with helper code):
```python
import sys
sys.path.insert(0,'./helper')
import dict_tokenizer as dt
```
## Errors and bugs

If something does not work in the code, there is a way to notify me about this by creating an issue. [Click here](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue) to read a guide on how to do this.

## Academic usage

If you are using any part of these tutorials for a research project, especially my own tokenization algorithm, I would appreciate a note mentioning me or a more formal citation. For more information on my academic work, please check my website https://marianazorkina.com/ <br>



