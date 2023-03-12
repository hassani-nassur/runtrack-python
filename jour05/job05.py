def nombreMetreMarche( nombreMarche, hauteurMarche):
    metre = 2 * nombreMarche * (hauteurMarche *0.01)
    metreParSemaine = 7 * metre
    txt = "pour {} marche de {} cm, le gardien parcours {} m par semaine"
    return txt.format(nombreMarche,hauteurMarche,metreParSemaine)

print(nombreMetreMarche( 12,40))
    