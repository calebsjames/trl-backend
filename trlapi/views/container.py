from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from trlapi.models import Container



class ContainerView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            container = Container.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = ContainerSerializer(container, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        containers = Container.objects.all()


        serializer = ContainerSerializer(
            containers, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for containers

        Returns:
            Response -- JSON serialized event instance
        """
        container = Container()
        container.dom = request.data["dom"]
        container.color = request.data["color"]
        container.manufacturer = request.data["manufacturer"]
        container.model = request.data["model"]
        container.size = request.data["size"]
        container.serialNumber = request.data["serialNumber"]
        container.notes = request.data["notes"]


        try:
            container.save()
            serializer = ContainerSerializer(container, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        container = Container.objects.get(pk=pk)

        container.dom = request.data["dom"]
        container.color = request.data["color"]
        container.manufacturer = request.data["manufacturer"]
        container.model = request.data["model"]
        container.size = request.data["size"]
        container.serialNumber = request.data["serialNumber"]
        container.notes = request.data["notes"]

        container.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            container = Container.objects.get(pk=pk)
            container.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Container.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ContainerSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Container
        fields = (
            'id', 'dom', 'color', 'manufacturer', 'model', 'size', 'serialNumber', 'notes'
            )
        
