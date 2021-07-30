from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from trlapi.models import Aad



class AadView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            aad = Aad.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = AadSerializer(aad, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        aads = Aad.objects.all()


        serializer = AadSerializer(
            aads, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for aads

        Returns:
            Response -- JSON serialized event instance
        """
        aad = Aad()
        aad.dom = request.data["dom"]
        aad.manufacturer = request.data["manufacturer"]
        aad.model = request.data["model"]
        aad.serialNumber = request.data["serialNumber"]
        aad.notes = request.data["notes"]


        try:
            aad.save()
            serializer = AadSerializer(aad, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        aad = Aad.objects.get(pk=pk)

        aad = Aad()
        aad.dom = request.data["dom"]
        aad.manufacturer = request.data["manufacturer"]
        aad.model = request.data["model"]
        aad.serialNumber = request.data["serialNumber"]
        aad.notes = request.data["notes"]

        aad.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            aad = Aad.objects.get(pk=pk)
            aad.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Aad.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class AadSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Aad
        fields = (
            'id', 'dom', 'manufacturer', 'model', 'serialNumber', 'notes', 'user'
            )
        
