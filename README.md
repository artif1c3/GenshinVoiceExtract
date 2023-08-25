# Genshin Dialogue Extractor

This is mainly used to extract dialogue from <a href="https://github.com/w4123/GenshinVoice">溯洄/w4123's GenshinVoice</a> and convert to csv.  

Set path to directory containing result.json and change value for data_name 'Keqing'.  

    os.chdir("path/to/result.json")
    data_name, data_type = 'Keqing', 'Dialog'