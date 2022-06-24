# Power Query code for data visualization
```batch
for /l %i in (1,1,100) do convert_to_xml_Performance_Test.py >> Performance_Test.csv
```

```powerquery
First_table
let
    Source = Csv.Document(File.Contents("path\to\Performance_Test.csv"),[Delimiter=",", Columns=16, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Removed Columns" = Table.RemoveColumns(Source,{"Column7", "Column8", "Column9", "Column10", "Column11", "Column12", "Column13", "Column14", "Column15", "Column16"}),
    #"Promoted Headers" = Table.PromoteHeaders(#"Removed Columns", [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"Start_time", type number}, {"Read_Time", type number}, {"Load_Time", type number}, {"cid_time", type number}, {"Process_Time", type number}, {"End_Time", type number}})
in
    #"Changed Type"
```

```
Second_table
let
    Source = Excel.CurrentWorkbook(){[Name="****First_table****"]}[Content],
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Start_time", type number}, {"Read_Time", type number}, {"Load_Time", type number}, {"cid_time", type number}, {"Process_Time", type number}, {"End_Time", type number}}),
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"cid_time"}),
    #"Added Custom" = Table.AddColumn(#"Removed Columns", "Read_delta", each [Read_Time]-[Start_time]),
    #"Added Custom1" = Table.AddColumn(#"Added Custom", "Load_delta", each [Load_Time]-[Read_Time]),
    #"Added Custom2" = Table.AddColumn(#"Added Custom1", "Process_delta", each [Process_Time]-[Load_Time]),
    #"Added Custom3" = Table.AddColumn(#"Added Custom2", "Write_time", each [End_Time]-[Process_Time]),
    #"Added Custom4" = Table.AddColumn(#"Added Custom3", "Total", each [End_Time]-[Start_time]),
    #"Removed Columns1" = Table.RemoveColumns(#"Added Custom3",{"Start_time", "Read_Time", "Load_Time", "Process_Time", "End_Time"})
in
    #"Removed Columns1"
```