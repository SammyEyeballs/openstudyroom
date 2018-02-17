from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<tournament_id>[0-9]+)/$',
        views.tournament_view,
        name='view'
    ),
    url(
        r'^create/$',
        views.TournamentCreate.as_view(success_url='/tournament/list/'),
        name='create'
    ),
    url(
        r'^list/$',
        views.tournament_list,
        name='list'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/settings/$',
        views.manage_settings,
        name='manage_settings'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/groups/$',
        views.manage_groups,
        name='manage_groups'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/brackets/$',
        views.manage_brackets,
        name='manage_brackets'
    ),
    url(
        r'^invite/(?P<tournament_id>[0-9]+)$',
        views.invite_user,
        name='invite_user'
    ),
    url(
        r'^quit/(?P<tournament_id>[0-9]+)//$',
        views.remove_players,
        name='remove_players'
    ),
    url(
        r'^save_players_order/(?P<tournament_id>[0-9]+)/$',
        views.save_players_order,
        name='save_players_order'
    ),
    url(
        r'^create-group/(?P<tournament_id>[0-9]+)/$',
        views.create_group,
        name='create_group'
    ),
    url(
        r'^create-bracket/(?P<tournament_id>[0-9]+)/$',
        views.create_bracket,
        name='create_bracket'
    ),
    url(
        r'^save-groups/(?P<tournament_id>[0-9]+)/$',
        views.save_groups,
        name='save_groups'
    ),
    url(
        r'^create-match/(?P<round_id>[0-9]+)/$',
        views.create_match,
        name='create_match'
    ),
    url(
        r'^create-round/(?P<bracket_id>[0-9]+)/$',
        views.create_round,
        name='create_round'
    ),
]
