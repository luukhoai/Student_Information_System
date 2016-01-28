--with temp_data as (select book_id, author_id, name, email from books_book_authors inner join books_author on books_book_authors.author_id = books_author.id and books_author.name = 'Author A')
--select book_id, author_id, title, publication_date, name, email from books_book inner join temp_data on books_book.id = temp_data.book_id

with temp_data as (select student_id, subject_id, middle_score, final_score from students_student inner join students_score on students_student.per_id = students_score.student_id and students_student.per_name = 'Alpha')
select sub_name, sub_code, sub_addr, middle_score, final_score from students_subject inner join temp_data on students_subject.sub_id = temp_data.subject_id