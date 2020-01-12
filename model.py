class Wine(models.Model):
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  price = models.IntegerField()
  points = models.IntegerField()
  class Meta:
          ordering = ('name',) 
  def __str__(self):
    return self.name+" : "+self.country+" : "+self.description+" : "+self.price+" : "+self.points