# Study-on-ChatGPT

A study on the capabilities of ChatGPT on correctly answering classroom assignments.

## Installation

You can install the latest version of this software directly from github with pip:

```pip install git+https://github.com/mmabrouk/chatgpt-wrapper```

This will install chatgpt-wrapper and it's dependencies. Before starting the program, you will need to install a browser
in playwright (if you haven't already). The program will use firefox by default.

```playwright install firefox```

With that done, you should start up the program in install mode, which will open up a browser window.

```chatgpt install```

Log in to ChatGPT in the browser window, then stop the program.

## Usage

From the terminal or IDE run ```__main__``` in the ```__init__.py``` of the src folder.


## Dataset Description
Our dataset contains questions from a well-known software testing book **Introduction to Software Testing 2nd Edition** by Ammann and Offutt. 
We use all the text-book questions in Chapters 1 to 5 that have solutions available on the book’s official website. 

Our dataset contains 40 such questions from these five chapters. 31 questions out of the 40 are multipart questions and the rest 9 are independent.
This tool generates responses from the ChatGPT automatically for these questions. All of these questions are run in both shared and separate context.
More information about the contexts can be found below.

### Combined.xlsx
Contains all the questions & answers for 3 iterations of both shared and separate contexts. Contains labels for answers and explanations given by ChatGPT.

### Combined_pair.xlsx
Contains the same data as **combined.xlsx** except for the questions that are independent i.e., not part of a multipart question.

### Combined_analysis.xlsx
Contains the result and analysis of the four research questions. Besides, it contains various illustrations for the results.

### Combined-merged.xlsx
Questions with missing shared contexts are replaced with the answers for the separate context to easily fetch the data for 
RQ2 & RQ3 from a single column.

### examples folders
Contains examples of some interesting response categories.

### Case Study.pdf
Contains the following analysis:
- When responses are likely to be incorrect?
- What are the reasons for being incorrect?
- Can we fix it with prompt engineering?
- Case studies with actual examples.


## Separate Context Query
In separate context queries, we treat each of the 31 multipart questions as an independent question.
Each sub-question is asked in a separate chat thread.
Combining with the nine independent questions, a total of 40 questions are asked for each run. To evaluate the consistency in
ChatGPT’s responses, we collect a total of three runs for each question, which results in a total of 120 responses from ChatGPT.

## Shared Context Query
Our dataset contains six questions that contain total 31 multipart questions or sub-questions and nine questions that do not. 
These six sub-questions are asked in a chat thread that are shared with other sub-questions as long as the sub-questions 
refer to the same code or scenario. 


## More Questions??
Reach me out to: [sjalil@gmu.edu](mailto:sjalil@gmu.edu)
