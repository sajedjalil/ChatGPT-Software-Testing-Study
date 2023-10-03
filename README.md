[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7700501.svg)](https://doi.org/10.5281/zenodo.7700501)

# ChatGPT Software Testing Study

A study on the capabilities of ChatGPT on correctly answering software testing textbook questions.

Our work on **"ChatGPT and Software Testing Education: Promises & Perils"** has been accepted in **ICSTW 2023**.

IEEEXplore link: [ieeexplore](https://ieeexplore.ieee.org/abstract/document/10132255)

Pre-print is now available at [arXiv.2302.03287](https://arxiv.org/abs/2302.03287).

# About
This tool automatically gathers ChatGPT responses on predefined questions from an Excel sheet mentioned in ```src/constant.py```. One of the key differences between this tool with any other conventional tool is that it can collect responses from ChatGPT in both shared and separate chat contexts. Please read [our paper](https://ieeexplore.ieee.org/document/10132255) for more information on shared and separate contexts.

The collected responses will be saved into the same Excel file that the tool is taking the questions from. This tool does not use the Official API endpoints for ChatGPT. Therefore, you might be limited by ChatGPT. If you are limited, please wait 1 hour before using this tool again.

## Installation

You can install the latest version of this software directly from GitHub with ```pip```:

```pip install git+https://github.com/mmabrouk/chatgpt-wrapper```

This will install chatgpt-wrapper and its dependencies. Before starting the program, you will need to install a browser
in Playwright (if you haven't already). The program will use Firefox by default.

```playwright install firefox```

With that done, you should start up the program in install mode, which will open up a browser window.

```chatgpt install```

Log in to ChatGPT in the browser window, then stop the program.

## Usage

From the terminal or IDE, run ```__main__``` function in the ```src/__init__.py``` file.


## Dataset Description
Our dataset contains questions from a well-known software testing book **''Introduction to Software Testing 2nd Edition''** by Ammann and Offutt. 
We use all the textbook questions in Chapters 1 to 5 that have solutions available on the book’s official website. 

Our dataset contains 31 such questions from these five chapters. 27 questions out of the 31 are multipart questions and the remaining 4 are independent.
This tool generates responses from the ChatGPT automatically for these questions. All of these questions are run in both shared and separate contexts.
More information about the contexts can be found below.

### dataset/combined.xlsx
Contains all the questions & answers for 3 iterations of both shared and separate contexts. Contains labels for answers and explanations given by ChatGPT.

### dataset/combined_pair.xlsx
Contains the same data as **combined.xlsx** except for the questions that are independent i.e., not part of a multipart question.

### dataset/combined_analysis.xlsx
Contains the results and analysis of the four research questions. It also contains various illustrations of the results.

### dataset/combined_merged.xlsx
Questions with missing shared contexts are replaced with the answers for the separate context to easily fetch the data for 
RQ2 & RQ3 from a single column.


# Cite
If you use our work, please cite our corresponding [ICSTW paper]([[https://arxiv.org/abs/2302.03287](https://ieeexplore.ieee.org/document/10132255)])(https://ieeexplore.ieee.org/document/10132255):
```
@inproceedings{jalil2023chatgpt,
  title={Chatgpt and software testing education: Promises \& perils},
  author={Jalil, Sajed and Rafi, Suzzana and LaToza, Thomas D and Moran, Kevin and Lam, Wing},
  booktitle={2023 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW)},
  pages={4130--4137},
  year={2023},
  organization={IEEE}
}
```
