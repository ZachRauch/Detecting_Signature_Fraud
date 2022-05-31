# Signature Classification
![img](./images/signature_banner.jpeg)
### Author 
Zachary Rauch: 
[LinkedIn](https://www.linkedin.com/in/zach-rauch/) |
[GitHub](https://github.com/ZachRauch)|
[Email](zach.rauch0@gmail.com)
## Overview
The aim of this analysis is to identify fraudulent signatures in a dataset. My audience here is ___. Using just a small dataset with only 300 sample I was able to create a classification model that accurately classifies fraudulent signatures _____.
---
## Business Understanding and Stakeholder
Currently institutions and businesses recognize signatures as the primary way of authenticating transactions. Signatures are used to sign checks, authorize documents and contracts, and validate credit card transactions. According to recent studies, check fraud costs banks about $900M a year with 22 percent of all fraudulent checks attributed to signature fraud. Therefor, creating an algorithm to identify signature fraud or flagging suspicious signatures for investigations is a valuable asset.
---
## Data 
The data was collected from kaggle [here](https://www.kaggle.com/datasets/divyanshrai/handwritten-signatures). The dataset contains just 300 samples of genuine and forged signatures from 30 people, of which 50 percent are genuine and 50 percent are forged. This is an ideal class balance when building and training a model but it is a rather small sample size. To train the model more effectively, image augmentation was performed to raise the training dataset from 240 images up to 3,360 images. 
---
## Methodology

---
## Results

---
## Conclusion

---
## Next Steps

---
## Direct Links

---
## Repository Structure
```
├── Data 
├── Workspace
├── images
├── .gitignore
├── READ.md
└── Signature_Classification.ipynb
```
## Citations

- [Business Understanding](https://towardsdatascience.com/signature-fraud-detection-an-advanced-analytics-approach-a795b0e588b2)

- [Data](https://www.kaggle.com/datasets/divyanshrai/handwritten-signatures)

Code References:

- [Image Augmentation](https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/)

- [VGG16 Reference](https://www.kaggle.com/code/raulcsimpetru/vgg16-binary-classification/notebook)

- [Keras Documentation](https://keras.io/api/)

Images:

- [Banner](https://www.adamsluka.com/forgery.html)

Streamlit References: 

- [Streamlit](https://streamlit.io/)

- [How to Run Streamlit Apps From Colab](https://medium.com/@jcharistech/how-to-run-streamlit-apps-from-colab-29b969a1bdfc) 

- [Code reference](https://github.com/jingxianho/streamlit-local-tunnel/blob/main/Streamlit_local_tunnel.ipynb)

- [NGROK](https://dashboard.ngrok.com/get-started/setup)

- [st.file_uploader to array](https://discuss.streamlit.io/t/png-bytes-io-numpy-conversion-using-file-uploader/1409)
