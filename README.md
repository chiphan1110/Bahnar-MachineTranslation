# Bahnar-MachineTranslation

This repository contain the implementation of the Machine Translation Model for Bahnar Language, including Bahnar-English, English-Bahnar, Bahnar-Vietnamese, Vietnames-Bahnar translation model.

## Dataset Preparation
### Data cleaning & processing
### Our Dataset
Folder structure: 
```bash
3-dataset
├───bdq-eng
│   ├───1-train
│   │   ├───1-without_aug
│   │   │   ├───before-split
│   │   │   │   ├───bdq-eng.bdq
│   │   │   │   └───bdq-eng.eng
│   │   │   └───train-val-split
│   │   │       ├───bdq-eng.train.bdq
│   │   │       ├───bdq-eng.train.eng
│   │   │       ├───bdq-eng.val.bdq
│   │   │       └───bdq-eng.val.eng
│   │   └───2-with_aug
│   │       ├───before-split
│   │       │   ├───bdq-vie-eng.bdq
│   │       │   └───bdq-vie-eng.eng
│   │       └───train-val-split
│   │           ├───bdq-vie-eng.train.bdq
│   │           ├───bdq-vie-eng.train.eng
│   │           ├───bdq-vie-eng.val.bdq
│   │           └───bdq-vie-eng.val.eng
│   └───2-test
│       ├───bdq-eng.test.bdq
│       └───bdq-eng.test.eng
└───bdq-vie
    ├───1-train
    │   ├───before-split
    │   │   ├───bdq-vie.bdq
    │   │   └───bdq-vie.vie    
    │   └───train-val-split
    │       ├───bdq-vie.train.bdq
    │       ├───bdq-vie.train.vie
    │       ├───bdq-vie.val.bdq
    │       └───bdq-vie.val.vie
    └───2-test
        ├───bde-vie.test.bdq
        └───bdq-vie.test.eng
        
```



