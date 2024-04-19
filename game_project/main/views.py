from django.shortcuts import render, redirect
from main.models import Team, Season, Match, PointsTable
from django.http import HttpResponse ,JsonResponse, HttpResponseRedirect
from random import choice
from random import randrange
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from collections import OrderedDict
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.

def home(request):
    seasons = Season.objects.all().filter(completed=True)
    if Season.objects.last() == None:
        complete = True
    elif Season.objects.last().completed == False:
        complete = False
    else:
        complete = True
    return render(request, 'main/home.html', {'seasons': seasons, 'complete': complete})


def get_season(request, num):
    season = Season.objects.get(editon=num)
    total_matches = reversed(Match.objects.filter(season=season).filter(discription='league-match'))
    playoff_matches = reversed(Match.objects.filter(season=season).exclude(discription='league-match'))
    return render(request, 'main/season_detail.html', {'matches':total_matches, 'playoff':playoff_matches, 'season':season})

@login_required
def match(request, pk=None):
    if request.method == 'POST':
        matches = int(request.POST.get('matches'))
        try:
            last_season = Season.objects.last().editon
        except:
            last_season = 0

        if Season.objects.all().count() > 0:
            if not Season.objects.last().completed:
                return redirect('/')

        new_season = Season.objects.create(editon = (int(last_season) + 1), matches=matches, teams=Team.objects.all().count())
        PointsTable.objects.create(season=new_season)
        teams = Team.objects.all()
        season = new_season

        for i in range(matches):
            team_list = []
            emp_list = []
            for team in teams:
                team_list.append(team)

            while len(emp_list) < len(team_list):
                team1 = choice(team_list)
                team_list.remove(team1)
                team2 = choice(team_list)
                team_list.remove(team2)
                Match.objects.create(season=season, team1=team1, team2=team2)

        total_matches = Match.objects.filter(season=season)
        return redirect('/matches', {'matches':total_matches, 'season':season})

    season = Season.objects.last()
    total_matches = Match.objects.filter(season=season).filter(discription='league-match')
    return render(request, 'main/matches.html', {'matches':total_matches, 'season':season})


@login_required
def play(request, id):
    match = Match.objects.get(id=id)
    season = match.season
    team1 = match.team1
    team2 = match.team2
    dict = {'desc':match.discription}
    count1 = 0
    count2 = 1
    for i in range(1,9):
        if randrange(1,21)%2 == 0:
            count1 = count1 + 1
            if count1 == 4:
                match.winner = team1
                match.loser = team2
                dict['winner'] = team1.name
                dict['loser'] = team2.name
                match.completed = True

                if match.discription == 'Qualifier-1':
                    qf2 = Match.objects.get(season=season, discription='Qualifier-2')
                    qf2.team1 = match.loser
                    qf2.save()
                    final = Match.objects.get(season=season, discription='Final')
                    final.team1 = match.winner
                    final.save()
            
                if match.discription == 'Eliminator':
                    qf2 = Match.objects.get(season=season, discription='Qualifier-2')
                    qf2.team2 = match.winner
                    qf2.save()

                if match.discription == 'Qualifier-2':
                    final = Match.objects.get(season=season, discription='Final')
                    final.team2 = match.winner
                    final.save()

                if match.discription == 'Final':
                    season.winner = match.winner
                    print(match.winner)
                    season.runnerup = match.loser
                    print(match.loser)
                    season.completed = True
                    season.save()

                match.save()
                break
        
        else:
            count2 = count2 + 1
            if count2 == 4:
                match.winner = team2
                match.loser = team1
                dict['winner'] = team2.name
                dict['loser'] = team1.name
                match.completed = True

                if match.discription == 'Qualifier-1':
                    qf2 = Match.objects.get(season=season, discription='Qualifier-2')
                    qf2.team1 = match.loser
                    qf2.save()
                    final = Match.objects.get(season=season, discription='Final')
                    final.team1 = match.winner
                    final.save()
            
                if match.discription == 'Eliminator':
                    qf2 = Match.objects.get(season=season, discription='Qualifier-2')
                    qf2.team2 = match.winner
                    qf2.save()

                if match.discription == 'Qualifier-2':
                    final = Match.objects.get(season=season, discription='Final')
                    final.team2 = match.winner
                    final.save()

                if match.discription == 'Final':
                    season.winner = match.winner
                    print(match.winner)
                    season.runnerup = match.loser
                    print(match.loser)
                    season.completed = True
                    season.save()


                match.save()
                break
    return JsonResponse(dict)


def points_table(request, num):
    season = Season.objects.get(editon=num)
    table = PointsTable.objects.get(season=season)
    season_matches = Match.objects.filter(season=season).filter(completed=True).filter(discription='league-match')
    total_matches = Match.objects.filter(season=season).filter(discription='league-match').count()
    season_teams = []
    teams_data = {}

    for match in season_matches:
        if match.team1 not in season_teams:
            season_teams.append(match.team1)
            teams_data[match.team1] = {'total_matches':0, 'wins':0, 'losses':0, 'total_matches': 0}
        if match.team2 not in season_teams:
            teams_data[match.team2] = {'total_matches':0, 'wins':0, 'losses':0, 'total_matches': 0}
            season_teams.append(match.team2)

    for match in season_matches:
        winner = match.winner
        loser = match.loser
        teams_data[winner]['wins'] = teams_data[winner]['wins'] + 1 
        teams_data[winner]['total_matches'] = teams_data[winner]['total_matches'] + 1 
        teams_data[loser]['losses'] = teams_data[loser]['losses'] + 1 
        teams_data[loser]['total_matches'] = teams_data[loser]['total_matches'] + 1 

    return render(request, 'main/points_table.html', {'teams_data': teams_data, 'season': season, 'season_matches':season_matches, 'total_matches': total_matches})


def playoffs(request, num):
    if request.method == 'POST':
        data = json.loads(request.body)
        season = Season.objects.get(editon=int(data['season']))
        team1 = Team.objects.get(name=data['team1'])
        team2 = Team.objects.get(name=data['team2'])
        team3 = Team.objects.get(name=data['team3'])
        team4 = Team.objects.get(name=data['team4'])

        qf1 = Match.objects.get_or_create(season=season, team1=team1, team2=team2, discription='Qualifier-1')
        el = Match.objects.get_or_create(season=season, team1=team3, team2=team4, discription='Eliminator')
        qf2 = Match.objects.get_or_create(season=season, discription='Qualifier-2')
        final = Match.objects.get_or_create(season=season, discription='Final')
        return JsonResponse({'msg': 'done'})


def playoffs_play(request, num):
    season = Season.objects.get(editon=num)
    matches = Match.objects.filter(season=season).exclude(discription='league-match')
    return render(request, 'main/playoffs.html', {'season':season, 'matches':matches})
