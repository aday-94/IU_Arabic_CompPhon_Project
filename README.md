# Arabic Emphatic Harmony: a comparison of phonological feature embeddings to neural network embeddings  

## Lily Kawaoto (lkawaoto@iu.edu) & Andrew S. Davis (ad7@iu.edu)

## LING-L645, Advanced Natural Language Processing, Final Project, Fall 2022
## Indiana University - Bloomington


### I. Project Description:

The purpose of our application is to be able to take **_any_** Arabic text, transcribe the text (characters _**and**_ diacritics) to its matching IPA representation in an effective and efficient mannger, and use this newly, created dataset to study the phonotactics of Arabic with the aid of machine learning. More specifically, our application allows us to apply specific phonological processes that occur in Arabic producing our Silver Standard which is an IPA representation of how the original, written Arabic text _would_ be spoken with respect to the emphatic harmony process demonstrated in our experiment.

Emphatic harmony occurs in Modern-Standard Arabic when an emphatic consonant (ص, ض, ط, ظ) is present in a word. The presence of an emphatic causes emphasis spreading to surrounding the vowels and liquids (/l/, /r/) within the word boundary. In our phonological model, this process is characterized by the feature [+RTR]. The IPA realization of emphasis spreading demonstrated in our Silver Standard is that the vowels become uvularized (i.e. /a/ -> [aʶ]) and the liquids become pharyngealized (i.e. /r/ -> [rˤ]).

Our phonological model is based on phonological features and feature geometry structures. Phonological features are unary and binary attributes of phonemes; think of them as the building blocks of phonemes. Feature Geometry is a form of phonology that allows us to take those features and model the hierachal structure of their organization within a language, dialect, or specific phoneme. The resulting structure becomes a visual representation of a language's sounds with respect to its phonological features.

The building of this application consisted of several sections. First, utilizing phonological features and feature geometry, we created a hierarchal structure modeling phonological features with relation to IPA characters for the Arabic language. Then, starting with the Commonvoice 11.0 Arabic dataset, we created an IPA representation of that dataset, our _**(pre-Silver Standard ; referred to as pre-SS in rest of readme)**_, and then processed it further by applying rules representing the phonological process of emphatic harmony -- the output of this is our **_(Silver Standard ; referred to as SS in rest of readme)_**. Finally, making use of machine learning techniques, we vectorized our phonological feature model as well as trained a neural network on our datasets to learn _**when**_ and **_where_** emphatic harmony should occur.

In the analysis of our results, we examined the cosine similarity scores between each character bigram for, both, the phonological feature & neural network models. Then, we checked to see which character bigrams had an increase in frequency from the pre-SS to the SS. Our hypothesis was that the character bigrams that would increase the most would be associated with the process of emphasis spreading and the results confirmed our hypothesis. Finally, we took a subset of character bigrams from, both, the phonological feature and neural network embeddings in order to compare similarity scores between the two models.

Most of the challenges encountered in this project were during the pre-processing of the dataset. Arabic text is known for being difficult to pre-process and utilize for machine learning experiments. Our original plan was to use Epitran to convert the orthographic text to IPA, however, there were too many errors and inconsistencies we found when manually inspecting the output. The program took several hours each time we tried processing the Arabic text through it which was inefficient as well as the fact that it didn't convert any of the diacritics (there are a little over a dozen in Arabic orthography) and since the diacritics represent many of the vowels, this presented an issue for our phonotactic research. Due to this, we decided to create our own pre-processing application that consisted of six steps to go from the Arabic Commonvoice 11.0 orthographic text to its accurate, IPA representation, pre-SS, and then two steps that apply the phonological processes of emphatic vowel harmony and emphatic liquid harmony to the pre-Silver Standard creating SS. 

Immediate next steps for our research include two directions: a) Incorporate Arabic dialects into our phonological feature model and pre-processing techniques to create dialect specific models and datasets, and, b) Apply more Arabic phonological processes to our data, so, that the Silver Standard becomes an even closer representation of how the original, Arabic text would be spoken.

## II. Table of Contents: 
Creating Dataset & Preprocessing Text

 I. Creating Dataset & Preprocessing Text 
 
 <p align="center"><img width="800" height="400" src="https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/L645-ArbOrtho.png"></p>

1. Download the [L645-Arabic-PreProcessing folder](https://github.com/lilykaw/IU_CompPhon_project/tree/main/L645-Arabic-PreProcessing)

2. Remove all English/non-Arabic characters from the text -- Run [Remove English](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/L645-ArbOrtho-RemoveEng.py)

3. Next, remove odd characters such as ligatures, random symbols, etc -- Run [Remove Odds](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/L645-ArbOrtho-RemoveOddChars.py)

4. Now, we need to apply the phonological process of gemination to the text **_before_** we convert it to the IPA. In Arabic, there is a diacritic called the "shaddah". When the shaddah diacritic is applied to a consonant, this signifies gemination which means this consonant is to be repeated. For example, /ظ/ is an Arabic consonant represented by the following IPA character /ðˤ/. However, if the Arabic consonant has a shaddah over it, like this /ظّ/, then the correct IPA representation is /ðˤðˤ/ after gemination is applied. -- Run [Shaddah - Arabic Gemination](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/L645-ArabicShaddah.py)

5. With gemination applied, we convert the majority of the Arabic, orthographic characters to their IPA equivalents -- Run [Arabic Consonants IPA](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/L645-ArabicConsonantsRegex.py)

6. The majority of short vowels are represented by the remaining diacritics, now we process those into their IPA counterparts -- Run [Arabic Diacritics IPA](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/L645-ArabicDiacriticsRegex.py)

7. Finally, we remove all punctuation marks and remaining symbols -- Run [Remove Arabic Punctuation](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/L645-ArabicRemovePunct.py)

The output of the last step is our [pre-SS dataset](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/f2k22data-step6-arbipa-removedpunct-phone1-gem.txt)

From here, we apply two more steps of pre-processing to create our SS dataset. They are:

1. Apply Emphatic Vowel Harmony to the dataset, so, that any vowel in a word containing an emphatic is realized as its uvularized form -- Run [Emphatic Vowel Harmony](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/L645-EmphasisRTRVowelHarmony.py)

2. Apply Emphatic Liquid Harmony to the dataset, so, that any liquid (/l/ or /r/) in a word containing an emphatic is realized as its pharyngealized form -- Run [Emphatic Liquid Harmony](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/L645-EmphasisRTRConsonantHarmony.py)

The output of this last step is our [SS dataset!](https://github.com/lilykaw/IU_CompPhon_project/blob/main/L645-Arabic-PreProcessing/f2k22data-step8-arbipa-phon2-emphasis-SS.txt)

See the images below of the pre-SS text as well as the SS text and notice the circled word. This word contains an emphatic consonant /sˤ/, the vowel /aː/, and the liquid /l/. Notice that in the SS text, after emphasis harmony for both vowels and liquids has been applied, the change in the IPA characters: /aː/ -> /aʶː/ and /l/ -> /lˤ/.

<p align="center"><img width="800" height="400" src="https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/L645-PreSS.png"><align="center"><img width="800" height="400" src="https://github.com/lilykaw/IU_CompPhon_project/blob/main/README_images/L645-SS.png"></p>


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
