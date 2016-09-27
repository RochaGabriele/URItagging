1) get_questionTags
    Create 8 TXT files with questions tags for all Groups:
    Example:
        number  group  level
         2059     1      1

2) get_questionText
    Create a JSON file with questions:
        "numero":    1
        "nivel":     NONE
        "assunto":   NONE
        "descricao": bla bla bla
        "entrada":   bla bla bla
        "saida":     bla bla bla
        "titulo":    bla bla bla
        
3) TagTextTogether
    Join TXT and JSON files to another JSON file:
        "numero":    1
        "nivel":     2
        "assunto":   4
        "descricao": bla bla bla
        "entrada":   bla bla bla
        "saida":     bla bla bla
        "titulo":    bla bla bla
        
4) split_dataJSON
     Divide the JSON file in train and test files randomly.
     
5) TrainTestTogether
     Join all tests and trains files in train a test file.
     


