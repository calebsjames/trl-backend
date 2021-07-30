from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from trlapi.models import MainParachute



class MainParachuteView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            mainParachute = MainParachute.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = MainParachuteSerializer(mainParachute, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        mainParachutes = MainParachute.objects.all()


        serializer = MainParachuteSerializer(
            mainParachutes, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for mainParachutes

        Returns:
            Response -- JSON serialized event instance
        """
        mainParachute = MainParachute()
        mainParachute.dom = request.data["dom"]
        mainParachute.color = request.data["color"]
        mainParachute.manufacturer = request.data["manufacturer"]
        mainParachute.model = request.data["model"]
        mainParachute.size = request.data["size"]
        mainParachute.serialNumber = request.data["serialNumber"]
        mainParachute.notes = request.data["notes"]


        try:
            mainParachute.save()
            serializer = MainParachuteSerializer(mainParachute, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        mainParachute = MainParachute.objects.get(pk=pk)

        mainParachute.dom = request.data["dom"]
        mainParachute.color = request.data["color"]
        mainParachute.manufacturer = request.data["manufacturer"]
        mainParachute.model = request.data["model"]
        mainParachute.size = request.data["size"]
        mainParachute.serialNumber = request.data["serialNumber"]
        mainParachute.notes = request.data["notes"]

        mainParachute.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            mainParachute = MainParachute.objects.get(pk=pk)
            mainParachute.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except MainParachute.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class MainParachuteSerializer(serializers.ModelSerializer):   
    class Meta:
        model = MainParachute
        fields = (
            'id', 'dom', 'color', 'manufacturer', 'model', 'size', 'serialNumber', 'notes'
            )
        
