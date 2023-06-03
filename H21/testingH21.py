
import os
import unittest
import importlib
import timeout_decorator
from unittest import mock

def run_tests_on_directory(directories):
    for current_directory in directories:
        print (current_directory)
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
                    if hasattr(code_being_tested, 'alfa'):
                        def test_alfa(self):
                            try:
                                self.assertEqual(code_being_tested.alfa('manus', 0), 'a')
                                self.assertEqual(code_being_tested.alfa('manus', 1), 'u')
                                self.assertEqual(code_being_tested.alfa('manus', 'abc'), 'u')
                                self.assertEqual(code_being_tested.alfa('manus', None), 'u')
                                print('test_alfa passed\n')
                            except Exception as e:
                                print('test_alfa failed\n')
                                code_errors.append([code_being_tested, e])
                    elif hasattr(code_being_tested, 'ant_land'):
                        def test_ant_land(self):
                            try:
                                self.assertEqual(code_being_tested.ant_land({'Belgia': ['Bryssel', 'Gent', 'Liege', 'Namur'], 'Polen':['Lodz']}), 2)
                                self.assertEqual(code_being_tested.ant_land({'Irland': ['Dublin'], 'Belgia': ['Gent', 'Liege', 'Namur'],'Japan': [] }), 3)
                                print('test_ant_land passed\n')
                            except Exception as e:
                                print('test_ant_land failed\n')
                                code_errors.append([code_being_tested, e])
                    elif hasattr(code_being_tested, 'sjekk'):
                        def test_sjekk(self):
                            try:
                                self.assertEqual(code_being_tested.sjekk(3), 'odde')
                                self.assertEqual(code_being_tested.sjekk(3.0), 'odde')
                                self.assertEqual(code_being_tested.sjekk(3.1), 'des')
                                self.assertEqual(code_being_tested.sjekk(4), 'par')
                                self.assertEqual(code_being_tested.sjekk(4.2), 'des')
                                print('test_sjekk passed\n')
                            except Exception as e:
                                print('test_sjekk failed\n')
                                code_errors.append([code_being_tested, e])

                    elif hasattr(code_being_tested, 'fjern_dup'):
                        @timeout_decorator.timeout(1)
                        def test_fjern_dup(self):  
                            try:    
                                self.assertEqual(code_being_tested.fjern_dup([1,4,3,2]),[1,4,3,2])
                                self.assertEqual(code_being_tested.fjern_dup([1,4,4,3]),[1,4,3])
                                self.assertEqual(code_being_tested.fjern_dup([2,2,3,3,3,1,4,1,1,1,1]),[2,3,1,4,1])
                                print('test_fjern_dup passed\n')
                            except Exception as e:
                                print('test_fjern_dup failed\n')
                                code_errors.append([code_being_tested, e])

                    elif hasattr(code_being_tested, 'list_str'):
                        @timeout_decorator.timeout(1)
                        def test_list_str(self):
                            try:
                                self.assertEqual(code_being_tested.list_str('abcdefX'), [])
                                self.assertEqual(code_being_tested.list_str('fedcabYabcdef'), [])
                                self.assertEqual(code_being_tested.list_str('xyzzy '), [])
                                self.assertEqual(code_being_tested.list_str('abcdefSabcdefOabcdefSabcdef'), ['S', 'O', 'S'])
                                self.assertEqual(code_being_tested.list_str('abcdef*abcdef'), ['*'])
                                self.assertEqual(code_being_tested.list_str('abcdefPabcdefYabcdef'), ['P', 'Y'])
                                print('test_list_str passed\n')
                            except Exception as e:
                                print('test_list_str failed\n')
                                code_errors.append([code_being_tested, e])

                    elif hasattr(code_being_tested, 'sjekk_to'):
                        @timeout_decorator.timeout(1)
                        def test_sjekk_to(self):
                            try:
                                self.assertEqual(code_being_tested.sjekk_to('051033'), 1)
                                self.assertEqual(code_being_tested.sjekk_to('421033'), 2)
                                self.assertEqual(code_being_tested.sjekk_to('052033'), 3)
                                self.assertEqual(code_being_tested.sjekk_to('051099'), 5)
                                self.assertEqual(code_being_tested.sjekk_to('422033'), 6)
                                self.assertEqual(code_being_tested.sjekk_to('421099'), 10)
                                self.assertEqual(code_being_tested.sjekk_to('422099'), 30)
                                print('test_sjekk_to passed\n')
                            except Exception as e:
                                print('test_sjekk_to failed\n')
                                code_errors.append([code_being_tested, e])

                    elif hasattr(code_being_tested, 'finn_pris'):
                        @timeout_decorator.timeout(1)
                        def test_finn_pris(self):
                            matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
                            try:
                                self.assertEqual(code_being_tested.finn_pris(matvarer, 'ost'), 99)
                                self.assertEqual(code_being_tested.finn_pris(matvarer, 'finnesikke'), 0)
                                self.assertEqual(code_being_tested.finn_pris(matvarer, 'laks'), 59)
                                self.assertEqual(code_being_tested.finn_pris(matvarer, 'lakks'), 0)
                                self.assertEqual(code_being_tested.finn_pris(matvarer, 'middag'), 0)
                                print('test_finn_pris passed\n')
                            except Exception as e:
                                print('test_finn_pris failed\n')
                                code_errors.append([code_being_tested, e])
                    
                    elif hasattr(code_being_tested, 'oppdater_matvare'):
                        def test_oppdater_matvare(self):
                            beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
                            try:
                                self.assertEqual(code_being_tested.oppdater_matvare(beholdning, 'kjøttdeig', -1), {'laks': 6, 'kjøttdeig': 13, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5})
                                self.assertEqual(code_being_tested.oppdater_matvare(beholdning, 'kjøttdeig', -3), {'laks': 6, 'kjøttdeig': 10, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5})
                                self.assertEqual(code_being_tested.oppdater_matvare(beholdning, 'laks', 2), {'laks': 8, 'kjøttdeig': 10, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5})
                                self.assertEqual(code_being_tested.oppdater_matvare(beholdning, 'bønner', 4), {'laks': 8, 'kjøttdeig': 10, 'ris': 15, 'ost': 9, 'bønner': 10, 'soyasaus': 0, 'banan': 5})
                                print('test_oppdater_matvare passed\n')
                            except Exception as e:
                                print('test_oppdater_matvare failed\n')
                                code_errors.append([code_being_tested, e])
                    
                    elif hasattr(code_being_tested, 'oppdater_beholdning'):
                        @timeout_decorator.timeout(1)
                        def test_oppdater_beholdning(self):
                            beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
                            endringer = ['ost', 2], ['bønner', 4], ['laks', 2], ['kjøttdeig', -3]
                            try:
                                self.assertEqual(code_being_tested.oppdater_beholdning(beholdning, endringer), {'laks': 8, 'kjøttdeig': 11, 'ris': 15, 'ost': 11, 'bønner': 10, 'soyasaus': 0, 'banan': 5})
                                print('test_oppdater_beholdning passed\n')
                            except Exception as e:
                                print('test_oppdater_beholdning failed\n')
                                code_errors.append([code_being_tested, e])
                    
                    elif hasattr(code_being_tested, 'vis_priser'):
                        @timeout_decorator.timeout(1)
                        def test_vis_priser(self):
                            beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
                            matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
                            try:
                                self.assertEqual(code_being_tested.vis_priser(beholdning, matvarer, 'bønner med soyasaus, og ris'), [('bønner',7),('soyasaus',33),('ris',15)])
                                print('test_vis_priser passed\n')
                            except Exception as e:
                                print('test_vis_priser failed\n')
                                code_errors.append([code_being_tested, e])
                    
                    elif hasattr(code_being_tested, 'salg'):
                        @timeout_decorator.timeout(1)
                        def test_salg(self):
                            beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
                            matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
                            try:
                                self.assertEqual(code_being_tested.salg(matvarer, beholdning, ['laks', 'kjøttdeig', 'ris', 'ost', 'bønner', 'soyasaus', 'banan']), ('laks', 'kjøttdeig', 'ris', 'ost', 'bønner', 'banan'))
                                print('test_salg passed\n')
                            except Exception as e:
                                print('test_salg failed\n')
                                code_errors.append([code_being_tested, e])

                    elif hasattr(code_being_tested, 'finn_pris'):
                        @timeout_decorator.timeout(1)
                        def test_finn_pris(self):
                            matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
                            try:
                                self.assertEqual(code_being_tested.finn_pris(matvarer, 'laks'), 59)
                                self.assertEqual(code_being_tested.finn_pris(matvarer, 'asdasdasd'), 0)
                                print('test_finn_pris passed\n')
                            except Exception as e:
                                print('test_finn_pris failed\n')
                                code_errors.append([code_being_tested, e])

                    elif hasattr(code_being_tested, 'oppdater_matvare'):
                        @timeout_decorator.timeout(1)
                        def test_oppdater_matvare(self):
                            beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
                            try:
                                self.assertEqual(code_being_tested.oppdater_matvare(beholdning, 'laks', 2), {'laks': 8, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5})
                                self.assertEqual(code_being_tested.oppdater_matvare(beholdning, 'banan', 3), {'laks': 8, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 8})
                            except Exception as e:
                                print('test_oppdater_matvare failed\n')
                                code_errors.append([code_being_tested, e])

                    elif hasattr(code_being_tested, 'oppdater_beholdning'):
                        @timeout_decorator.timeout(1)
                        def test_oppdater_beholdning(self):
                            beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
                            endringer = [['laks', 2], ['banan', 3]]
                            try:
                                self.assertEqual(code_being_tested.oppdater_beholdning(beholdning, endringer), {'laks': 8, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 8})
                                print('test_oppdater_beholdning passed\n')
                            except Exception as e:
                                print('test_oppdater_beholdning failed\n')
                                code_errors.append([code_being_tested, e])

                    elif hasattr(code_being_tested, 'vis_priser'):
                        @timeout_decorator.timeout(1)
                        def test_vis_priser(self):
                            beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
                            matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
                            try:
                                self.assertEqual(code_being_tested.vis_priser(beholdning, matvarer, 'bønner med soyasaus og ris'), [('bønner', 7), ('soyasaus', 33), ('ris', 15)])
                                self.assertEqual(code_being_tested.vis_priser(beholdning, matvarer, 'laks med ris og ost'),[('laks', 59), ('ris', 15), ('ost', 99)])
                                print('test_vis_priser passed\n')
                            except Exception as e:
                                print('test_vis_priser failed\n')
                                code_errors.append([code_being_tested, e])
                    
                    elif hasattr(code_being_tested, 'salg'):
                        @timeout_decorator.timeout(1)
                        def test_salg(self):
                            beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
                            matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
                            handleliste = ['ost','banan','banan', 'kjøttdeig', 'kjøttdeig']
                            try:
                                self.assertEqual(code_being_tested.salg(beholdning, matvarer, handleliste), ('ost', 'banan', 'banan', 'kjøttdeig', 'kjøttdeig'))
                                print('test_salg passed\n')
                            except Exception as e:
                                print('test_salg failed\n')
                                code_errors.append([code_being_tested, e])

                suite = unittest.TestLoader().loadTestsFromTestCase(TestEksamen)
                unittest.TextTestRunner().run(suite)
                print('-----------------')
                print("Success")
                print('Writing error to file')
                with open('errorH21.csv', 'a', encoding='utf-8') as f:
                    if code_errors:
                        f.write(f'{code_errors}\n')
                    else:
                        print('No errors in code')
            except Exception as e:
                print(f'Error in {module_name}: {e}')

if __name__ == '__main__':
    directories = ['oppgave2a', 'oppgave2b', 'oppgave2c', 'oppgave2g', 'oppgave2h', 'oppgave2i', 'oppgave3_1', 'oppgave3_2', 'oppgave3_3', 'oppgave3_4', 'oppgave3_5']
    run_tests_on_directory(directories)