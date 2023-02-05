# Guess the Poet - Data rhymes
***Guess the Poet*** is a *text analysis* project for dealing with the organization of a *poetry challenge*.

## Why
The organizer of a *poetry challenge* often faces substantial difficulties in the process of selecting the authors to include in the challenge. 

In order to set a fair difficulty level for the challenge the organizer has to weight up different factors including the **uniqueness** of the author writing style; the more identifiable a writing style, the easier is to link a specific poem to its author. 

On the other hand the goal of the organizer is to create a *not-too-easy* challenge in order to increase the competition among its students. Overall the aim of the challenge is to encourage the knowledge of the Italian literature and Italian poets.

> A **poetry challenge** is a challenge organized by school teachers in which the participant students have to guess the author of a poem. The only information provided is the body of the poem.

## How
The first part of the project is focused on the collection of poems from the Internet and the archiving of the poems into different folders with the purpose  of grouping them by author.

The collection process is held by a python script that consumes the URLs of the web pages containing the poems, scrapes the website searching for the body of the poem and saves the body of the poem in a ```<NOME DELL'AUTORE>/poesia%s.txt``` file, where ```<NOME DELL'AUTORE> ``` is a folder with the name of the author of the poems and ```%s``` is a progressive integer number starting from 1.

The second part of the project involves the cleaning, elaboration, sampling of the ```.txt```  files and the final classification.

In order to estimate the uniqueness of an author writing style we provide an Orange Workflow aimed at cleaning and sampling ```*.txt``` files containing poems. 
The Workflow includes also a Neural Network trained on 80% of the sampled poems.

After the cleaning up, sampling of poems and training of the Neural Network the Workflow proceeds to classify the remaining 20% of the poems and groups them by author.

## Files provided
The release of the project includes:

1. 	A folder called *File aggiuntivi* containing:
	
	*	Folder called *poeti* that stores five sub-folders containing poems of five different Italian authors;
	*	```report.pdf```, a file that contains a detailed report of the Orange Workflow and results;
	*	The python script ```webscraper3.py``` responsible for the web-scraping process and storage of ```.txt``` files;
	*	A file called ```words_to_be_deleted.txt``` used for the data cleaning process.

2. A presentation of the Workflow and project in pdf format (```Project_work.pdf```);
3. ```dataset.xlsx```, an Excel file that stores the poems one for each row
4. ```poeti_text_mining.ows```, the Orange Data Mining file containing the Workflow.

## More
The python script used for the web-scraping process is highly customizable by modifing the target folders according to the local environment and to the needs of the web-scraping activity.