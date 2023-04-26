import { Book } from "./Book";


export interface PublishingHouse {
    id?: number;
    name: string;
    headquarters: string;
    founding_year: number;
    books?: Book[];
}



// class PublishingHouse ( models.Model):
//     name = models.CharField( max_length = 100)
//     headquarters = models.CharField ( max_length = 100)
//     founding_year = models.IntegerField(default = 0)

//     def __str__(self):
//         return self.name