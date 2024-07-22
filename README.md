# *De Novo* Design of Protein-Protein Interactions Modulators
Master's thesis presenting a framework to design protein-protein interactions modulators and a case study with modulators of NCS-1/Ric-8A and NCS-1/D2R

## Abstract
The process of drug development is inherently lengthy and costly, often taking over a decade and requiring substantial financial investment. Deep learning models offer a promising solution by enhancing both the exploration of the chemical space with generative models and the identification of potential drug candidates with property predictors. This master final project (MFP) focuses on generating modulators of protein-protein interactions (PPIs), which are important therapeutic targets due to their central role in numerous biological processes and their potential in treating various diseases.

We present a comprehensive framework for the *de novo* generation of PPI modulators, structured around three main pillars. First, we employ a diverse set of state-of-the-art molecular generators to effectively explore the chemical space, ensuring a wide range of molecular diversity. Second, we adapt existing research to develop a novel PPI bioactivity regressor, designed to predict the affinity of molecules to specific PPIs. This regressor guides the generative process toward compounds with high therapeutic potential. Third, we incorporate various auxiliary property filters, focusing on predicting toxicity, blood-brain barrier penetration capability, drug-likeness, synthetic accessibility, molecular similarity to known compounds, and the binding affinity to specific protein pockets. These filters are essential for eliminating low-quality compounds and refining the selection of viable candidates.

This framework is applied to generate modulators for two specific PPIs, NCS-1/Ric-8A and NCS-1/D2R. The resulting compounds are compiled into two virtual chemical libraries, which are currently undergoing furhter testing to identify new and effective modulators. This MFP highlights the potential of deep learning in drug discovery and proposes a robust methodology for developing targeted PPI modulators.

## Repository contents

```
├── Training_Data
│   ├── tox21.csv                  # Tox21 dataset
│   ├── BBBP.csv                   # BBBP dataset
│   ├── PPI_data                   # Protein-Protein interactions modulators regression and classification data
│   │   ├── Processed_reg_data
│   │   │   ├── ppi_train.csv
│   │   │   ├── ppi_test.csv
│   │   │   └── preprocessing_parameters.pkl
│   │   ├── PPI_reg.csv            
│   │   └── Class_folds          
│   ├── Protein_data               # Protein sequence and embedding data
│   │   ├── Protein_sequence.csv
│   │   ├── Protein_phy.csv        # Pre-calculated protein descriptors
│   │   └── Protein_embedding.csv  
├── Model_Checkpoints              # Finetuned models for generation of modulators of NCS-1/Ric-8A and NCS-1/D2R
│   ├── HierVAE
│   │   ├── HierVAE_ric8.ckpt.9
│   │   └── HierVAE_d2r.ckpt.4
│   ├── Taiga
│   │   ├── Taiga_ric8.pt
│   │   └── Taiga_d2r.pt
│   ├── FREED2
│   │   ├── FREED2_ric8.pth
│   │   └── FREED2_d2r.pth
│   ├── Bioactivity_Model
│   │   ├── Ensemble
│   │   │   └── bioactivity_model_0-9.model
│   │   └── model_class.py         # Class defining the multi task learning bioactivity model
│   ├── Toxicity_Model
│   └── BBBP_Model
└── Virtual_Chemical_Libraries     
│   ├── ncs1_ric8.csv              # 1129 modulating candidates
│   └── ncs1_d2r.csv               # 87 modulating candidates
└── master_final_project.pdf                     # Master's thesis
```

## References
The code for the models used can be consulted in the following repositories:
- HierVAE: (https://github.com/wengong-jin/hgraph2graph)
- Taiga: (https://github.com/eyalmazuz/MolGen)
- FREED++: (https://github.com/airi-institute/ffreed)
- MultiPPIMI: (https://github.com/sun-heqi/MultiPPIMI)
