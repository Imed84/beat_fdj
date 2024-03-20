import pandas as pd

files = ["all-euro-data-1993-1994.xls", "all-euro-data-1994-1995.xls", "all-euro-data-1995-1996.xls", "all-euro-data-1996-1997.xls", 
         "all-euro-data-1997-1998.xls", "all-euro-data-1998-1999.xls", "all-euro-data-1999-2000.xls", "all-euro-data-2000-2001.xls", 
         "all-euro-data-2001-2002.xls", "all-euro-data-2002-2003.xls", "all-euro-data-2003-2004.xls", "all-euro-data-2004-2005.xls", 
         "all-euro-data-2005-2006.xls", "all-euro-data-2006-2007.xls", "all-euro-data-2007-2008.xls", "all-euro-data-2008-2009.xls", 
         "all-euro-data-2009-2010.xls", "all-euro-data-2010-2011.xls", "all-euro-data-2011-2012.xls", "all-euro-data-2012-2013.xls", 
         "all-euro-data-2013-2014.xls", "all-euro-data-2014-2015.xls", "all-euro-data-2015-2016.xls", "all-euro-data-2016-2017.xls", 
         "all-euro-data-2017-2018.xlsx", "all-euro-data-2018-2019.xlsx", "all-euro-data-2019-2020.xlsx", "all-euro-data-2020-2021.xlsx", 
         "all-euro-data-2021-2022.xlsx", "all-euro-data-2022-2023.xlsx", "all-euro-data-2023-2024.xlsx"] 

df = pd.DataFrame()
# parse excel file containing several sheets
for i in files:
    data = pd.read_excel('database/' + i, sheet_name=None)
    df_temp = pd.concat(data.values(), ignore_index=True)
    df = pd.concat([df, df_temp], ignore_index=True)

print(len(df))

