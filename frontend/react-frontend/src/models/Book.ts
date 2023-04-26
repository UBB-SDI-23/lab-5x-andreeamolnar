import { PublishingHouse } from "./PublishingHouse";
import { Author } from "./Author";




export interface Book {
    id?: number;
    title: string;
    publishing_house: PublishingHouse;
    description:string;
    releasing_year: number;
    authors: Author[]
}




// class Book( models.Model):
//     title = models.CharField(max_length=100,default = "")
//     #author = models.ManyToManyField(Author, through= 'BookWithAuthors')
//     publishing_house = models.ForeignKey( PublishingHouse, related_name = "books", on_delete = models.CASCADE)
//     description = models.TextField(default = "")
//     releasing_year = models.IntegerField(default = 0)
    
//     def __str__(self):
//         return self.title 