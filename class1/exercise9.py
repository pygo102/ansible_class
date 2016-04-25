from ciscoconfparse import CiscoConfParse


def main():
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
    pfs_entries = cisco_cfg.find_objects(r"pfs group2")
    
    print "Entries using pfs group2:"
    for pfs_entry in pfs_entries:
        if pfs_entry.is_child:
            print pfs_entry.parent.text


if __name__ == "__main__":
    main()