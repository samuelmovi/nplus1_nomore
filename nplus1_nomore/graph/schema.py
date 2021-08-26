from graphene import List, ObjectType, Schema
from graphene_django import DjangoConnectionField, DjangoObjectType

from .models import Article, Comment


class CommentType(DjangoObjectType):

    class Meta:
        model = Comment
        only_fields = ('text',)


class ArticleType(DjangoObjectType):

    comments = List(CommentType)

    class Meta:
        model = Article
        only_fields = ('title', 'body')
        use_connection = True

    def resolve_comments(root, info, **kwargs):
        return root.comments.all()


class ArticleTypeGood(DjangoObjectType):
    """
    Optimized version of ArticleType,
    comments resolved by loader
    """

    comments = List(CommentType)

    class Meta:
        model = Article
        only_fields = ('title', 'body')
        use_connection = True

    def resolve_comments(root, info, **kwargs):
        return info.context.comments_by_article_id_loader.load(root.id)
        

class Query(ObjectType):
    """
    Optimization:
    - switch between options for articles and check the difference in performace
    """

    articles = DjangoConnectionField(ArticleType)
    # articles = DjangoConnectionField(ArticleTypeGood)


    def resolve_articles(root, info, **kwargs):
        return Article.objects.all()


schema = Schema(query=Query)
