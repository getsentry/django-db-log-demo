from django.http import HttpResponse


CHOICES = (
    "Python",
    "JavaScript",
    "Ruby",
    "C"
)

VOTES = {}

INDEX_TEMPLATE = """
<html>
<body>
<h1>Welcome to our Sentry's AI driven language study!</h1>
<p>Which programming language is the <strong>absolute best</strong>?</p>
<ul>{choices}</ul>
</body>
<html>
"""

VOTE_TEMPLATE = """
<html>
<body>
<h1>The results so far...</h1>
<p>Which programming language is the <strong>absolute best</strong>?</p>
<ul>{choices}</ul>
</body>
<html>
"""


def index(request):
    return HttpResponse(INDEX_TEMPLATE.format(
        choices='\n'.join(['<li><a href="/vote/{}">{}</a></li>'.format(i, c) for i, c in enumerate(CHOICES)])
    ))



def vote(request, choice_id):
    global VOTES

    VOTES.setdefault(choice_id, 0)
    VOTES[choice_id] += 1

    total_votes = VOTES[choice_id] / sum(VOTES.values())

    return HttpResponse(VOTE_TEMPLATE.format(
        choices='\n'.join(['<li>{} - {}%</li>'.format(VOTES[i] / total_votes, c) for i, c in enumerate(CHOICES)])
    ))

    