import os,sys
sys.path.append(os.getcwd())
from base.base import start
from page.pagenetwork import PageNetWork

class Test_Click:
    # def setup(self):
    #     self.driver = start()
    #     self.openwith = PageNetWork(self.driver)
    def test_click(self):
        # self.openwith.type_2G()
        print('1234')
    # def test_click_3(self):
    #     self.openwith.type_3G()

    # def teardown(self):
    #     self.driver.quit()
