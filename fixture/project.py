from selenium.webdriver.support.wait import WebDriverWait

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

    def wait_for_correct_current_url(self, desired_url):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5)
        wait.until(
            lambda driver: wd.current_url.endswith(desired_url))

    def open_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()
    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        self.open_project_by_name(name)
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.wait_for_correct_current_url('/manage_proj_delete.php')
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.open_projects_page()
        self.group_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
