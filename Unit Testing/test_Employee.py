if __name__ == '__main__':
    import unittest
    from Employee import Employee

    class TestEmployee(unittest.TestCase):
        
        def setUp(self):
            self.e = Employee('Jonh Bob', 30, 1000.00)
        
        def tearDown(self):
            pass

        def test_name(self):
            with self.assertRaises(ValueError):
                self.e.name = 123
            with self.assertRaises(ValueError):
                self.e.name = '123'
            with self.assertRaises(ValueError):
                self.e.name = 'Jónh Bób'

            self.e.name = "Robert Bob"
            self.assertEqual(self.e.name, 'Robert Bob')
        def test_age(self):
            with self.assertRaises(ValueError):
                self.e.age = 'string'
            with self.assertRaises(ValueError):
                self.e.age = 10.6
            
            self.e.age = 18
            self.e.age

        def test_salary(self):
            with self.assertRaises(ValueError):
                self.e.salary = 'string'
            with self.assertRaises(ValueError):
                self.e.salary = 'çspecial çchar'
            
            self.e.salary = 100
            self.assertEqual(self.e.salary, 100.00)

        def test_salary_raise(self):
            with self.assertRaises(TypeError):
                self.e.salary_raise('string')
                
            self.e.salary_raise(100)
            self.assertEqual(self.e.salary, 1100.00)

    unittest.main()