# Political-Motivation-behind-French-EV-Promotion

In 2013, Bradley W. Lane and others identified two motivations for why governments seek to promote the electric car: risk management in response to ecological or energy concern versus industrial policy seeking an economic upgrade. In this framework, jurisdictions suite of policies falls in one of three categories: primary risk management, primary industrial policy, or a substantial blend of the two. By reading government documents, Lane concluded that France was an intermediate case with a substantial blend of industrial policy and risk management.

Lane’s framework of analysis provided useful guidelines, but it has been seven years and two government changes since their research. It is time to apply the theory on more recent policy texts to update our understanding of the intention of this French government on the French EV industry. Instead of repeating the conventional way of generating policy positions, this team project wishes to draw inspiration from computer sciences and explore a more efficient way of collecting and classifying text. By doing so, not only can we collect and process considerably sized corpus with fewer costs but also replace the intuitive understanding of the text to something more measurable, putting subjectivity in a more objective criterion. 

## Therefore, this project firstly wishes
1. to design a more efficient way of collecting text data from the open web by using Python web scrapping technique;
2. classify the scrapped text depending on their topic relevance with the Python language. 

## This repo is created for the team project of the course Python Programming for Data Scientists @Hertie School. It is organized as the following:
* folder "Dataset" collects two csv files "evsearch.csv" and "evarticle.csv" corresponding to the phased achievement by midterm report and the manuall-processed file for the final report. In the same folder, you can also find the iad_tuning_results prepared for lda model improvement. 

* folder "Code" contains both the web scrapping code in python and the code for later data analysis. There are two scrapy folder. "vehicule" is the old one contains my initial attempt to crawl the title, teaser and the publication date of the search result from the target website. "evarticles" is the scrapy framework that I created for the final report. I attached also the LDA topic modeling code in this folder. 

* folder "Literature Review" includes all references used in this project.

* folder "Reports & Feedbacks" combines both final versions of the project proposal, midterm report, and the final report, as well as feedbacks from the course instructors, and some screen shots or illustrations that I quoted in the reports drafting 

