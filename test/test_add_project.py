from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()

    #old_projects = db.get_project_list()
    app.project.create(Project(name="test"))
    #new_project = db.get_project_list()
    #old_projects.append(project)
    #assert sorted(old_projects, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
    #if check_ui:
    #    for project in new_projects:
    #        project.name = project.name.rstrip()
    #    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)