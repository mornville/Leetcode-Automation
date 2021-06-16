from selenium import webdriver
import time, sys
import os, shutil
from webdriver_manager.chrome import ChromeDriverManager
OPTS = webdriver.ChromeOptions()
OPTS.add_argument("--log-level=3")
OPTS.headless = False
MAX_NO_OF_TRIES = 20
DRIVER = webdriver.Chrome(ChromeDriverManager().install(), options=OPTS)
PARENT_DIR = "Problems"
LANGUAGE_EXT = {
    "python":".py",
    "python3":".py",
    "java":".java",
    "csharp":".cs",
    "cpp":".cpp",
    "javascript":".js",
    "c":".c",
    "ruby": ".rb",
    "go":".go",
    "swift":".swift",
    "typescript":".ts",
    "php":".php"

}
class Scrape:
    def __init__(self) -> None:
        self.findClassTry = 0
    def waitForElementToLoad(self, className, class_or_id):
        try:
            if class_or_id == "class":
                element = DRIVER.find_element_by_class_name(className)
            else:
                element = DRIVER.find_element_by_id(className)   
            self.findClassTry = 0
            return element
        except:
            self.findClassTry += 1
            if(self.findClassTry > MAX_NO_OF_TRIES):
                return None
            else:
                print("Waiting for the webpage..")
                print("(element name: " + className + ")")
                time.sleep(3)
            self.waitForElementToLoad(className, class_or_id)

    def login(self, username, password):
        ## Get username element
        usernameElement = self.waitForElementToLoad("id_login", "id")
        if(usernameElement):
            passwordElement = self.waitForElementToLoad("id_password", "id")
            if(passwordElement):
                usernameElement.send_keys(username)
                passwordElement.send_keys(password)
                time.sleep(1)
                DRIVER.find_element_by_id("signin_btn").click()
                time.sleep(3)
                if(self.waitForElementToLoad("base_content", "id")):
                    return True
        return False

    def get_problem_name_url(self):
        problems = {}
        try:
            table = DRIVER.find_element_by_class_name("table-striped")
            ## Select all option for listing all solved problems
            table.find_element_by_xpath(".//tbody[@class='reactable-pagination']/tr/td/span/select[@class='form-control']/option[text()='all']").click()
            ## Add url of the problem 
            tr = table.find_elements_by_xpath(".//tbody[@class='reactable-data']/tr")
            for item in tr:
                a = item.find_element_by_xpath(".//td[@label='Title']/div/a")
                link = a.get_attribute("href")
                name = a.text
                problems[name] = link
            return problems
        except Exception as e:
            print(e)
            return {}

if __name__ == "__main__":
    a = Scrape()
    DRIVER.get("https://leetcode.com/accounts/login")

    """ Add Username and password """
    if(not a.login("USERNAME", "PASSWORD")):
        print("Login Unsuccessful")
        sys.exit(0)
    print("Success Login")

    ## Get all solved problems list
    DRIVER.get("https://leetcode.com/problemset/all/?status=Solved")
    err_count = 0
    try:
        os.mkdir(PARENT_DIR)
    except Exception as e:
        print(e)
    print("\nGetting all problems information, please wait....")
    time.sleep(3)
    problems = a.get_problem_name_url()
    if len(problems) == 0:
        print("Couldn't find any solved problems, exiting. \n")
        sys.exit(0)
    print(str(len(problems)) + " Problems found.")

    ## Get problem question for its README.md and solution
    for idx, problem_name  in enumerate(problems):
        try:
            path = os.getcwd() + '/' + PARENT_DIR + '/' + str(idx+1) + '. ' + problem_name
            os.mkdir(path)
            DRIVER.get(problems[problem_name])
            ## Wait for page content to load
            a.waitForElementToLoad("app", "id")
            time.sleep(1)
            ## Write problem question inside readme.md
            with open(path + '/README.md', 'a+') as file:
                question_text = a.waitForElementToLoad("description__24sA", "class")
                title = '# ' + str(idx+1) + '. ' + problem_name
                diffi = "### Difficulty: " + question_text.find_element_by_xpath('.//div/div[@class="css-10o4wqw"]/div').text
                content = question_text.find_element_by_class_name("content__u3I1").text.replace('\n', ' <br/> ').replace("Example", "<br/><b>- Example</b>").replace("Constraints", "<br/><b>Constraints</b>")
                file.write(title + '\n' + diffi + '\n' + content)
                file.close()
            ## Go to submissions page for its latest accepted solution
            DRIVER.get(problems[problem_name] + '/submissions')
            a.waitForElementToLoad('status-column__3SUg', "class")
            submissions = DRIVER.find_elements_by_xpath(".//td[@class='status-column__3SUg']/a")
            for sub in submissions:
                if sub.text == "Accepted":
                    sub.click()
                    break
            DRIVER.switch_to.window(DRIVER.window_handles[-1])
            print(a.waitForElementToLoad("result_language", "id").text)
            language_ext = LANGUAGE_EXT.get(a.waitForElementToLoad("result_language", "id").text, ".txt")
            code = DRIVER.find_element_by_class_name("ace_content").text
            with open(path + '/' + (problem_name.replace(" ", '_') + language_ext), 'a+') as file:
                file.write(code)
                file.close()   
            time.sleep(1)
            print("\nfile created at " + path) 
            ## Close submissions tab and switch back to problems page        
            DRIVER.close()
            DRIVER.switch_to.window(DRIVER.window_handles[0])
            
        except Exception as e:
            print(e)
            err_count+=1
            print("Could not create file for " + problem_name + '\n')
            shutil.rmtree(path)

    print("Number of errors encountered: ", err_count) 

    
