def getTblSql(tbl):
	tbl_dict = {
	#=================================
		"stock" : """
								create table if not exists stock (
									code text				
								);
								""",
	#================================ primary key unique not null
	}
	return tbl_dict[tbl]