from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
from .utils import get_customer_by_id, get_salesman_by_id, get_chart
from reports.forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home_view(request):
    sales_df = None
    sales_df_html = None
    positions_df = None
    positions_df_html = None
    manged_df = None
    manged_df_html = None
    chart = None
    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()
    no_data = None

    if request.method == "POST":
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")
        results_by = request.POST.get("results_by")

        # print(date_from, date_to, chart_type, sep="\n")

        ## Can aldo do it like this.
        # for data_name, data in search_form.data.items():
        #     print(f"{data_name} - {data}")

        sales_qs = Sale.objects.filter(
            created__date__gte=date_from, created__date__lte=date_to
        )

        if len(sales_qs) > 0:
            sales_df = pd.DataFrame(sales_qs.values())
            sales_df["customer_id"] = sales_df["customer_id"].apply(get_customer_by_id)  # type: ignore
            sales_df["salesman_id"] = sales_df["salesman_id"].apply(get_salesman_by_id)  # type: ignore
            sales_df["created"] = sales_df["created"].apply(lambda x: x.strftime("%Y-%m-%d"))  # type: ignore
            sales_df["updated"] = sales_df["updated"].apply(lambda x: x.strftime("%Y-%m-%d"))  # type: ignore

            sales_df.rename(
                columns={
                    "id": "sale_id",
                    "customer_id": "customer_name",
                    "salesman_id": "salesman_name",
                },
                inplace=True,
            )
            sales_df_html = sales_df.to_html()

            positions_data = []
            for sale in sales_qs:
                for position in sale.get_positions():
                    positions_data.append(
                        {
                            "position_id": position.id,
                            "sale_id": sale.id,  # type: ignore
                            "product": position.product,
                            "quantity": position.quantity,
                            "price": position.price,
                            # "created_at": position.created,
                        }
                    )
            positions_df = pd.DataFrame(positions_data)
            manged_df = positions_df.merge(sales_df, how="left", on="sale_id")
            manged_df = manged_df.groupby("transaction_id", as_index=False)[
                "price"
            ].agg("sum")
            positions_df_html = positions_df.to_html()
            manged_df_html = manged_df.to_html()

            chart = get_chart(chart_type, sales_df, results_by)
            print(chart)

        else:
            print("NO SALES  🥲 🥲 🥲 🥲")
            no_data = "No data available in this date range."

    context = {
        "search_form": search_form,
        "report_form": report_form,
        "sales_df": sales_df_html,
        "positions_df": positions_df_html,
        "manged_df": manged_df_html,
        "chart": chart,
        "no_data": no_data,
    }
    return render(request, "sales/home.html", context)


class SaleListView(LoginRequiredMixin,ListView):
    model = Sale
    template_name = "sales/main.html"


class SaleDetailView(LoginRequiredMixin,DetailView):
    model = Sale
    template_name = "sales/detail.html"
