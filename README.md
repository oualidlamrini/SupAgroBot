# SupAgroBot

This git reposotory is build to automate the mesurements of Alfalf's LAI, with the use of [ImageJ](https://ij.imjoy.io/) web site.

# Insallation

The SupAgrBot is mainly build with the Python's [Selenium](https://www.selenium.dev/documentation/) package. So to use the script do the following:

-   **Install Anaconda**:The official web site of [Anaconda](https://www.anaconda.com/download/).
-   **Create an environment**: Open a terminale and type.

``` bash
conda create - n selenium 
```


-   **Activate the invironment**:Working with the installed packages of `requirements.txt`

``` bash
conda activate selenium
```

-   **install requirements**:Install the needed packages.

``` bash
pip install -r requirements.txt
```

-   **Clone the repo**:The last step

``` bash
# Change the working directory 
cd path_to_the_folder_where_you_want_to_clone
```

``` bash
# Clone 
git clone https://github.com/oualidlamrini/SupAgroBot.git
```

# Usage

For technical issues it was relevant to remove the backround of all images in order to have a good precision of the **LAI**, and split the folder of this images into 6 batches.

The most imporatnt files in this reposotry are :

-   `constantes.py`:Contains all paths used in the script, and they should be cahnged in order to have the right access into the rghit folder (see comments of `constantes.py`).

-   `remove.py`: Remove the backround of the images

-   `Split.py`: Split the removed backround images's folder into 6 bach

-   `run.py`: Extract the **LAI** from different baches image by image in a `CSV`file.

-   `CSV.py`: Concatenate all `CSV` file in a sigle one.

-   **Remove backround** by using the `remove.py` and make the images in a *folder* (`M1_Remove` for exemple):

``` bash
python path_to_the_folder_where_you_want_to_clone/SupAgroBot/bot/remove.py
```

-   **Split** the *folder* (`M1_Remove` for exemple) into 6 batches from 1 to 6:

``` bash
python path_to_the_folder_where_you_want_to_clone/SupAgroBot/bot/Supagro/Split.py
```

-   **Extract LAI** from the different baches from bach_1 to batch_6 one by one :

``` bash
# Extract the LAI from the first batch
python path_to_the_folder_where_you_want_to_clone/SupAgroBot/bot/run.py batch_1
```

``` bash
# Extract the LAI from the sixthe batch
python path_to_the_folder_where_you_want_to_clone/SupAgroBot/bot/run.py batch_6
```

-   **Concatenate the CSVs files** into just one:

``` bash
python path_to_the_folder_where_you_want_to_clone/SupAgroBot/bot/Supagro/CSV.py
```

NB:If a following like error message is displayed, just run the `run.py` file again.

``` bash
Traceback (most recent call last):
  File "/Users/oualidlamrini/Documents/SupAgroBot/bot/run.py", line 18, in <module>
    bot.Upload_file()
  File "/Users/oualidlamrini/Documents/SupAgroBot/bot/Supagro/imageJFunc.py", line 47, in Upload_file
    file = WebDriverWait(self, 1).until(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Caskroom/miniconda/base/envs/selenium/lib/python3.11/site-packages/selenium/webdriver/support/wait.py", line 101, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message:
```
