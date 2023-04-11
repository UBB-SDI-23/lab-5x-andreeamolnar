export interface PublishingHouse {
    name: string;
    headquarters: string;
    founding_year: number;
}



// class PublishingHouse ( models.Model):
//     name = models.CharField( max_length = 100)
//     headquarters = models.CharField ( max_length = 100)
//     founding_year = models.IntegerField(default = 0)

//     def __str__(self):
//         return self.name