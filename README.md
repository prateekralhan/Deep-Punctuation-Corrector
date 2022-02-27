# 📄 Deep Punctuation Corrector 🛠 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A simple streamlit based webapp to process text and correct punctuation built using "fullstop-punctuation-multilang-large" Model from Huggingface Transformers 🤗.

![text](https://user-images.githubusercontent.com/29462447/155897274-d13b864b-530c-4f79-a956-7f1d63b3d311.gif)
![doc](https://user-images.githubusercontent.com/29462447/155897279-285f5ab9-79eb-40fa-ab25-b15e5c21edd5.gif)

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Simply run the command: 
```
streamlit run app.py
```
3. Navigate to http://localhost:8501 in your web-browser.
4. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading audio files, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

## Results:
1. Perform punctuation correction on random text on the fly!
![1](https://user-images.githubusercontent.com/29462447/155897302-d8345d12-2392-40f1-9534-5f3ed07a8fdb.png)
![2](https://user-images.githubusercontent.com/29462447/155897300-725e4ab0-1bf7-4647-8edf-c5fb661cb147.png)

2. Upload your document ***(supports PDFs, Word Files, Text files)*** and perform correction of punctuation:
![doc](https://user-images.githubusercontent.com/29462447/155897279-285f5ab9-79eb-40fa-ab25-b15e5c21edd5.gif)

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
