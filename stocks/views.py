from django.shortcuts import render
from django.http import JsonResponse
from .balanceSheetQuery import userQuery
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
import json

class RegisterView(generic.CreateView):
    form_class      = UserCreationForm
    success_url     = reverse_lazy('login')
    template_name   = 'register.html'

class DetailsView(generic.CreateView):
    success_url     = reverse_lazy('profile')
    template_name   = 'accounts/profile.html'

def index(request):
    ticker = 'MSFT'
    try:
        user_query_instance = userQuery(ticker)

        lq_assets              = user_query_instance.getTotalAssetsLatestQuarter(ticker)
        lq_liabilities         = user_query_instance.getTotalLiabilitiesLatestQuarter(ticker)
        lq_equity              = user_query_instance.getTotalShareholderEquityLatestQuarter(ticker)
        lq_bookvalue           = user_query_instance.getBookValuePerShareLatestQuarter(ticker)
        lq_retainedearnings    = user_query_instance.getRetainedEarningsLatestQuarter(ticker)
        lq_ratio               = user_query_instance.getCurrentRatioLatestQuarter(ticker)
        lq_debttoequity        = user_query_instance.getDebtToEquityLatestQuarter(ticker)
        data = {
                'ticker':              ticker,
                'lq_assets':           lq_assets,
                'lq_liabilities':      lq_liabilities,
                'lq_equity':           lq_equity,
                'lq_bookvalue':        lq_bookvalue,
                'lq_retainedearnings': lq_retainedearnings,
                'lq_ratio':            lq_ratio,
                'lq_debttoequity':     lq_debttoequity,
         }
    
    except Exception as e:
            data = {'error': str(e)}

    return render(request, 'index.html', {'data': data})

def results(request):
    if request.method == 'GET':
        ticker = request.GET.get('ticker', '')
        selected_date = request.GET.get('date', None)
        try:
            user_query_instance = userQuery(ticker)

            quarterly_dates = set()
            annual_dates = set()
            for report in user_query_instance.data.get('quarterlyReports', []):
                quarterly_dates.add(report['fiscalDateEnding'])
            for report in user_query_instance.data.get('annualReports', []):
                annual_dates.add(report['fiscalDateEnding'])
            quarterly_dates = sorted(quarterly_dates)
            quarterly_dates = json.dumps(list(quarterly_dates))
            annual_dates = list(annual_dates)

            lq_assets              = user_query_instance.getTotalAssetsLatestQuarter(selected_date)
            lq_liabilities         = user_query_instance.getTotalLiabilitiesLatestQuarter(selected_date)
            lq_equity              = user_query_instance.getTotalShareholderEquityLatestQuarter(selected_date)
            lq_bookvalue           = user_query_instance.getBookValuePerShareLatestQuarter(selected_date)
            lq_retainedearnings    = user_query_instance.getRetainedEarningsLatestQuarter(selected_date)
            lq_ratio               = user_query_instance.getCurrentRatioLatestQuarter(selected_date)
            lq_debttoequity        = user_query_instance.getDebtToEquityLatestQuarter(selected_date)

            la_assets              = user_query_instance.getTotalAssetsLatestYear(selected_date)
            la_liabilities         = user_query_instance.getTotalLiabilitiesLatestYear(selected_date)
            la_equity              = user_query_instance.getTotalShareholderEquityLatestYear(selected_date)
            la_bookvalue           = user_query_instance.getBookValuePerShareLatestYear(selected_date)
            la_retainedearnings    = user_query_instance.getRetainedEarningsLatestYear(selected_date)
            la_ratio               = user_query_instance.getCurrentRatioLatestYear(selected_date)
            la_debttoequity        = user_query_instance.getDebtToEquityLatestYear(selected_date)
            data = {
                'ticker':              ticker,
                'lq_assets':           lq_assets,
                'lq_liabilities':      lq_liabilities,
                'lq_equity':           lq_equity,
                'lq_bookvalue':        lq_bookvalue,
                'lq_retainedearnings': lq_retainedearnings,
                'lq_ratio':            lq_ratio,
                'lq_debttoequity':     lq_debttoequity,
                'la_assets':           la_assets,
                'la_liabilities':      la_liabilities,
                'la_equity':           la_equity,
                'la_bookvalue':        la_bookvalue,
                'la_retainedearnings': la_retainedearnings,
                'la_ratio':            la_ratio,
                'la_debttoequity':     la_debttoequity,
                
            }
        except Exception as e:
            data = {'error': str(e)}

        return render(request, 'results.html', {'data': data, 'annual_dates': annual_dates, 'quarterly_dates': quarterly_dates})

def learn(request):
    return render(request,'learn.html')

@login_required
def profile(request):
    return render(request, 'account/profile.html')




