import os
import unittest
import importlib
from unittest.mock import patch

import H21.fasit as export1

code_errors = []

class TestEksamen(unittest.TestCase):
   
    def test_alfa(self):
        try:
            self.assertEqual(export1.alfa('manus', 0), 'a')
            self.assertEqual(export1.alfa('manus', 1), 'u')
            self.assertEqual(export1.alfa('manus', 'abc'), 'u')
            self.assertEqual(export1.alfa('manus', None), 'u')
            print('test_alfa passed\n')
        except Exception as e:
            print('test_alfa failed\n')
            code_errors.append(e)
    def test_ant_land(self):
        try:
            self.assertEqual(export1.ant_land({'Belgia': ['Bryssel', 'Gent', 'Liege', 'Namur'], 'Polen':['Lodz']}), 2)
            self.assertEqual(export1.ant_land({'Irland': ['Dublin'], 'Belgia': ['Gent', 'Liege', 'Namur'],'Japan': [] }), 3)
            print('test_ant_land passed\n')
        except Exception as e:
            print('test_ant_land failed\n')
            code_errors.append(e)

    def test_sjekk(self):
        try:
            self.assertEqual(export1.sjekk(3), 'odde')
            self.assertEqual(export1.sjekk(3.0), 'odde')
            self.assertEqual(export1.sjekk(3.1), 'des')
            self.assertEqual(export1.sjekk(4), 'par')
            self.assertEqual(export1.sjekk(4.2), 'des')
            print('test_sjekk passed\n')
        except Exception as e:
            print('test_sjekk failed\n')
            code_errors.append(e)

    def test_fjern_dup(self):
        try:
            self.assertEqual(export1.fjern_dup([1,4,3,2]),[1,4,3,2])
            self.assertEqual(export1.fjern_dup([1,4,4,3]),[1,4,3])
            self.assertEqual(export1.fjern_dup([2,2,3,3,3,1,4,1,1,1,1]),[2,3,1,4,1])
            print('test_fjern_dup passed\n')
        except Exception as e:
            print('test_fjern_dup failed\n')
            code_errors.append(e)

    def test_list_str(self):
        try:
            self.assertEqual(export1.list_str('abcdefX'), [])
            self.assertEqual(export1.list_str('fedcabYabcdef'), [])
            self.assertEqual(export1.list_str('xyzzy '), [])
            self.assertEqual(export1.list_str('abcdefSabcdefOabcdefSabcdef'), ['S', 'O', 'S'])
            self.assertEqual(export1.list_str('abcdef*abcdef'), ['*'])
            self.assertEqual(export1.list_str('abcdefPabcdefYabcdef'), ['P', 'Y'])
            print('test_list_str passed\n')
        except Exception as e:
            print('test_list_str failed\n')
            code_errors.append(e)
    
    def test_sjekk_to(self):
        try:
            self.assertEqual(export1.sjekk_to('051033'), 1)
            self.assertEqual(export1.sjekk_to('421033'), 2)
            self.assertEqual(export1.sjekk_to('052033'), 3)
            self.assertEqual(export1.sjekk_to('051099'), 5)
            self.assertEqual(export1.sjekk_to('422033'), 6)
            self.assertEqual(export1.sjekk_to('421099'), 10)
            self.assertEqual(export1.sjekk_to('422099'), 30)
            print('test_sjekk_to passed\n')
        except Exception as e:
            print('test_sjekk_to failed\n')
            code_errors.append(e)
    
    def test_finn_pris(self):
        matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
        try:
            self.assertEqual(export1.finn_pris(matvarer, 'ost'), 99)
            self.assertEqual(export1.finn_pris(matvarer, 'finnesikke'), 0)
            self.assertEqual(export1.finn_pris(matvarer, 'laks'), 59)
            self.assertEqual(export1.finn_pris(matvarer, 'lakks'), 0)
            self.assertEqual(export1.finn_pris(matvarer, 'middag'), 0)
            print('test_finn_pris passed\n')
        except Exception as e:
            print('test_finn_pris failed\n')
            code_errors.append(e)
    
    def test_oppdater_matvare(self):
        beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
        try:
            self.assertEqual(export1.oppdater_matvare(beholdning, 'kjøttdeig', -1), {'laks': 6, 'kjøttdeig': 13, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5})
            self.assertEqual(export1.oppdater_matvare(beholdning, 'kjøttdeig', -3), {'laks': 6, 'kjøttdeig': 10, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5})
            self.assertEqual(export1.oppdater_matvare(beholdning, 'laks', 2), {'laks': 8, 'kjøttdeig': 10, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5})
            self.assertEqual(export1.oppdater_matvare(beholdning, 'bønner', 4), {'laks': 8, 'kjøttdeig': 10, 'ris': 15, 'ost': 9, 'bønner': 10, 'soyasaus': 0, 'banan': 5})
            print('test_oppdater_matvare passed\n')
        except Exception as e:
            print('test_oppdater_matvare failed\n')
            code_errors.append(e)
    
    def test_oppdater_beholdning(self):
        beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
        endringer = ['ost', 2], ['bønner', 4], ['laks', 2], ['kjøttdeig', -3]
        try:
            self.assertEqual(export1.oppdater_beholdning(beholdning, endringer), {'laks': 8, 'kjøttdeig': 11, 'ris': 15, 'ost': 11, 'bønner': 10, 'soyasaus': 0, 'banan': 5})
            print('test_oppdater_beholdning passed\n')
        except Exception as e:
            print('test_oppdater_beholdning failed\n')
            code_errors.append(e)
    
    def test_vis_priser(self):
        beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
        matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
        try:
            self.assertEqual(export1.vis_priser(beholdning, matvarer, 'bønner med soyasaus, og ris'), [('bønner',7),('soyasaus',33),('ris',15)])
            print('test_vis_priser passed\n')
        except Exception as e:
            print('test_vis_priser failed\n')
            code_errors.append(e)
    
    def test_salg(self):
        beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 5}
        matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
        try:
            self.assertEqual(export1.salg(matvarer, beholdning, ['laks', 'kjøttdeig', 'ris', 'ost', 'bønner', 'soyasaus', 'banan']), ('laks', 'kjøttdeig', 'ris', 'ost', 'bønner', 'banan'))
            print('test_salg passed\n')
        except Exception as e:
            print('test_salg failed\n')
            code_errors.append(e)

    def test_tilfeldig_middag(self):
        matvarer = [['laks', 59,'middag'], ['kjøttdeig', 25,'middag'],['ris', 15,'middag'], ['ost', 99,'frokost'], ['bønner', 7,'middag'],['soyasaus', 33,'middag'],['banan', 4,'mellommåltid']]
        try:
            self.assertEqual(export1.tilfeldig_middag(matvarer, 70), ['laks', 'bønner'])
            self.assertEqual(export1.tilfeldig_middag(matvarer, 50), ['ris', 'bønner', 'kjøttdeig'])
            print('test_tilfeldig_middag passed\n')
        except Exception as e:
            print('test_tilfeldig_middag failed\n')
            code_errors.append(e)

if __name__ == '__main__':
    unittest.main()
    print('Errors:', code_errors)