
export interface Author {
    id?: number;
    first_name: string;
    last_name: string;
    nationality: string;
    date_of_birth: number;
    preponderent_genre: string;
}



// class Author ( models.Model):
//     first_name = models.CharField(max_length = 100,default = "")
//     last_name = models.CharField(max_length = 100,default = "")
//     nationality = models.CharField(max_length=100)
//     date_of_birth = models.IntegerField(default = 0)
//     preponderent_genre = models.CharField(max_length = 100,default = "")
   