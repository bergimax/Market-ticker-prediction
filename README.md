# Market-ticker-prediction
First ML project about the recognition of the market ticker. Project for ML-zoomcamp course
---

## 1 - Problem description

A futures market is an auction market in which participants buy and sell commodities and futures contracts for delivery on a specified future date. Futures are exchange-traded derivative contracts that lock in future delivery of a commodity or security at a price set today.

Usually investors try to predict the future movement of the price into the market using metrics and indicators based on historical data, but the prediction isn't enough to develop a successful trading strategy. You can't focus only in the historical price, but you should consider a lot of things like the time and how long they eant to keep the trade. 

A lot of strategies are using trading guidelines and operators such as measure of risk as stop loss and take profit, however, there is a field growing in this sector established on statistical decision based on probabilities.

With this project i tried to elaborate the data, trying to predict the market ticker. A key aspect about this repository , it's that this is not intended to be a strategy because it doesn't have the components needed to enter and exit a position, or even risk management. If this project works, it's because each market has a proper values, different one to the other.

--- 

## 2 - Data
This dataset offers detailed, up-to-date information on precious metals futures. Futures are financial contracts obligating the buyer to purchase, and the seller to sell, a particular precious metal (such as gold, silver, platinum, etc.) at a predetermined future date and price.

The data was obtained from this repository (https://www.kaggle.com/datasets/guillemservera/precious-metals-data) that has data, from 2000 until october 2023, on several markets:
	  - Gold 
    - Silver
    - Platinum
    - Copper
    - Palladium

Important details about the data:
- The timezone is UTC
- The data updates daily
- The format of the data is: 
	- Date: The date the data was recorded. Format YYYY-MM-DD.
	- Open: Market opening price.
	- High: Highest price during the trading day.
	- Low: Lowest price during the trading day.
	- Close: Market closing price.
	- Volume: Number of contracts traded during the day.
	- Ticker: Market quotation symbol for the future.
	- Commodity: Name of the precious metal the future refers to.
 
In this dataset we decided to use the dataset with different commodities, in this way we don't have data related to the market. I uploaded the entire dataset in the repository. File: *all_commodities_data.csv*
The last data store in the data folder to train our model was obtained 20 october 2023
 
This data is processed using the ``train.py`` file store in the data folder.
Those markets have different price and flow, so i decided to change the data in something shared, like distances between the main important values:
	  - 'diff_oc': This is the distance between the open and the close of the day 
    - 'diff_ol': This is the distance between the open and the low of the day 
    - 'diff_oh': This is the distance between the open and the high of the day 
    - 'diff_cl': This is the distance between the close and the low of the day 
    - 'diff_ch': This is the distance between the close and the high of the day
    - 'diff_hl': This is the distance between the high and the low of the day 

We decided to eliminate some columns based on the Correlation Matrix Heatmap. With this matrix we showed the dependencies between columns. 
we cut:
	- ticker, because it's the same of commodity, but wrote under another form.
	- volume
	- open
	- high
	- low

The goal of this project is to predict the commoddity if we have open, close, high and low of the market.

---

## 3 - Structure of the repository

### DATASET
**all_commodities_data.csv**: Contains the full dataset
**Copper_data.csv**: Dataset to test the model and discover all the copper values
**Gold_data.csv**: Dataset to test the model and discover all the gold values
**Silver_data.csv**: Dataset to test the model and discover all the silver values
**Palladium_data.csv**: Dataset to test the model and discover all the palladium values
**Platinum_data.csv**: Dataset to test the model and discover all the platinum values

### Files
**MidTermProj.ipynb**: contains the notebook to explore the data and choose the model with the best results
**Pipfile and Pipfile.lock**: contains the dependencies to run the repo
**predict.py**: Contains the prediction using flask
**predict-test.py**: Contains some values to test the model
**mid_term_model.bin**: This is the model got from the train.py using Pickle
**train.py**: Contains the model with the best performance in the testing set, obtained using the notebook
**Dockerfile**: contains the image for the docker

---

## Loading final model in web service:

#### pipenv

The script *train.py* load the model : *mid_term_model.bin* and it can run in a separate virtual environment across its dependency files *Pipenv* and *Pipenv.lock*.
*flask* was used for the web deployment in *train.py* script.

- Install pipenv :
```
pip install pipenv
```
- Get a copy of project and dependencies, or clone the repository :
```
git clone [https://github.com/bergimax/Market-ticker-prediction]
```
- From the project's folder, run :
``` 
pipenv install
```
- All the dependencies should be automatically soddisfied, just verify.
- Run the web service using gunicorn inside the virtual environment:
```
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
```

#### Docker
There is also the file: *Dockerfile* in the repository, through this you can run the web service in a completely separate container :
- From the project directory, create the docker image :
```
docker build -t market_prevision .
```
- Run the docker image created:
```
docker run -it --rm -p 9696:9696 market_prevision
```

#### Test the local web service:

- To test the web service, in another terminal you can run the test script:
```
python predict-test.py
```
- Edit the market values to analize the data about some market, you should change the parameters in the file, you can get them from the smaller dataset present in this repo:
```
vi predict-test.py
```

---

#### Video of the service running :
I loaded a small video where you can see how the web service works : *sefvice.mp4* 

The video show the local web service starting in Docker, and how it works, evaluating different patients with different data.

I suggest to view it using VLC player.
