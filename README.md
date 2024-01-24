# Swiss-Voting-Data-Analysis-and-Visualization-1848-2023

This repository contains a simple data analysis and visualization project focusing on Swiss votes over the years. The visualisation inspect extreme voting results, it emphasizes  the 95th and 5th quantiles of voting data to highlight the most and least popular voting trends, providing unique insights into the Swiss electoral landscape.

You can view the interactive graph here [Extreme Swiss Votes Interactive Graph](https://drive.google.com/file/d/1cgyHj4yRz-WSyCFovbt04L016R7_cFeA/view?usp=sharing)

The data used for this purpose comes from the University of Bern. The
Année Politique Suisse, based there, maintains a comprehensive data set
(Swissvotes) on all votes that have taken place since the founding of
the modern federal state in 1848 (<https://swissvotes.ch/page/dataset>) to 2023. 

Since the data set is very large (834 variables), following variables are selected: 


-   **volkja-proz** : Percentage of yes-votes out of valid votes
-   **ja-lager**: Sum of the voter shares of all parties that recommended their voters to vote "Yes", the yes camp
-   **datum**: Date of the voting day
-   **title_kurz_d**: Short version of the official title of the vote in German
-   **title_kurz_en**: Short version of the official title of the vote in English
-   **swissvoteslink**: Link to the vote
