from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()


    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init group creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit group creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_projects_page()
        self.project_cache = None


    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("new test test")
