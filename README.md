# Arabic Emphatic Harmony: a comparison of phonological feature embeddings to neural network embeddings  

## Lily Kawaoto (lkawaoto@iu.edu) & Andrew S. Davis (ad7@iu.edu)

## LING-L645, Advanced Natural Language Processing, Final Project, Fall 2022
## Indiana University - Bloomington


### I. Project Description:

    1. What your application does, -- DONE

Our application is to be able to take **_any_** Arabic text, transcribe the text (characters _**and**_ diacritics) to its matching IPA representation in an effective and efficient mannger, and use this newly, created dataset to study the phonotactics of Arabic with the aid of machine learning. More specifically, our application allows us to apply the specific phonological processes (such as emphatic harmony which is demonstrated in our experiment) that occur in Arabic producing a _Silver Standard_ which is an IPA representation of how the original, written Arabic text _would_ be spoken.

The building of this application consisted of several sections. First, utilizing phonological features and feature geometry, we created a hierarchal structure modeling phonological features with relation to IPA characters for the Arabic language. Then, starting with the Commonvoice 11.0 Arabic dataset, we created a an IPA representation of that dataset, _**pre-Silver Standard**_, and then processed it further by applying rules representing the phonological process of emphatic harmony -- the output of this is our **_Silver Standard_**. Finally, making use of machine learning techniques, we vectorized our phonological feature model as well as trained a neural network on our datasets to learn _**when**_ and **_where_** emphatic harmony should occur.

In the pre-processing of the dataset, our original plan was to use Epitran to convert the orthographic text to IPA, however, there were too many errors and inconsistencies we found when manually inspecting the output as well as the . Also, it didn't convert any of the diacritics (there are a little over a dozen in Arabic orthography) and since the diacritics represent many of the vowels, this presented an issue for our phonotactic research. Due to this, we created our own pre-processing application that pre-p

 
    ***Rough Outline***
    
The purpose of our research is: 1) to take any Orthographic, Arabic text ; 2) Use our patented pre-processing method to convert the entire Orthographic text to its IPA representation + applied a phonological rule (gemination) in the pre-processing based on the orthographic shaddah character in Arabic, so, that we could produce the correct IPA representation of the Orthographic words -- this is our pre-Silver Standard ; 3) Then we created our Silver Standard from the last step's output via applying emphasis spreading (emphatic vowel harmony & emphatic liquid harmony) which means that if an emphatic phoneme (list them here) occurred within a word, any vowels in that word became uvularized and any liquids (l r) in that word became emphatic ; 4) From here we used our proprietary Arabic Phonological Feature Model based on our own Feature Geometrical Structure to create feature embeddings and test their accuracy for predicting when and where emphasis should spread to vowels and liquids ; 5) We then extracted the character bigrams of the pre-SS and the SS standard and when analyzing the character bigrams of these two datasets, our hypothesis was validated, as the major difference was the addition of character bigrams associated with emphatic harmony ; 6) We then analyzed those character bigrams with respect to our hypotheses ; 7) We then trained a NN (LSTM) on SS-Train and then learned its feature embeddings of the ipa symbols ; 8) We used our PF model and NN model on Pre-SS & SS to learn when and where emphasis harmony should occur ; 9) Then, we compared:

1) the similarity scores between each character bigram for each the PF & NN models  

2) we see which 2-char combos had in increase in counts from preSS to SS 

3) we take that subset of combos and compare the sim score btwn PF embeds & NN embeds 

Overall, this program allows us to create a dataset from Arabic orthographic text, convert it to IPA, and use this dataset to train machine learning models for the purpose analyzing the phonotactics of Arabic; specifically with regards to phonological processes such as emphatic harmony.  
    
    2. Why you used the technologies you used,

***ROUGH OUTLINE***

We got our data from xxx database (Common Voice?) for Arabic data then ; 2) we originally were using Epitran’s Arabic Text preprocessing to convert the Arabic, orthographic text to its correct IPA representations, however, there were numerous issues with Epitran’s program: a) it took a long time (several hours) to process ; b) it had many, many leftover characters ; c) upon manual examination it was converting some orthographic characters to the incorrect IPA symbol ; d) it was splitting what is one word in orthography into two separate words in the IPA representation (have no idea how/why it did this as words are separated by white space in the original Arabic orthographic text) ; 3) After this multitude of issues, we decided to create our own program to do all of the preprocessing to create the Silver Standard according to the following steps:  
    
    3. Some of the challenges you faced and features you hope to implement in the future

***ROUGH DRAFT***

 Preprocessing: 

    Challenges were that Epitran didn’t work well at all; errors mentioned above 

    There are very unique challenges to preprocessing arabic text: multiple unicodes associated with one character, multiple styles of character that look the same, but have different unicodes, abjad meaning that vowels are written as diacritics and many issues with diacritics and preprocessing (numerous diacritics) and they are essential to create an accurate IPA representation of the arabic orthographic text. There were numerous odd characters such as ligatures and other symbols that had to be identified to process out. At the end there was a period of time where we had to go through a list of maybe two dozen left over variations of punctuations as well and preprocess them out. In terms of phonological processes, we ran into issues applying gemination (based on the shaddah character) to the IPA text, so, we applied the process of gemination to the orthographic text and then were able to convert it to IPA successfully.  


