from model.project import Project

def test_add_project(app, db):
    app.project.open_projects_page()
    project_new = Project(name="project new")
    old_projects = db.get_project_list()
    app.project.create(project_new)
    new_projects = db.get_project_list()
    old_projects.append(project_new)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)