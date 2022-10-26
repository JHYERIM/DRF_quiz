from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
