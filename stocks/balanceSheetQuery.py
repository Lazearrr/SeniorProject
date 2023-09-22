from dotenv import load_dotenv
import requests
import json
import os


class userQuery():
    def __init__(self, ticker):
        self.ticker = ticker
        load_dotenv()
        self.AV_APIKEY = os.environ.get('AV_APIKEY')
        
        if not self.AV_APIKEY:
            raise ValueError("AV API KEY NOT FOUND IN ENVIRONMENT VARIABLES")
        
        url       = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={self.ticker}&apikey={self.AV_APIKEY}'
        r         = requests.get(url)
        data      = r.json()
        self.data = data

    def get_data_by_date(self, report_type, metric, date=None):
        reports = self.data.get(report_type, [])
        if date:
            for report in reports:
                if report['fiscalDateEnding'] == date:
                    return report.get(metric, "Data not available")
        else:
            if reports:
                return reports[0].get(metric, "Data not available")
        return "Data not available"

    ##START OF QUARTERLY QUERIES##
    ######################################
    def getTotalAssetsLatestQuarter(self, date=None):
        if 'quarterlyReports' in self.data and self.data['quarterlyReports']:
            return self.data['quarterlyReports'][0]['totalAssets']
        else:
            return "Quarterly total assets data not available"

    def getTotalLiabilitiesLatestQuarter(self, date=None):
        if 'quarterlyReports' in self.data and self.data['quarterlyReports']:
            return self.data['quarterlyReports'][0]['totalLiabilities']
        else:
            return "Quarterly total liabilities data not available"  

    def getTotalShareholderEquityLatestQuarter(self, date=None):
        if 'quarterlyReports' in self.data and self.data['quarterlyReports']:
            return self.data['quarterlyReports'][0]['totalShareholderEquity']
        else:
            return "Quarterly total shareholder equity data not available"

    def getBookValuePerShareLatestQuarter(self, date=None):
        if 'quarterlyReports' in self.data and self.data['quarterlyReports']:
            shareHolderEquity = self.data['quarterlyReports'][0]['totalShareholderEquity']
            outStandingShares = self.data['quarterlyReports'][0]['commonStockSharesOutstanding']
            bookValuePerShare = float(shareHolderEquity) / float(outStandingShares)
            return str(bookValuePerShare)
        else:
            return "Either Shareholder Equity or outstanding shares data is unavailable" 

    def getRetainedEarningsLatestQuarter(self, date=None):
        if 'quarterlyReports' in self.data and self.data['quarterlyReports']:
            return self.data['quarterlyReports'][0]['retainedEarnings']
        else:
            return "Retained Earnings Data is Not Available at this time"
        
    def getPriceToBookRatioLatestQuarter(self):
        coming_soon = print("Price to book ratio is coming soon!")
        return coming_soon
    
    def getCurrentRatioLatestQuarter(self, date=None):
        if 'quarterlyReports' in self.data and self.data['quarterlyReports']:
            totalAssets      = self.data['quarterlyReports'][0]['totalAssets']
            totalLiabilities = self.data['quarterlyReports'][0]['totalLiabilities']
            ratio            = float(totalAssets) / float(totalLiabilities)
            return str(ratio)
        else:
            return "Either Total Assets or Liability Data is Unavailable"

    def getDebtToEquityLatestQuarter(self, date=None):
        if 'quarterlyReports' in self.data and self.data['quarterlyReports']:
            totalLiabilities       = totalLiabilities = self.data['quarterlyReports'][0]['totalLiabilities']
            totalShareholderEquity = self.data['quarterlyReports'][0]['totalShareholderEquity']
            debtToEquity           = float(totalLiabilities) / float(totalShareholderEquity)
            return str(debtToEquity)
        else:
            return "Either Total Liability or Shareholder Equity Data is currently unavailable"
    
    ## START OF YEARLY QUERYS ##
    ###################################
    def getTotalAssetsLatestYear(self, date=None):
        if 'annualReports' in self.data and self.data['annualReports']:
            return self.data['annualReports'][0]['totalAssets']
        else:
            return "annual total assets data not available"

    def getTotalLiabilitiesLatestYear(self, date=None):
        if 'annualReports' in self.data and self.data['annualReports']:
            return self.data['annualReports'][0]['totalLiabilities']
        else:
            return "annual total liabilities data not available"  

    def getTotalShareholderEquityLatestYear(self, date=None):
        if 'annualReports' in self.data and self.data['annualReports']:
            return self.data['annualReports'][0]['totalShareholderEquity']
        else:
            return "annual total shareholder equity data not available"

    def getBookValuePerShareLatestYear(self, date=None):
        if 'annualReports' in self.data and self.data['annualReports']:
            shareHolderEquity = self.data['annualReports'][0]['totalShareholderEquity']
            outStandingShares = self.data['annualReports'][0]['commonStockSharesOutstanding']
            bookValuePerShare = float(shareHolderEquity) / float(outStandingShares)
            return str(bookValuePerShare)
        else:
            return "Either Shareholder Equity or outstanding shares data is unavailable" 

    def getRetainedEarningsLatestYear(self, date=None):
        if 'annualReports' in self.data and self.data['annualReports']:
            return self.data['annualReports'][0]['retainedEarnings']
        else:
            return "Retained Earnings Data is Not Available at this time"
        
    def getPriceToBookRatioLatestYear(self):
        coming_soon = print("Price to book ratio is coming soon!")
        return coming_soon
    
    def getCurrentRatioLatestYear(self, date=None):
        if 'annualReports' in self.data and self.data['annualReports']:
            totalAssets      = self.data['annualReports'][0]['totalAssets']
            totalLiabilities = self.data['annualReports'][0]['totalLiabilities']
            ratio            = float(totalAssets) / float(totalLiabilities)
            return str(ratio)
        else:
            return "Either Total Assets or Liability Data is Unavailable"

    def getDebtToEquityLatestYear(self, date=None):
        if 'annualReports' in self.data and self.data['annualReports']:
            totalLiabilities       = totalLiabilities = self.data['annualReports'][0]['totalLiabilities']
            totalShareholderEquity = self.data['annualReports'][0]['totalShareholderEquity']
            debtToEquity           = float(totalLiabilities) / float(totalShareholderEquity)
            return str(debtToEquity)
        else:
            return "Either Total Liability or Shareholder Equity Data is currently unavailable"



# Use this function to run each functions and return on query so we display all at once
def main():
    user = userQuery()
    user.getInitBlob()

if __name__ == "__main__":
        main()