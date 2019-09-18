import allure


class TestJenkins:
    @allure.step("练习测试步骤")
    def test001(self):
        allure.attach("练习附件", "练习附件内容")
        assert True
