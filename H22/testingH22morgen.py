import os
import unittest
import importlib
import time
import timeout_decorator

def run_tests_on_directory(directories):
    for current_directory in directories:
        test_files = [f for f in os.listdir(current_directory) if f.startswith('export') and f.endswith('.py')]
        for test_file in test_files:
            module_name = test_file[:-3]
            code_errors = []
            try:
                print(f'Testing {current_directory} : {module_name}')
                try:
                    code_being_tested = importlib.import_module(f'{current_directory}.{module_name}')
                except Exception as e:
                    print(f'Failed to import {module_name}:\n{e}\n')
                    code_errors.append([module_name, e])
                    continue

                class TestEksamen(unittest.TestCase):
                    if hasattr(code_being_tested, 'sum_except'):
                        @timeout_decorator.timeout(1)
                        def test_sum_except(self):
                            try:
                                self.assertEqual(code_being_tested.sum_except([3,4,3,7],3), 11)
                                print('test_sum_except passed\n')
                            except Exception as e:
                                print('test_sum_except failed\n')
                                code_errors.append([code_being_tested, e])
                    
                    if hasattr(code_being_tested, 'ok_size'):
                        @timeout_decorator.timeout(1)
                        def test_ok_size(self):
                            try:
                                self.assertTrue(code_being_tested.ok_size(110, 75, True), True)
                                self.assertTrue(code_being_tested.ok_size(120, 95, False), False)
                                self.assertTrue(code_being_tested.ok_size(100, 45, True), False)
                                print('test_ok_size passed\n')
                            except Exception as e:
                                print('test_ok_size failed\n')
                                code_errors.append([code_being_tested, e])

                    if hasattr(code_being_tested, 'count_local_min'):
                        @timeout_decorator.timeout(1)
                        def test_count_local_min(self):
                            try:
                                import numpy as np
                                A = np.array([[1.7, 1.4, 1.8, 2.2],[2.6, 3.8, 3.4, 3.8],[4.2, 4.6, 0.9, 5.4],[5.8, 6.2, 6.6, 7.3],[9.9, 7.8, 5.2, 8.6]])
                                self.assertTrue(code_being_tested.count_local_min(A), 3)
                                print('test_count_local_min passed\n')
                            except Exception as e:
                                print('test_count-local_min failed\n')
                                code_errors.append([code_being_tested, e])

                suite = unittest.TestLoader().loadTestsFromTestCase(TestEksamen)
                unittest.TextTestRunner().run(suite)
                print('-----------------')
                print("Success")
                print('Writing error to file')
                with open('errorH22morgen.csv', 'a', encoding='utf-8') as f:
                    if code_errors:
                        f.write(f'{code_errors}\n')
                    else:
                        print('No errors in code')
            except Exception as e:
                print(f'Error in {module_name}: {e}')

if __name__ == '__main__':
    directories = ['oppgave1', 'oppgave2', 'oppgave3']
    run_tests_on_directory(directories)