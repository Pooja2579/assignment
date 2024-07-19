from django.urls import path
from .views import (
    SignUpView, LoginView, UserSearchView, SendFriendRequestView,
    HandleFriendRequestView, ListFriendsView, ListPendingFriendRequestsView
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user_search'),
    path('friend-request/<int:user_id>/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('friend-request/<int:request_id>/<str:action>/', HandleFriendRequestView.as_view(), name='handle_friend_request'),
    path('friends/', ListFriendsView.as_view(), name='list_friends'),
    path('friend-requests/pending/', ListPendingFriendRequestsView.as_view(), name='list_pending_friend_requests'),
]
