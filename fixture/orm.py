from pony.orm import *
from datetime import datetime
from model.project import Project


class ORMFixture:

    db = Database()

    class ORMProject(db.Entity):
        _table_ = "mantis_project_table"
        id = PrimaryKey(int, column='id')
        name = Optional(str, column='name')



    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_project_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), name=project.name)
        return list(map(convert, projects))


    @db_session
    def get_contact_list(self):
        return self.convert_project_to_model(select(c for c in ORMFixture.ORMProject))

    def destroy(self):
        self.db.disconnect()