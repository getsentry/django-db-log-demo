from django.http import HttpResponse


CHOICES = (
    "Twitter",
    "Facebook",
    "Truthers Anonymous",
    "Only Fans"
)

NETWORKS = {}

INDEX_TEMPLATE = """
<html>
<body>
<h1>Welcome to Lifestrm!</h1>
<p>Which social network would you like to add</strong>?</p>
<ul>{choices}</ul>
</body>
<html>
"""

ADD_TEMPLATE = """
<html>
<body>
<h1>Great! We're working on it.</h1>
<p>By the way, here's how popular each social network has been..</p>
<ul>{choices}</ul>
</body>
<html>
"""


def index(request):
    return HttpResponse(INDEX_TEMPLATE.format(
        choices='\n'.join(['<li><a href="/add/{}">{}</a></li>'.format(i, c) for i, c in enumerate(CHOICES)])
    ))



def add(request, choice_id):
    global NETWORKS

    NETWORKS.setdefault(choice_id, 0)
    NETWORKS[choice_id] += 1

    total_networks = NETWORKS[choice_id] / sum(NETWORKS.values())

    return HttpResponse(ADD_TEMPLATE.format(
        choices='\n'.join(['<li>{} - {}%</li>'.format(NETWORKS[i] / total_networks, c) for i, c in enumerate(CHOICES)])
    ))

    