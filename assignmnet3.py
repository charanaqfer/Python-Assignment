import unittest
import yaml
def get_clk_imp_info(imps,clks,dict1):
    out={}
    out["os"]=dict1["os"]
    out["browser"]=dict1["browser"]
    out["impressions"]=[]
    imp_id=set()
    clk_id=set()
    # out["ip"]=dict1["ip"]
    out["clicks"]=[]
    # out["matching_ids"]=[]
    for imp in imps:
        if imp['ip']==dict1['ip']:
            del imp['ip']
            out['impressions'].append(imp)
            imp_id.add(imp['id'])
    for clk in clks:
        if clk['ip']==dict1['ip']:
            del clk['ip']
            out['clicks'].append(clk)
            clk_id.add(clk['id'])
    out['matching_ids']=set(imp_id&clk_id)
    return out

class UnitTestClass(unittest.TestCase):
    def test_get_clk_imp_info(self):
        IO_yaml_path='/Users/charankumarrampelli/Python_assignment/assignment3_IO.yaml'
        with open(IO_yaml_path,'r') as yaml_file:
            data=yaml.safe_load(yaml_file)
        impressions1 = data.get('impressions1', [])
        clicks1 = data.get('clicks1', [])
        os_brow1 = data.get('os_brow1', {})

        impressions2 = data.get('impressions2', [])
        clicks2 = data.get('clicks2', [])
        os_brow2 = data.get('os_brow2', {})
        res1=get_clk_imp_info(impressions1,clicks1,os_brow1)
        res2=get_clk_imp_info(impressions2,clicks2,os_brow2)
        
        
        expected_res1 = data.get('expect_res1', {})
        expected_res2 = data.get('expect_res2', {})
        print(res1)
        print(res2)
        expected_res2['matching_ids']=set(expected_res2["matching_ids"])
        expected_res1['matching_ids']=set(expected_res1["matching_ids"])
        self.assertEqual(res1,expected_res1)
        self.assertEqual(res2,expected_res2)

if __name__=='__main__':
    unittest.main()
