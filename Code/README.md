
# Code Documentation

## Structural Setting:
I created the starter repo by typing the command: scrapy startproject tutorial in the windows prompt. This helped us to auto generate the right folder structure and necessary files for later calibration.

## Spider code writing:
The spider is set for the website 'https://www.gouvernement.fr/search/site/vehicules%2520electriques'. Here I used the class method to define our spider under the name “VehiculeSpider”. After learning about the basic knowledge of html structure from DataCamp, I copied the route of our targeted content in xpath format by using Firefox in-built developer tools. 

We consulted the instruction from Medium article “A Minimalist End-to-End Scrapy Tutorial (Part I)” to design the code for extracting the article content following the url extracted from search results. The final outcome is yield in the format of a csv file

## LDA Topic Modeling:

Our topic modeling used the **Lantent Dirichlet Allocation (LDA)** method using the Gensim library in jupyter notebook editor.

The Colab version is for more convenient editing of the code description and results presentation.

### LDA Implementation Outlines


1. Library import
2. Data cleaning
3. Preparing data for LDA analysis
4. Model training and result visualization
5. Parameters tuning and final results presentation

After validation, the final LDA model achieves a coherence score of 0.4784
