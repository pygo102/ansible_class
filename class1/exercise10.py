import re
from ciscoconfparse import CiscoConfParse


def main():
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
    crypto_maps = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map", childspec="AES")

    for crypto_map in crypto_maps:
        print "crypto map: %s" % crypto_map.text  

        for child in crypto_map.children:
            m = re.search(r'set transform-set (?P<transform>\w+)', child.text)
            if m:
                print "transform: %s" % m.group('transform')
            

if __name__ == "__main__":
    main()