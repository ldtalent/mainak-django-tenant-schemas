from rest_framework import serializers
from .models import Poll, Choice, Vote
from ..tenant.serializers import ClientSerializer


class PollSerializer(serializers.ModelSerializer):
    created_by = ClientSerializer(read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'pub_date', 'created_by')

    def create(self, validated_data):
        created_by = self.context.get('created_by', None)
        return Poll.objects.create(created_by=created_by, **validated_data)


class ChoiceSerializer(serializers.ModelSerializer):
    poll = PollSerializer(read_only=True, required=False)

    class Meta:
        model = Choice
        fields = ('id', 'poll', 'choice_text')

    def create(self, validated_data):
        poll = self.context.get('poll', None)
        return Choice.objects.create(poll=poll, **validated_data)


class VoteSerializer(serializers.ModelSerializer):
    voted_by = ClientSerializer(read_only=True)
    poll = PollSerializer(read_only=True)
    choice = ChoiceSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = ('id', 'choice', 'poll', 'voted_by')

    def create(self, validated_data):
        voted_by = self.context.get('voted_by', None)
        poll = self.context.get('poll', None)
        choice = self.context.get('choice', None)
        return Vote.objects.create(voted_by=voted_by, poll=poll, choice=choice)
