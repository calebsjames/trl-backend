from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from trlapi.models import Reserve



class ReserveView(ViewSet):

    def retrieve(self, request, pk=None):
        """Get a single record"""
        try:
            reserve = Reserve.objects.get(pk=pk)
            # categories = Category.objects.filter(categorygame__)

            serializer = ReserveSerializer(reserve, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    # Get a list of all records
    def list(self, request):
        reserves = Reserve.objects.all()


        serializer = ReserveSerializer(
            reserves, many=True, context={'request': request})
        return Response(serializer.data)


    # Create a record
    def create(self, request):
        """Handle POST operations for reserves

        Returns:
            Response -- JSON serialized event instance
        """
        reserve = Reserve()
        reserve.dom = request.data["dom"]
        reserve.color = request.data["color"]
        reserve.manufacturer = request.data["manufacturer"]
        reserve.model = request.data["model"]
        reserve.size = request.data["size"]
        reserve.serialNumber = request.data["serialNumber"]
        reserve.notes = request.data["notes"]


        try:
            reserve.save()
            serializer = ReserveSerializer(reserve, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # Edit a record via PUT method
    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        reserve = Reserve.objects.get(pk=pk)

        reserve.dom = request.data["dom"]
        reserve.color = request.data["color"]
        reserve.manufacturer = request.data["manufacturer"]
        reserve.model = request.data["model"]
        reserve.size = request.data["size"]
        reserve.serialNumber = request.data["serialNumber"]
        reserve.notes = request.data["notes"]

        reserve.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # DELETE a single record 
    def destroy(self, request, pk=None):
        """DELETE requests for a single game
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            reserve = Reserve.objects.get(pk=pk)
            reserve.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Reserve.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ReserveSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Reserve
        fields = (
            'id', 'dom', 'color', 'manufacturer', 'model', 'size', 'serialNumber', 'notes'
            )
        
