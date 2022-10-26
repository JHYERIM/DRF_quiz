from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer

@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    article = articles[0]
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
