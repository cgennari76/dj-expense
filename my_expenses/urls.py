from django.contrib import admin
from django.urls import path
from expenses.views import (HomepageView, BillListView,
                            PayrollListView, ExpensesListView,
                            report_view
                            )


from django.urls import path

def trigger_error(request):
    division_by_error = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'),
    path('bills/', BillListView.as_view(), name='bills_view'),
    path('payroll/', PayrollListView.as_view(), name='payroll_view'),
    path('expenses/', ExpensesListView.as_view(), name='expenses_view'),
    path('reports/', report_view, name='reports_view'),
    path('sentry-debug/', trigger_error)
]
