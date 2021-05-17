from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	leagues = League.objects.all()
	teams = Team.objects.all()
	players = Player.objects.all()
	tarea1 = League.objects.filter(sport="Baseball")
	tarea2 = League.objects.filter(name__contains="Women")
	tarea3 = League.objects.filter(sport__contains="Hockey")
	tarea4 = League.objects.exclude(sport="Football")
	tarea5 = League.objects.filter(name__contains="Conference")
	tarea6 = League.objects.filter(name__contains="Atlantic")
	tarea7 = Team.objects.filter(location__contains="Dallas")
	tarea8 = Team.objects.filter(team_name__contains="Raptors")
	tarea9 = Team.objects.filter(location__contains="City")
	tarea10 = Team.objects.filter(team_name__startswith="T")
	tarea11 = Team.objects.order_by('location')
	tarea121 = Team.objects.order_by('team_name')
	tarea12 = tarea121.reverse()
	tarea13 = Player.objects.filter(last_name__contains="Cooper")
	tarea14 = Player.objects.filter(first_name__contains="Joshua")
	tarea15 = tarea13.exclude(first_name__contains="Joshua")
	tarea16 = Player.objects.filter(Q(first_name__contains="Alexander") | Q(first_name__contains="Wyatt"))
	lvl2tarea1p1 = League.objects.get(name="Atlantic Soccer Conference")
	lvl2tarea1 = Team.objects.filter(league=lvl2tarea1p1)
	
	lvl2tarea2p1 = Team.objects.get(location = "Boston", team_name = "Penguins")
	lvl2tarea2 = Player.objects.filter(curr_team=lvl2tarea2p1)


	lvl2tarea3 = Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="International Collegiate Baseball Conference"))))

	lvl2tarea4 = Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="American Conference of Amateur Football"))))
	#American Conference of Amateur Football

	#lvl2tarea5 = Team.objects.filter(league = League.objects.filter(sport = "Football"))
	lvl2tarea5 = Player.objects.filter(all_teams__in=Team.objects.filter(league__in=(League.objects.filter(sport='Soccer'))))

	lvl2tarea6 = Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia"))
	
	lvl2tarea7 = League.objects.filter(teams__in = lvl2tarea6)

	#lvl2tarea7 = League.objects.filter(teams__in=Team.objects.filter(curr_players__in=(Player.objects.filter(first_name="Sophia"))))
	
	lvl2tarea8p1 = Team.objects.exclude(location="Washington", team_name="Roughriders")
	
	lvl2tarea8 = Player.objects.filter(last_name="Flores", curr_team__in=lvl2tarea8p1)
	#lvl2 = Team.objects.filter(all_players).count()
	#lvl2tarea12 = Player.objects.filter(first_name = "Jonathan", last_name = "Brooks")[0]
	#print(lvl2tarea12)
	#lvl2tarea12p2 = lvl2tarea12.all_teams.all()

	lvl2tarea9p1 = Player.objects.get(first_name="Samuel", last_name="Evans")
	lvl2tarea9 = Team.objects.filter(all_players =lvl2tarea9p1)

	lvl2tarea10p1 = Team.objects.get(location="Manitoba")
	lvl2tarea10 = lvl2tarea10p1.all_players.all()

	lvl2tarea11p1 = Team.objects.get(location="Wichita", team_name="Vikings")
	lvl2tarea11p2 = lvl2tarea11p1.all_players.all()
	lvl2tarea11p3 = lvl2tarea11p1.curr_players.all()
	lvl2tarea11 = list(set(lvl2tarea11p2)-set(lvl2tarea11p3)) 	

	lvl2tarea12p1 = Player.objects.get(first_name="Jacob", last_name="Gray")
	lvl2tarea12 = lvl2tarea12p1.all_teams.all().exclude(location="Oregon", team_name="Colts")

	lvl2tarea13p1 = Player.objects.filter(all_teams__in =Team.objects.filter(league__in=(League.objects.filter(name="Atlantic Federation of Amateur Baseball Players"))))
	lvl2tarea13 = lvl2tarea13p1.filter(first_name="Joshua")
	

	lvl2tarea14all = Team.objects.annotate(Count('all_players'))
	#lvl2tarea14curr = Team.objects.annotate(Count('curr_players'))
	#lvl2tarea14 = lvl2tarea14all.union(lvl2tarea14curr)
	print(lvl2tarea14all[0].all_players)
	
	#print(lvl2tarea14)
	final = {}
	for team in lvl2tarea14all:
		if team.all_players__count > 11:
			final[team.team_name] = team.all_players__count
			print(team.team_name, " ", team.all_players__count)
		#print(team.team_name, " ",team.all_players__count + team.curr_players__count)
		#print(team.team_name, " ", team.all_players__count)
	print(final)

	lvl2tarea15 = Player.objects.annotate(Count('all_teams'))
	print(lvl2tarea15)
	lvl2tarea15ordered = lvl2tarea15.order_by('-all_teams__count')
	print(lvl2tarea15ordered)
	
	context = {
		'leagues': leagues,
		'teams': teams,
		'players': players,
		'tarea1': tarea1,
		'tarea2': tarea2,
		'tarea3': tarea3,
		'tarea4': tarea4,
		'tarea5': tarea5,
		'tarea6': tarea6,
		'tarea7': tarea7,
		'tarea8': tarea8,
		'tarea9': tarea9,
		'tarea10': tarea10,
		'tarea11': tarea11,
		'tarea12': tarea12,
		'tarea13': tarea13,
		'tarea14': tarea14,
		'tarea15': tarea15,
		'tarea16': tarea16,
		'lvl2tarea1': lvl2tarea1,
		'lvl2tarea2': lvl2tarea2,
		'lvl2tarea3': lvl2tarea3,
		'lvl2tarea4': lvl2tarea4,
		'lvl2tarea5': lvl2tarea5,
		'lvl2tarea6': lvl2tarea6,
		'lvl2tarea7': lvl2tarea7,
		'lvl2tarea8': lvl2tarea8,
		'lvl2tarea9': lvl2tarea9,
		'lvl2tarea10': lvl2tarea10,
		'lvl2tarea11': lvl2tarea11,
		'lvl2tarea12': lvl2tarea12,
		'lvl2tarea13': lvl2tarea13,
		'lvl2tarea14': final,
		'lvl2tarea15': lvl2tarea15ordered





	}
	return render(request, 'leagues/index.html', context)



def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")