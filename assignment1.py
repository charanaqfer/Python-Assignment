import yaml
import unittest
# Path to your YAML file
def statistics_of_yaml():
    yaml_file_path = '/Users/charankumarrampelli/Python_assignment/assign1.yaml'
    # Open the YAML file and load its content
    with open(yaml_file_path, 'r') as file:
        try:
            # Load the YAML content into a Python dictionary
            data = yaml.safe_load(file)
            map={} #eventype:{months:{min_count,max_year,min_year}}
            for event in data['file']:
                cur_ev_type=event['event_type']
                cur_mnth=event['date'].month
                cur_yr=event['date'].year
                if cur_ev_type in map:
                    map[cur_ev_type]['total_count']+=event['count']
                    if cur_mnth in map[cur_ev_type] and map[cur_ev_type][cur_mnth]['min_count']>event['count']:
                        map[cur_ev_type][cur_mnth]['min_count']=event['count']
                        map[cur_ev_type][cur_mnth]['max_year']=cur_yr
                        map[cur_ev_type][cur_mnth]['min_year']=cur_yr
                    elif cur_mnth in map[cur_ev_type] and map[cur_ev_type][cur_mnth]['min_count']==event['count']:
                        
                        map[cur_ev_type][cur_mnth]['max_year']=max(cur_yr,map[cur_ev_type][cur_mnth]['max_year'])
                        map[cur_ev_type][cur_mnth]['min_year']=min(cur_yr,map[cur_ev_type][cur_mnth]['min_year'])
                    elif not cur_mnth in map[cur_ev_type]:
                        map[cur_ev_type][cur_mnth]={}
                        map[cur_ev_type][cur_mnth]['min_count']=event['count']
                        map[cur_ev_type][cur_mnth]['max_year']=cur_yr
                        map[cur_ev_type][cur_mnth]['min_year']=cur_yr
                else:
                    map[cur_ev_type]={'total_count':event['count'],cur_mnth:{'min_count':event['count'],'max_year':cur_yr,'min_year':cur_yr}}

            for type,event in map.items():
                print(f"Event_type :{type}")
                print(f"Total_event_count ;{event['total_count']}")
                print('\n')
                for mnt_name,data in event.items():
                    if mnt_name!='total_count':
                        print(f"Month:{mnt_name}")
                        print(data)
                        print("\n")
            return map
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")

# print(statistics_of_yaml())
        
class UnitTestClass(unittest.TestCase):
    def test_statistics_yaml(self):
        results=statistics_of_yaml()
        # print(results)
        expected_res_file_path='/Users/charankumarrampelli/Python_assignment/assignment1.yaml'
        with open(expected_res_file_path,'r') as exp_res:
            expected_results=yaml.safe_load(exp_res)
        self.assertEqual(results,expected_results)
if __name__=='__main__':
    unittest.main()
