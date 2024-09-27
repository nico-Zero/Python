from django.shortcuts import render, get_object_or_404
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report
from django.views.generic import ListView, DetailView, TemplateView

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from sales.models import Sale, Position, CSV
import csv
from django.utils.dateparse import parse_date
from products.models import Product
from customers.models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ReportListView(LoginRequiredMixin,ListView):
    model = Report
    template_name = "reports/main.html"


class ReportDetailView(LoginRequiredMixin,DetailView):
    model = Report
    template_name = "reports/detail.html"


@login_required
def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

@login_required
def create_report_view(request):
    if is_ajax(request):
        name = request.POST.get("name")
        remarks = request.POST.get("remarks")
        image = get_report_image(request.POST.get("image"))

        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name, remarks=remarks, image=image, author=author)

        # 4:28:41 in video before.

        return JsonResponse({"msg": "send"})
    return JsonResponse({})

@login_required
def render_pdf_view(request, pk):
    template_path = "reports/pdf.html"
    obj = get_object_or_404(Report, pk=pk)
    context = {"obj": obj}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")

    ## if download is enabled
    # response["Content-Disposition"] = 'attachment; filename="report.pdf"'
    # if display is enabled
    response["Content-Disposition"] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:  # type: ignore
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


class UploadTemplateView(LoginRequiredMixin,TemplateView):
    template_name = "reports/from_file.html"


@login_required
def csv_upload_view(request):
    print("file has been received.")

    if request.method == "POST":
        csv_file_name = request.FILES.get("file").name
        csv_file = request.FILES.get("file")
        obj, created = CSV.objects.get_or_create(file_name=csv_file_name)
        if created:
            obj.csv_file = csv_file
            obj.save()
            with open(obj.csv_file.path, "r") as f:
                render = csv.reader(f)
                render.__next__()
                for row in render:
                    transaction_id = row[1]
                    product = row[2]
                    quantity = int(row[3])
                    customer = row[4]
                    date = parse_date(row[5])

                    try:
                        product_obj = Product.objects.get(name=product)
                    except:
                        product_obj = None

                    if product_obj is not None:
                        customer_obj, _ = Customer.objects.get_or_create(name=customer)
                        salesman_obj = Profile.objects.get(user=request.user)
                        position_obj = Position.objects.create(
                            product=product_obj, quantity=quantity, created=date
                        )
                        sale_obj, _ = Sale.objects.get_or_create(
                            transaction_id=transaction_id,
                            customer=customer_obj,
                            salesman=salesman_obj,
                            created=date,
                        )
                        sale_obj.positions.add(position_obj)
                        sale_obj.save()
                return JsonResponse({"ex": False})
        else:
            return JsonResponse({"ex": True})
    return HttpResponse()
