from posts.models import Post
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from posts.serializers import PostSerializer
from rest_framework.response import Response
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPost(request):
    data = request.data
    print(data)
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.create(serializer.validated_data)
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPost(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePost(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.update(post, serializer.validated_data)
        return Response(serializer.data)
    return Response(serializer.errors)

    