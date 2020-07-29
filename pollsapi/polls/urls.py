from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pollsapi.polls.views import PollsViewSet, VoteViewSet, ChoiceViewSet

router = DefaultRouter()
router.register('polls', PollsViewSet, base_name='polls')
router.register('votes', VoteViewSet, base_name='votes')
router.register('choices', ChoiceViewSet, base_name='choices')

urlpatterns = [
    path('', include(router.urls)),
]
