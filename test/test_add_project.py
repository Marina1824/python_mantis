from model.project import Project

def test_add_project(app, db):
    app.project.open_projects_page()
    project_new = Project(name="new project test")
    old_projects = app.soap.get_project_list()
    app.project.create(project_new)
    new_projects = app.soap.get_project_list()
    old_projects.append(project_new)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)