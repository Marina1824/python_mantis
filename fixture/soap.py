from model.project import Project
from suds.client import Client
from suds import WebFault

class SoapHelper:


    def __init__(self, app, username, password):
        self.app = app
        self.username = username
        self.password = password

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        soap_projects = client.service.mc_projects_get_user_accessible(self.username, self.password)
        projects = []
        for i in range(len(soap_projects)):
            project = Project(name=soap_projects[i].name, id=soap_projects[i].id)
            projects.append(project)
        return projects