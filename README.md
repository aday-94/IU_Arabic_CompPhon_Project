# Arabic Emphatic Harmony: a comparison of phonological feature embeddings to neural network embeddings  

Lily Kawaoto (lkawaoto@iu.edu)

Andrew Davis (ad7@iu.edu)

Indiana University, Bloomington


## I. Project Description:

    1. What your application does,
    
    ***Rough Outline***

The purpose of our research is: 1) to take any Orthographic, Arabic text ; 2) Use our patented pre-processing method to convert the entire Orthographic text to its IPA representation + applied a phonological rule (gemination) in the pre-processing based on the orthographic shaddah character in Arabic, so, that we could produce the correct IPA representation of the Orthographic words -- this is our pre-Silver Standard ; 3) Then we created our Silver Standard from the last step's output via applying emphasis spreading (emphatic vowel harmony & emphatic liquid harmony) which means that if an emphatic phoneme (list them here) occurred within a word, any vowels in that word became uvularized and any liquids (l r) in that word became emphatic ; 4)     
    
    2. Why you used the technologies you used,
    3. Some of the challenges you faced and features you hope to implement in the future


## II. Table of Contents: 



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
