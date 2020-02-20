class Record:
  name=team=pos=age=gp=mpg=fta=ftp=twpa=twpp=thpa=thpp=ppg=rpg=apg=spg=bpg=topg = None
  
  def __init__(self, name, team, pos, age, gp, mpg, fta, ftp, twpa, twpp, thpa, thpp, ppg, rpg, apg, spg, bpg, topg):
    self.name = name
    self.team = team
    self.pos = pos
    self.age = age
    self.gp = gp
    self.mpg = mpg
    self.fta = fta
    self.ftp = ftp
    self.twpa = twpa
    self.twpp = twpp
    self.thpa = thpa
    self.thpp = thpp
    self.ppg = ppg
    self.rpg = rpg
    self.apg = apg
    self.bpg = bpg
    self.topg = topg

    def __repr__(self):
      return f"<Record: {self.name} ({self.team}) | {self.pos}>"
