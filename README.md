# nlpcourse
Elaboration on NLP tasks for Shahid Beheshti University
In this repository we will be specifying the course project guidelines and also finally once all projects are done, make the project available to public as opensource project. 
This project is part of NLP course in [Shahid Beheshti University](http://sbu.ac.ir). For more information on the NLP projects you can look at [NLP Lab Website.] (http://nlp.sbu.ac.ir/). 

Items that this project will cover

#Tasks 
For each of the below tasks there is an input and output format that needs to be defined. It is preferred that the formats to be unified to make more use of data in different tasks. 
## Tokenization & Segmentation
### Input File
In this task the input will be a plain text file (.txt) It will be UTF-8 encoded and can be very large (up to giga bytes). Normalization is out of scope for this competition as it is really hard to define a measure for it. What we can say here is that   

### Output File
With each input file the tools must produce a file with same name but a different  extension (.out)
The (.out) file is a tab delimited format.  Each line of the file starts with the token that is identified. The next entries will be used for other tasks (e.g. Stemming) For this task we only care about the first entry of each line. 
An empty line means end of a sentence.  
The whitespaces between the tokens should be ignored. (you must include them if they are in middle of the detected tokens). Following characters are considered white spaces: 
* \r
* \n 
* \t
* Normal Space
* No-width Space 

All other characters are considered to be tokens if not part of another token. 
For example for following sentence: 
> My new Ipad worth 300$ and I bought it by 10% off. But I don't like it.

Should be converted to: 
```
My
new
Ipad
worth
300
$
and 
I 
bought
it
by
10
%
off
.

But
I 
don't 
like
it
.

```

###  Reference File 
The test file will contain the same format file as output but with (.ref) extension. This file is the evaluation benchmark for the output file produced. 

### Evaluation Method 
For tokenization task based on the ref file that is provided, we will find the largest number of common lines between the output file and the reference file. 
The total score will be the sum of the scores you get from all input samples. 

For segmentation purpose, we do as following. One sentence tokens (until the empty line) are concatenated and any further whitespace will removed as well. Then we will count the number of matches between the sentences in the reference file and output file. 

> For evaluation purpose, all the characters are converted to lowercase for English language. But for persian text no further normalization is done. 
## Morphological Analysis 
TBC 

# How to participate 
This is a multi phase competition and the aim is to build a good test and evaluation set at the end. We also promote open-source culture to re-use each other's achievements. 
## Phase I: Write your code
Prepare your code and make it ready. Use whatever tool that you like. But consider the fact that you should be able to use your scripts on many files (each group will come up with a brand new test file) . At this stage there is no language or technology preference. But if we want to get something out of this competition we can put an standard on the language that is used. 
## Phase II: Prepare your test files 
Each group should write a test file. In one day every group is responsible to upload their input files to repository (Location and folder structure TBC) 

## Phase III: Run your code 
Download all of the input files and run your code on them.  Then upload your results back to the repository. 

## Phase IV: Upload the reference files 

Upload the reference files to the repository. 
Then we run our scoring algorithm on it and will announce the results. 

## Phase V: Upload your code 

Upload the code and scripts that you had to the repository. Also you have to write a small documentation for your code on how to run it and what method it uses. 

# Ethics 
We want to promote the open science culture and one of the main points for it is maturity and responsibility. So please make sure that whatever is uploaded is your own work. Even if you use an open source library please mention it on your documentation. Also uploaded results MUST be output of your program and no manual edition is accepted. 
If any violation of a fair competition is detected the matter will be reported to the instructor. 

# Q&A 
*What language we can write our code in?* You are free to use any language. We strongly suggest python language so for future we can consolidate your code. 
*How should I upload files to this project?* You should use Git. If you are not familiar with Git, search internet and learn the basics. 
*How I can ask my questions and clarify?* Please open an issue in this project and we will discuss it here is the link for it [Create a New Issue](https://github.com/sehsanm/sbunlpcourse/issues/new).
