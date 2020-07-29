from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from pollsapi.polls.models import Poll, Choice
from pollsapi.polls.serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from pollsapi.tenant.models import Client


class PollsViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PollSerializer

    def create(self, request):
        poll = request.data or {}
        created_by = Client.objects.get(tenant_uuid=request.META.get('HTTP_X_REQUEST_ID'))
        serializer_context = {
            "created_by": created_by
        }
        serializer = self.serializer_class(data=poll, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        pass

    def retrieve(self, request, pk):
        pass

    def list(self, request):
        queryset = Poll.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        pass


class ChoiceViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ChoiceSerializer

    def create(self, request):
        choice = request.data or {}
        poll = Poll.objects.get(id=choice.get('poll'))
        serializer_context = {
            "poll": poll
        }
        serializer = self.serializer_class(data=choice, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        pass

    def retrieve(self, request, pk):
        pass

    def list(self, request):
        pass

    def destroy(self, request, pk):
        pass


class VoteViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = VoteSerializer

    def create(self, request):
        vote = request.data or {}
        voted_by = Client.objects.get(tenant_uuid=request.META.get('HTTP_X_REQUEST_ID'))
        poll = Poll.objects.get(id=vote.get('poll'))
        choice = Choice.objects.get(id=vote.get('poll'))

        serializer_context = {
            "voted_by": voted_by,
            "poll": poll,
            "choice": choice
        }
        serializer = self.serializer_class(data=vote, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        pass

    def retrieve(self, request, pk):
        pass

    def list(self, request):
        pass

    def destroy(self, request, pk):
        pass
