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
                    if hasattr(code_being_tested, 'sum_larger'):
                        @timeout_decorator.timeout(1)
                        def test_sum_larger(self):
                            try:
                                self.assertEqual(code_being_tested.sum_larger([2,5,4,7,3,8],5), 15)
                                print('test_sum_larger passed\n')
                            except Exception as e:
                                print('test_sum_larger failed\n')
                                code_errors.append([code_being_tested, e])
                    
                    if hasattr(code_being_tested, 'car_type'):
                        @timeout_decorator.timeout(1)
                        def test_car_type(self):
                            try:
                                self.assertTrue(code_being_tested.car_type(9, 5001, True), 'M3')
                                print('test_car_type passed\n')
                            except Exception as e:
                                print('test_car_type failed\n')
                                code_errors.append([code_being_tested, e])

                    if hasattr(code_being_tested, 'sum_near_whole'):
                        @timeout_decorator.timeout(1)
                        def test_ok_sum_near_whole(self):
                            try:
                                import numpy as np
                                A = np.array([[1.0, 1.4, 1.8, 2.2],
                                              [2.6, 3.8, 3.4, 3.8],
                                              [4.2, 4.6, 0.9, 5.4],
                                              [5.8, 6.2, 6.6, 7.0],
                                              [1.0, 7.8, 8.2, 8.6]])
                                self.assertTrue(code_being_tested.sum_near_whole(A), 38.2)
                                print('test_sum_near_whole passed\n')
                            except Exception as e:
                                print('test_sum_near_whole failed\n')
                                code_errors.append([code_being_tested, e])

                suite = unittest.TestLoader().loadTestsFromTestCase(TestEksamen)
                unittest.TextTestRunner().run(suite)
                print('-----------------')
                print("Success")
                print('Writing error to file')
                with open('errorH22kveld.csv', 'a', encoding='utf-8') as f:
                    if code_errors:
                        f.write(f'{code_errors}\n')
                    else:
                        print('No errors in code')
            except Exception as e:
                print(f'Error in {module_name}: {e}')

if __name__ == '__main__':
    directories = ['oppgave1', 'oppgave2', 'oppgave3']
    run_tests_on_directory(directories)