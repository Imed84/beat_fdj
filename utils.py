def fill_odds(row):
    if 'B365H' in row.index and pd.notna(row['B365H']):
        row['BH'] = row['B365H']
        row['BD'] = row['B365D']
        row['BA'] = row['B365A']
        return row  
    elif 'BWH' in row.index and pd.notna(row['BWH']):
        row['BH'] = row['BWH']
        row['BD'] = row['BWD']
        row['BA'] = row['BWA']
        return row
    elif 'IWH' in row.index and pd.notna(row['IWH']):
        row['BH'] = row['IWH']
        row['BD'] = row['IWD']
        row['BA'] = row['IWA']
        return row
    elif 'BSH' in row.index and pd.notna(row['BSH']):
        row['BH'] = row['BSH']
        row['BD'] = row['BSD']
        row['BA'] = row['BSA']
        return row
    elif 'WHH' in row.index and pd.notna(row['WHH']):
        row['BH'] = row['WHH']
        row['BD'] = row['WHD']
        row['BA'] = row['WHA']
        return row
    elif 'VCH' in row.index and pd.notna(row['VCH']):
        row['BH'] = row['VCH']
        row['BD'] = row['VCD']
        row['BA'] = row['VCA']
        return row
    elif 'SYH' in row.index and pd.notna(row['SYH']):
        row['BH'] = row['SYH']
        row['BD'] = row['SYD']
        row['BA'] = row['SYA']
        return row
    elif 'SJH' in row.index and pd.notna(row['SJH']):
        row['BH'] = row['SJH']
        row['BD'] = row['SJD']
        row['BA'] = row['SJA']
        return row
    elif 'SBH' in row.index and pd.notna(row['SBH']):
        row['BH'] = row['SBH']
        row['BD'] = row['SBD']
        row['BA'] = row['SBA']
        return row
    elif 'SOH' in row.index and pd.notna(row['SOH']):
        row['BH'] = row['SOH']
        row['BD'] = row['SOD']
        row['BA'] = row['SOA']
        return row
    elif 'PSH' in row.index and pd.notna(row['PSH']):
        row['BH'] = row['PSH']
        row['BD'] = row['PSD']
        row['BA'] = row['PSA']
        return row
    elif 'LBH' in row.index and pd.notna(row['LBH']):
        row['BH'] = row['LBH']
        row['BD'] = row['LBD']
        row['BA'] = row['LBA']
        return row
    elif 'GBH' in row.index and pd.notna(row['GBH']):
        row['BH'] = row['GBH']
        row['BD'] = row['GBD']
        row['BA'] = row['GBA']
        return row

    return row


files = ["all-euro-data-1993-1994.xls", "all-euro-data-1994-1995.xls", "all-euro-data-1995-1996.xls", "all-euro-data-1996-1997.xls", 
         "all-euro-data-1997-1998.xls", "all-euro-data-1998-1999.xls", "all-euro-data-1999-2000.xls", "all-euro-data-2000-2001.xls", 
         "all-euro-data-2001-2002.xls", "all-euro-data-2002-2003.xls", "all-euro-data-2003-2004.xls", "all-euro-data-2004-2005.xls", 
         "all-euro-data-2005-2006.xls", "all-euro-data-2006-2007.xls", "all-euro-data-2007-2008.xls", "all-euro-data-2008-2009.xls", 
         "all-euro-data-2009-2010.xls", "all-euro-data-2010-2011.xls", "all-euro-data-2011-2012.xls", "all-euro-data-2012-2013.xls", 
         "all-euro-data-2013-2014.xls", "all-euro-data-2014-2015.xls", "all-euro-data-2015-2016.xls", "all-euro-data-2016-2017.xls", 
         "all-euro-data-2017-2018.xlsx", "all-euro-data-2018-2019.xlsx", "all-euro-data-2019-2020.xlsx", "all-euro-data-2020-2021.xlsx", 
         "all-euro-data-2021-2022.xlsx", "all-euro-data-2022-2023.xlsx", "all-euro-data-2023-2024.xlsx"] 
