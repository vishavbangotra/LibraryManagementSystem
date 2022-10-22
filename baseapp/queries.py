## Writing reusable and loose coupled sql queries
class Query:
    getBookAll = "SELECT * FROM baseapp_book"
    selectBooksByName = "SELECT * FROM baseapp_book WHERE name like %s"
    getBookById = "SELECT * FROM baseapp_book WHERE id = %s"
    getStudentById = "SELECT * FROM baseapp_student WHERE reg_num = %s"
    getAllStudents = "SELECT * FROM baseapp_student"
