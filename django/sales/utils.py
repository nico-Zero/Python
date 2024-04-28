import uuid, base64
from profiles.models import Profile
from customers.models import Customer
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns


def generate_code():
    code = str(uuid.uuid4()).upper()[:12]
    return code


def get_salesman_by_id(id):
    salesman = Profile.objects.get(id=id)
    return salesman


def get_customer_by_id(id):
    customer = Customer.objects.get(id=id)
    return customer


def __get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph


def __get_key(res_by):
    if res_by == "1":
        return "transaction_id"
    elif res_by == "2":
        return "created"


def get_chart(chart_type, data, results_by, **kwargs):
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(10, 5))
    key = __get_key(results_by)
    grouped_data = data.groupby(key, as_index=False)["total_price"].agg("sum")
    
    if chart_type == "1":
        print("Bar Chart")
        # plt.bar(grouped_data[key], data["total_price"])
        sns.barplot(x=key, y="total_price", data=grouped_data, hue=key)
    elif chart_type == "2":
        print("Pie Chart")
        plt.pie(data=grouped_data, x="total_price", labels=key)
    elif chart_type == "3":
        print("Line Chart")
        plt.plot(grouped_data[key], grouped_data["total_price"])
    else:
        print("Invalid chart type")

    plt.tight_layout()
    chart = __get_graph()
    return chart
