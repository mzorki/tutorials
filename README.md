# tutorials

Tutorials is a collection of tutorials and code examples for working with Chinese language.

## Installation & running

The tutorials are written via Google Colab in .ipynb format.
This means, that there are two ways to run them.

1. the default one: copy the notebook to the Google Drive account and open with Google Colab
2. if already familiar with Jupyter Notebooks, run from them. <br>
In this case, skip the steps with mounting Google Drive and install all the required libraries from the command line. <br>
** Parts to remove:
```python
from google.colab import drive
drive.mount('/gdrive', force_remount=True)

project_dir = "/gdrive/My Drive/Digital Orientalist/" 
#move to the working directory 
%cd {project_dir} 

!pip install pyhanlp
!pip install udkanbun
```
** To be able to import a local package, remove the following code:
```python
import dict_tokenizer as dt
```
...and replace it with this:
```python
import sys
sys.path.insert(0,'./modules')
import dict_tokenizer as dt
```



