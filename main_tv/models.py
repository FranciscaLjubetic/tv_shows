from django.db import models

# Create your models here.
class Network(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Movie object: {self.title} ({self.id})>"

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    networks = models.ForeignKey(Network, related_name="curr_shows", on_delete = models.CASCADE)

    def __repr__(self):
        return f"<Movie object: {self.title} ({self.id})>"


    #netforgumball = Network.objects.get(title = 'Netflix')
    #netformandalorian = Network.objects.get(title = 'Disney+')
    #netforgot = Network.objects.get(title = 'HBO')
    #Show.objects.create(title='Game of Thrones',release_date= '2010-05-13 00:00:00', description='Fictional Middle Ages on the continent of Westeros. Intrigue, fantasy.', networks= netforgot)
    #Show.objects.create(title='Hilda',release_date= '2016-08-24 00:00:00', description='A little girl surrounded by supernatural friends.', networks= netforgumball)
    #Show.objects.create(title='Barry',release_date= '2021-02-15 00:00:00', description='Gangsters.', networks= netforgot)
    #Show.objects.create(title='Chernobyl',release_date= '2019-05-06 00:00:00', description='In April 1986, the city of Chernobyl in the Soviet Union suffers one of the worst nuclear disasters in the history of mankind. Consequently, many heroes put their lives on the line to save Europe.', networks= netforgot)
    #Show.objects.create(title='Mandalorian',release_date= '2019-11-12 00:00:00', description='After the defeat of the Empire at the hands of Rebel forces, a lone bounty hunter operating in the Outer Rim, away from the dominion of the New Republic, goes on many surprising and risky adventures.', networks= netformandalorian)
    #Show.objects.create(title='Gravity Falls',release_date= '2012-06-15 00:00:00', description='Twins Dipper and Mabel travel to the mysterious town of Gravity Falls in Oregon for their summer vacations but are shocked after they discover some strange occurrences.', networks= netformandalorian)
    #Show.objects.create(title='Miraculous: Tales Of Ladybug & Cat Noir',release_date= '2015-09-01 00:00:00', description='Marinette and Adrien, both in high school, are tasked with capturing akumas, creatures that make people evil. For this, both become superheroes but they do not know each other's identities.', networks= netformandalorian)
    #Show.objects.create(title='Dark',release_date= '2017-01-12 00:00:00', description='When two children go missing in a small German town, its sinful past is exposed along with the double lives and fractured relationships that exist among four families as they search for the kids. The mystery-drama series introduces an intricate puzzle filled with twists that includes a web of curious characters, all of whom have a connection to the town's troubled history -- whether they know it or not. The story includes supernatural elements that tie back to the same town in 1986.', networks= netforgumball)
    #Show.objects.create(title='Stranger Things',release_date= '2016-07-15 00:00:00', description='In 1980s Indiana, a group of young friends witness supernatural forces and secret government exploits. As they search for answers, the children unravel a series of extraordinary mysteries.', networks= netforgumball)