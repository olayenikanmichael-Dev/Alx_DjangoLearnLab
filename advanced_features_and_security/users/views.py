from django.shortcuts import render
from .models import Article
# Create your views here.
# Safe query: search articles by title
def search_articles(request):
    query = request.GET.get('q', '')
    # Using ORM to prevent SQL injection
    results = Article.objects.filter(title__icontains=query)
    return render(request, 'users/search_results.html', {'results': results})
