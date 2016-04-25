from ciscoconfparse import CiscoConfParse


def main():
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
    crypto_entries = cisco_cfg.find_objects(r"^crypto map CRYPTO")
    
    for crypto_map in crypto_entries:
        print "crypto map entry: %s" % crypto_map.text
        for child in crypto_map.children:
            print "    child: %s" % child.text


if __name__ == "__main__":
    main()