## II. Table of Contents: 
Creating Dataset & Preprocessing Text

 I. Creating Dataset & Preprocessing Text 

    Step 1 We removed all English characters from the data,  

    Step 2 We removed all “odd” characters – these were Arabic ligatures, random symbols such as the Soviet symbol, etc 

    Step 3 While the text was still in Arabic Orthography, we applied the phonological rule of gemination to process the text further. Gemination is when a phoneme is doubled/repeated. In Arabic, whenever there’s a shaddah diacritic (insert here) that means the Arabic, orthographic, consonant that it presides over undergoes the process of gemination (the character is doubled/repeated) 

    Step 4 We converted the majority of characters to their IPA equivalents (mainly consonants and long vowels) 

    Step 5 Then we converted the left over diacritics to their IPA equivalents 

    Step 6 Then we removed various forms of punctuation and other special characters 

    This is Pre-SS  

    Step 7 Then we applied the phonological process of Emphatic Vowel Harmony 

    Step 8 Then we applied the phonological process of Emphatic Liquid Harmony 

    This is SS 

Colab Notebook 

    Step 1. Import libraries 

    Step 2. Create phonological feature (PF) embeddings for each IPA character 

    Step 3. Read in pre-silver standard (preSS) and silver standard (SS) transcription texts 

            Get counts of all possible 2-character combinations in the preSS and SS 

    Debrief 1

    Step 4. Learn and extract neural network (NN) feature embeddings for each IPA character 

    Step 5. Visualize cosine similarity histograms of all IPA characters using PF and NN embeddings 

    Step 6. Qualitatively compare the cosine similarity scores of each 2-character pair that showed an increase in counts from the preSS to SS texts

    Debrief 2

    Step 7. Get OCP cluster hierarchical graphs 


## III. How to Install and Run the Project:

1. Copy [Arabic Emphatic Harmony.ipynb](https://colab.research.google.com/drive/1RwUR1gN7S30NM2al0vkGU-5itQQTyjY-?usp=sharing) to your own Google Colab directory.

2. Change Google Colab settings to run on GPU (Runtime > Change runtime type > choose ‘GPU’ in dropdown menu).
![](https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/change_runtime.png) ![](https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/change_to_gpu.png)
   
3. Download relevant project files and upload them to your Google Drive (there is also an option to download them directly from cells in the notebook).  
   - [Phonological feature chart](https://raw.githubusercontent.com/lilykaw/IU_CompPhon_project/main/L2_arb_ipa_S2K22.tsv)

   - [Pre- silver standard transcription](https://raw.githubusercontent.com/lilykaw/IU_CompPhon_project/main/f2k22data-step6-arbipa-removedpunct-phone1-gem.txt)

   - [Silver standard transcription](https://raw.githubusercontent.com/lilykaw/IU_CompPhon_project/main/f2k22data-step8-arbipa-phon2-emphasis-SS.txt)

   - [OCP clustering algorithm code](https://raw.githubusercontent.com/lilykaw/IU_CompPhon_project/main/ocpcluster.py) (if necessary)

4. Mount Google Drive to enable Colab to access files (file icon on the left sidebar > folder icon with Google Drive icon) 

<p align="center"><img width="350" height="400" src="https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/mount_drive.png"></p>

5. Run cells in notebook sequentially.  

## IV. How to Use the Project:

1. Import libraries

2. Create phonological feature embeddings for each IPA character 
   - Using the phonological feature chart, map each IPA character to a vector representation based on the presence, absence, or lack of a certain feature. This is stored in a dict() called `ipa2PFvec`. 
   - We will refer to this later to compute the cosine similarity score between 2 IPA characters. 

3. Read in pre-silver standard (`preSS`) and silver standard (`SS`) transcription texts 
   - Change `preSS` and `SS` file paths as necessary. 
   
   Get counts of all possible 2-character combinations in `preSS` and `SS` 
   - Respectively, they are stored in dicts `twochar_cnt_preSS` and `twochar_cnt_SS`
   - We can now compare which 2-character combination pairs increased from the `preSS` text to `SS` text. Since we know that the `SS` text is the output after phonological rules have been applied, combinations whose counts increased means an emphatic rule affected those characters. We take note of this subset of combinations by storing them in a set called `incr_twochar_cnt`. 

4. Learn neural network (NN) feature embeddings for each IPA character 
   - Encode the text and get batches to facilitate LSTM learning (`encoded`)
   - Input to the network is the encoded `SS` text 
   - After training, the model has learned weights for each IPA character. We take these weights and map them to their respective character, storing this mapping in a `dict()` called `ipa2NNvec`. 

5. Visualize cosine similarity histograms of PF and NN embeddings 

<p align="center"><img src="https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/cossim_pf_histogram.png" width="400" height="400"> <img src="https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/cossim_nn_histogram.png" width="400" height="400"></p>

6. Qualitatively compare the cosine similarity scores of each 2-character pair 
   - For each 2-character combination, get the similarity scores between each phoneme in the pair using (1) PF embeddings and (2) NN embeddings. Store in a Pandas dataframe called ‘sim_df’ and display. 

<p align="center"><img width="400" height="400" src="https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/cossim_comparison.png"></p>
   
   - The two phonological processes we investigate are RTR Vowel Harmony (RTR-VH)and RTR Consonant Harmony (RTR-CH). By filtering ‘sim_df’ so that only the scores of 2-character pairs that contain phonemes affected by RTR-VH and RTR-CH appear, we can more easily analyze the difference between cosine similarity scores produced by the PF embedding and NN embedding. 

7. Get OCP hierarchical cluster graphs 

   - Run the cells in this step to obtain files of the preSS and SS hierarchical cluster graphs. Note that Colab may not display some of the IPA characters correctly.  
   - In this case, please download a local copy of this Python code.  
     Usage: `python3 ocpcluster.py [PATH_TO_INPUT_TEXT]`


## V. Credits:
OCP phoneme clustering algorithm modified from https://github.com/cvocp/cvocp (Hulden 2017). 

Character LSTM code referenced from https://github.com/viritaromero/Character-Level-LSTM-in-Pytorch. 


## VI. License:
MIT License. See LICENSE.txt.
