from lru import lru


class lruTest:

    def _init_(self):
        pass

    def testcases(self):
        a = lru(3)
        a.put("google")
        assert a.get("google") == "www.google.com", "testcase 1 failed"
        print("testcase 1 passed")
        a.put("facebook")
        assert a.get("facebook") == "www.facebook.com", "testcase 2 failed"
        print("testcase 2 passed")
        a.put("gmail")
        a.put("youtube")
        assert a.get("google") == None, "testcase 3 failed"
        print("testcase 3 passed")
        print("All Testcases passed!!")
        lst = a.get_cache()
        for i in lst:
            print(i)


if __name__ == "__main__":
    a = lruTest()
    a.testcases()