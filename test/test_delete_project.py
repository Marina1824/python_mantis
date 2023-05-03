
from model.project import Project
import random

def test_delete_some_group(app, db):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="test462"))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
